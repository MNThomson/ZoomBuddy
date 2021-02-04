import webbrowser, requests, json, csv, sys

from os import system, name
from datetime import datetime
from time import sleep

VERSION = "1.0.4"
URL = "https://github.com/MNThomson/ZoomBuddy"
API_URL = 'https://api.github.com/repos/mnthomson/zoombuddy/releases/latest'
Update_URL = 'https://github.com/MNThomson/ZoomBuddy/releases/latest'

def main():
	figlet()
	update()
	if len(sys.argv) == 1:
		auto()
	else:
		manual()

def figlet():
	#Figlet for ZoomBuddy
	print("\
 _____                     ____            _     _\n\
|__  /___   ___  _ __ ___ | __ ) _   _  __| | __| |_   _\n\
  / // _ \\ / _ \\| '_ ` _ \\|  _ \\| | | |/ _` |/ _` | | | |\n\
 / /| (_) | (_) | | | | | | |_) | |_| | (_| | (_| | |_| |\n\
/____\\___/ \\___/|_| |_| |_|____/ \\__,_|\\__,_|\\__,_|\\__, |")
	print("v" + VERSION, end ="")
	for i in range(1,41-len(VERSION)):
		print(" ", end ="")
	print("MNThomson |___/")

def update():
	try:
		response = requests.get(API_URL).text
	except:
		return
	data = json.loads(response)
	CURRENT_VERSION = data['tag_name'].split("v")[1]

	if (int(VERSION.replace('.','')) < int(CURRENT_VERSION.replace('.',''))):
		print("Downloaded Version: v" + VERSION)
		print("Current Version:    v" + CURRENT_VERSION)
		Choice = input('Would you like to update ZoomBuddy? (Y/N)')
		if Choice.lower() == 'yes' or Choice.lower() == 'y':
			#Yes to update
			if getattr(sys, 'frozen', False):
				print('Redircting...')
				webbrowser.open(Update_URL)
				sys.exit(0)
			else:
				print("Either run a git pull or reclone this repo.")
				Choice = input('Would you like to be redirected to the Github page? (Y/N)')
				if Choice.lower() == 'yes' or Choice.lower() == 'y':
					#Yes to update
					print('Redircting...')
					webbrowser.open(Update_URL)
					sys.exit(0)
				else:
					pass
		else:
			pass
		system('cls' if name == 'nt' else 'clear')
		figlet()
	else:
		pass

def open_data():
	#Open the ZoomData csv file and skip first line (since it's the formatting)
	try:
		file = open('ZoomData.csv', 'r')
		csvfile = csv.reader(file)
		next(csvfile)
		return file, csvfile
	except FileNotFoundError:
		print("ZoomData.csv Does Not Exist!!!")
		print("Please read the setup instructions for ZoomData.csv")
		Choice = input('Would you like to be redirected to the instructions page? (Y/N)')
		if Choice.lower() == 'yes' or Choice.lower() == 'y':
			print('Redircting...')
			webbrowser.open(URL)
		sleep(1)
		sys.exit(0)

def auto():
	#Open the ZoomData
	file, csvfile = open_data()

	#Get time and date
	day = datetime.today().weekday()
	time = int(datetime.now().strftime("%H"))*60 + int(datetime.now().strftime("%M"))

	#Iterate through ZoomData.csv to find the specified class
	for row in csvfile:
		try:
			classtime = int(row[day+4].split(":")[0]) * 60 + int(row[day+4].split(":")[1])
			if (time>classtime-15) and (time<classtime+15):
				meetingID=row[2]
				#Check if password exists
				try:
					passWD=row[3]
				except:
					passWD=""
				connect(meetingID, passWD)
		except ValueError:
			pass
	print("No meetinges found for this time!")
	manual()

def manual():
	#Open the ZoomData
	file, csvfile = open_data()

	#Print out each possible option
	print("Choose an option below:")
	for row in csvfile:
		print(row[0] + " [" + row[1] + "]")
	file.seek(1)

	#Get intended meeting
	meetingname = input("Enter a Meeting: ")

	#Find the specified meeting
	for row in csvfile:
		if (meetingname==row[1]):
			meetingID=row[2]
			#Check if password exists
			try:
				passWD=row[3]
			except:
				passWD=""
			break

	#Check if the input is not in the list
	try:
		meetingID
	except NameError:
		print("Input Invalid")
		Choice = input('Try again? (Y/N)')
		if Choice.lower() == 'yes' or Choice.lower() == 'y':
			#Yes to update
			system('cls' if name == 'nt' else 'clear')
			figlet()
			manual()
		else:
			sys.exit(0)
		sys.exit(1)
	connect(meetingID, passWD)

def connect(meetingID, passWD):
	if sys.platform == "linux" or sys.platform == "linux2":
		Path = "/opt/zoom/zoom"
		print("Linux is currently under developement. Please open a Github issue is an error occurs")
		sleep(1)
	elif sys.platform == "darwin":
		print("MacOS is currently unsupported. Please open an issue with the installation location and it will be added")
		sleep(5)
		sys.exit(1)
	elif sys.platform == "win32":
		Path = "%appdata%\\Zoom\\bin\\Zoom.exe"
	else:
		print("Operating System unknown. Please manually set this is the python file")
		sleep(5)
		sys.exit(1)

	#Command to join zoom meeting
	command= Path + " --url=zoommtg://zoom.us/join?confno=" + meetingID + "^&pwd=" + passWD

	#Execute command
	system(command)
	sys.exit(0)

if __name__ == "__main__":
	main()