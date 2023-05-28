# Dwnldmngr - A simple background service to keep your downloads organized
Dwnldmngr is a background service that helps keep your downloads organized 

## Usage
- Install `watchdog` package: `pip install watchdog`
- Customize `file_map.json` if required
  - `file_map.json` has file extensions organized as list of values with the folder name as keys in the json
- Run python script and provide the *Downloads* folder path (*current directory is consider if no parameter is provided*): `python dwnldmngr /path/to/downloads`
- You can keep track of logs in `output.log` file in folder where dwnldmngr is located

### Run dwnldmngr as a background service
- Make `dwnldmngr` an executable file: `chmod +x dwnldmngr`
- Run `dwnldmngr` as a background service (and provide *Downloads* folder path):  `./dwnldmngr.py /path/to/downloads &`

### Stop dwnldmngr background service:
- Find the dwnldmngr process id: `ps aux | grep dwnldmngr`
- Kill the process: `kill *pid*`