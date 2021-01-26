import datetime, time, csv, sys, os
try:
	from Update import *
except:
	pass


def main():
	#Figlet for ZoomBuddy
	print(" _____                     ____            _     _\n|__  /___   ___  _ __ ___ | __ ) _   _  __| | __| |_   _\n  / // _ \\ / _ \\| '_ ` _ \\|  _ \\| | | |/ _` |/ _` | | | |\n / /| (_) | (_) | | | | | | |_) | |_| | (_| | (_| | |_| |\n/____\\___/ \\___/|_| |_| |_|____/ \\__,_|\\__,_|\\__,_|\\__, |\n                                                   |___/")
	if getattr(sys, 'frozen', False):
		update()
	if len(sys.argv) == 1:
		auto()
	else:
		manual()

def auto():
	#Open the ZoomData csv file and skip first line (since it's the formatting)
	try:
		file = open('ZoomData.csv', 'r')
		csvfile = csv.reader(file)
		next(csvfile)
	except FileNotFoundError:
		print("ZoomData.csv Does Not Exist!!!")
		print("Follow the instructions on Github to setup ZoomData.csv")
		time.sleep(5)
		sys.exit()
	

	#Get time and date
	day = datetime.datetime.today().weekday()
	time = int(datetime.datetime.now().strftime("%H"))*60 + int(datetime.datetime.now().strftime("%M"))

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
	#Open the ZoomData csv file and skip first line (since it's the formatting)
	try:
		file = open('ZoomData.csv', 'r')
		csvfile = csv.reader(file)
		next(csvfile)
	except FileNotFoundError:
		print("ZoomData.csv Does Not Exist!!!")
		print("Follow the instructions to setup ZoomData.csv")
		time.sleep(5)
		sys.exit()

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
		sys.exit()
	connect(meetingID, passWD)

def connect(meetingID, passWD):
	if sys.platform == "linux" or sys.platform == "linux2":
		print("Linux is currently unsupported. Please open an issue with the installation location and it will be added")
	elif sys.platform == "darwin":
		print("MacOS is currently unsupported. Please open an issue with the installation location and it will be added")
	elif sys.platform == "win32":
		Path = "%appdata%\\Zoom\\bin\\Zoom.exe"
	else:
		print("Operating System unknown. Please manually set this is the python file")
		sys.exit()

	#Command to join zoom meeting
	command= Path + " --url=zoommtg://zoom.us/join?confno=" + meetingID + "^&pwd=" + passWD

	#Execute command
	os.system(command)
	sys.exit()

if __name__ == "__main__":
	main()