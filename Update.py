import requests, webbrowser, json, time, sys

VERSION = "1.0.4"
Update_URL = 'https://api.github.com/repos/mnthomson/zoombuddy/releases/latest'

def update():
	response = requests.get(Update_URL).text
	data = json.loads(response)
	CURRENT_VERSION = data['tag_name'].split("v")[1]

	if (int(VERSION.replace('.','')) < int(CURRENT_VERSION.replace('.',''))):
		print("Downloaded Version:  " + VERSION)
		print("Current Version:     " + CURRENT_VERSION)
		Choice = input('Would you like to update ZoomBuddy? (Y/N)')
		if Choice.lower() == 'yes' or Choice.lower() == 'y':
			#Yes to update
			print('Redircting...')
			webbrowser.open(Update_URL)
			sys.exit(0)

		else:
			pass
	else:
		pass

if __name__ == "__main__":
	start_time = time.time()
	update()
	print("--- %s seconds ---" % (time.time() - start_time))