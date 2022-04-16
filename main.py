import sys, requests


class GetCurrentRelease:

    def __init__(self):
        # Add the URL to latest releases from GitHub Repo. Keep api.* as subdomain.
        self.json_url = "https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest"
        self.important_module = "requests"
        # To store current release version and also given assets.
        self.current_version = ""
        self.assets = ""

    # Start communicating with GitHub API.
    def readJSONData(self):
        try:
            getjson_data = requests.get(self.json_url)
            if getjson_data.status_code == 200:
                json_data = getjson_data.json()
                # You may want to use 'tag_name' or 'name'. Seems like GitHub stores the current version number
                # in tag_name or name.
                self.current_version = json_data['name']
                # Assets contains the downloadable archives with corresponding names, download URLs and more.
                # Do not change this as assets is the part we want to have.
                self.assets = json_data['assets']
        except requests.exceptions.RequestException as ex:
            print ('ERROR while running: ' + ex)
        except requests.exceptions.Timeout as timEx:
            print ('Timeout Exception: ' + timEx)

    # Just because we need requests. Do not change anything in here.
    def getModules(self):
        if self.important_module in sys.modules:
            return bool(True)
        else:
            return bool(False)

    # Everything to print.
    def createUI(self):
        # Current Version means latest version that was uploaded to GitHub.
        print ('Current Version: ' + self.current_version)
        # You can print everything whats inside of assets.
        for values in self.assets:
            # Prints the current archive name and its corresponding download URL.
            print (values['name'] + ': ' + values['browser_download_url'])

    # To run everything what we need. 
    def run(self):
        # Lets see if requests is intalled. 
        if self.getModules() == bool(True):
            # First we want to read the JSON File
            self.readJSONData()
            # Then we print the printable stuff.
            self.createUI()
        else:
            # Just to tell why its not working.
            print ('You need to install ' + self.important_module)


# Lets run everything.
if __name__ == '__main__':
    rel = GetCurrentRelease()
    rel.run()

