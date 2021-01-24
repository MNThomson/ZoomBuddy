import requests, webbrowser, sys

VERSION = "1.0.1"
URL = 'https://github.com/MNThomson/ZoomBuddy/releases/latest'

def update():
	r = requests.get(URL)
	CURRENT_VERSION = r.url.split("v")[1]

	if (int(VERSION.replace('.','')) < int(CURRENT_VERSION.replace('.',''))):
		print("Downloaded Version:  " + VERSION)
		print("Current Version:     " + CURRENT_VERSION)
		Choice = input('Would you like to update ZoomBuddy? (Y/N)')
		if Choice.lower() == 'yes' or Choice.lower() == 'y':
			#Yes to update
			print('Redircting...')
			webbrowser.open(URL)
			sys.exit()

		else:
			pass
	else:
		pass