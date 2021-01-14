import datetime, os, csv, sys

def main():
	if len(sys.argv) == 1:
		auto()
	else:
		manual()

def auto():
	#Open the ZoomData csv file and skip first line (since it's the formatting)
	file = open('ZoomData.csv', 'r')
	csvfile = csv.reader(file)
	next(csvfile)

	#Get time and date
	day = datetime.datetime.today().weekday()
	now = float(datetime.datetime.now().strftime("%H.%M"))

	#Iterate through ZoomData.csv to find the specified class
	for row in csvfile:
		try:
			if (now>float(row[day+4])-0.15) and (now<float(row[day+4])+0.15):
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
	file = open('ZoomData.csv', 'r')
	csvfile = csv.reader(file)
	next(csvfile)

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
	#Command to join zoom meeting
	command="%appdata%\\Zoom\\bin\\Zoom.exe --url=zoommtg://zoom.us/join?confno=" + meetingID + "^&pwd=" + passWD

	#Execute command
	os.system(command)
	sys.exit()

if __name__ == "__main__":
	main()