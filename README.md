<h1 align="center">
		<a href="https://github.com/MNThomson/ZoomBuddy">
			<img src=assets/ZoomBuddy.png alt="ZoomBuddy Logo" width="200">
		</a>
	<br>
		Zoom Buddy
	<br>
</h1>
<h4 align="center">
	Automatically Join Scheduled Zoom calls
</h4>
<p align="center">
  <a href="https://github.com/MNThomson/ZoomBuddy/releases/latest"><img src="https://img.shields.io/github/release/MNThomson/ZoomBuddy.svg?style=for-the-badge" alt="github release version"></a>
  <a href="https://github.com/MNThomson/ZoomBuddy/releases/latest"><img src="https://img.shields.io/github/downloads/MNThomson/ZoomBuddy/total?style=for-the-badge" alt="github release downloads"></a>
  <a href="https://github.com/MNThomson/Test/commit"><img src="https://img.shields.io/github/last-commit/MNThomson/ZoomBuddy?style=for-the-badge" alt="github last commit"></a>
</p>
<h4 align="center">
	<a href="https://github.com/MNThomson/ZoomBuddy/releases/latest">
		🔰 Download ZoomBuddy 🔰
	</a>
</h4>


## Install

### Recommended Install

Download the latest version of ZoomBuddy from the [Releases page](https://github.com/MNThomson/ZoomBuddy/releases/latest).

### Advanced Install

- Try the development version by cloning the Git repository:
	```sh
	$ git clone https://github.com/MNThomson/ZoomBuddy.git
	```

- Run `ZoomBuddy.py` from the command line:
	```sh
	$ python3 ZoomBuddy.py
	```

- Build your own executable through [Pyinstaller](https://pypi.org/project/pyinstaller) with the command:
	```sh
	$ pyinstaller --onefile --clean --distpath . --icon=assets/ZoomBuddy.ico ZoomBuddy.py
	```

## Setup

A file `EXAMPLE_ZoomData.csv` is provided. Rename this to `ZoomData.csv` in the same folder as `ZoomBuddy.exe` with your meeting ID's and passwords. Time is in 24hr format with a `:` between the hour and minute (e.g. `6:45PM` would be `18:45`).

## Usage

Run the executable `ZoomBuddy.exe` (or the `.py`) and it will search for `ZoomData.csv`. If a Zoom call is happening within ±15mins, ZoomBuddy will automatically join that call. If it cannot detect a meeting, a window will open asking which meeting (in `ZoomData.csv`) to join

If any cli argument is given, it will launch into the selection mode and bypass checking which meeting to join

# Annoying Smart Screen Warning

On some Windows PC's, Windows Smart Screen will trigger when running an unknown file. If this happens, right click on the file and click on `properties`. At the bottom of the pop-up there is a section which says `Security: This file came from another computer...`, just click the button to the right titled `Unblock` and Windows Smart Screen will no longer trigger

## To Do

- [x] Add update function
- [x] Add code to check if version is current
- [x] Fix the time system to be base 60
- [x] Download example csv if not detected (option box)
- [ ] Add MacOS/Linux support (find binary installation location)
- [ ] Add system tray icon
- [ ] Refactor imports to make the executable smaller