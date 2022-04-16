# CheckForOC
This repository is planned to be a Python testing repository. To make it usefull I will created something for me to check if there is a new version of OpenCore available. Due to my laziness it will support me to get new versions. ;)

## Structure
* **main.py**: Contains the whole code. Maybe I will change this in the future. 

## How to run?
* Open up a terminal window
* Install `requests` via `python3 -m pip install requests`
* Run `python3 main.py`

### Problems
* **ModuleNotFoundError: No module named 'requests'**: `python3 -m pip install requests`

## Getting Started
If you have successfully started the script you are going to see three outputs via cmd. The first one is the latest version of OpenCore (e.g. 0.7.4) and the second and third output are the main assets of the project. This means you are going to see the latest downloadable files with the corresponding download links. 
This does not include the source code files because they are not listed as assets inside GitHub .json API. 

### GitHub API 
Every release is stored inside a .json file created by GitHub API. Inside the .json you are going to see latest release number as `name` and the corresponding downloadable assets as `assets`. You can find more then this but for now it will work just fine. You could also get informations like who released this latest release etc.

### Requests via CheckForOC
`requests.get("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest")` is used to get the .json file. You could use any GitHub API link and add this to the script. As for now any .json created by GitHub API is using the same format. 
