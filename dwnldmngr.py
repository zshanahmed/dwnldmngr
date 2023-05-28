#!/usr/bin/env python3

import sys
import time
import logging
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder names and their corresponding file extensions
with open('file_map.json') as f:
    file_paths = json.load(f)

class CustomHandler(FileSystemEventHandler):
    def on_created(self, event): # event triggered when a file is created
        logging.info(f'event type: {event.event_type}  path : {event.src_path}')
        file_extension = event.src_path.split('.')[-1]
        file_name = event.src_path.split('/')[-1]
        for key, value in file_paths.items():
            if file_extension in value:
                curr_dir = os.path.dirname(event.src_path)
                new_path = f'{curr_dir}/{key}'
                if not os.path.exists(new_path): # if folder doesn't exist, create it
                    os.makedirs(new_path)
                if os.path.exists(f'{new_path}/{file_name}') and os.path.getsize(f'{new_path}/{file_name}') != os.path.getsize(event.src_path): # if file already exists and the size is different
                    new_file_name = f'{file_name.split(".")[0]}_{int(time.time())}.{file_extension}'
                    logging.info(f'File {file_name} already exists in {new_path}. Renaming to {new_file_name}')
                    os.rename(event.src_path, f'{new_path}/{new_file_name}')
                else:
                    os.rename(event.src_path, f'{new_path}/{event.src_path.split("/")[-1]}') # move the file to the corresponding folder
                logging.info(f'File {file_name} moved to {new_path}')
                break

if __name__ == '__main__':
    logging.basicConfig(filename='output.log',
                        filemode='a',
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.' # path to watch / if not given use current directory
    observer = Observer()
    logging.info(f'Dwnldmngr started. Watching {path}')
    event_handler = CustomHandler()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt: # if keyboard interrupt, stop the observer
        observer.stop()
    observer.join()