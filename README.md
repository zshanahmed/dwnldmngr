# Dwnldmngr - A simple background service to keep your downloads organized
Dwnldmngr is a background service that helps keep your downloads organized 

## Usage
- Install `watchdog` package: `pip install watchdog`
- Customize `file_map.json` if required
  - `file_map.json` has file extensions organized as list of values with the folder name as keys in the json
- Run python script and provide the *Downloads* folder path (*current directory is consider if no parameter is provided*): `python main.py /path/to/downloads`
- You can keep track of logs in `output.log` file in folder where dwnldmngr is located

### Run dwnldmngr as a background service
- Make `main.py` an executable file: `chmod +x main.py`
- Run `main.py` as a background service (and provide *Downloads* folder path):  `./main.py /path/to/downloads &`