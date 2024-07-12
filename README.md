# Note: Mac/Linux does not currently work.

## I have stopped work on this repo. Thanks to anyone who tried it!

## An IXL Bot
I don't like IXL but I do like to code, so I decided to make this. This repo uses Auto Hot Key (AHK) to automatically answer questions for IXL. As of now it can only do B.1 for twelvth grade and M.1 for eighth.

## Disclaimer!!
Please do not use this to cheat on IXL. Answer questions by hand until you understand the topic, and if you are doing a leaderboard, use this for Goofs and Giggles. Use the honor system!

# AHK
## Prerequisites 
To use this script, you need Windows 10/11 and to install AHK from [here](https://www.autohotkey.com/download/ "AHK Download"). Be sure to install the latest version. 
## Setup
To start, copy the `12_B.1` file onto your computer, making sure that it is still an `.ahk` file. Right click it and open it with the AHK launcher. Go to [B.1](https://www.ixl.com/ela/grade-12/which-text-is-most-formal) in twelvth grade and hit `Ctrl+Caps+i` to start the macro. If it works fine, Congrats! If it does not, you will need to fix it! **PS: Hit `enter` to kill the script!**
## Modifying the Code
All of the mouse positions in this program are hardcoded, meaning that you may have to modify them by going into the file and tweaking them individually (Sorry!). To change the positions, open the file be right clicking on it and opening it with Notepad or something of the like. You should now see the code. Navagate to where it says `^t::`. This is the testing macro. You will see multiple `Click` functions, and those are what you need to modify. Go back to IXL and hit `Ctrl+m` over the first answer to get the mouse position. Put that number into the first `Click`, and make the y-value for the second click a bit higher, but keep the x-value the same. Back in IXL, get the question wrong and find the `Got it` button. Hit `Ctrl+m` over the top of the buttion and put it into the 3rd `Click`. Keep the x-value the same for all three, but make the y-value a bit higher each time. Save the script and run it. Go to IXL and hit `Ctrl+t` to test it. If it works a few times in a row, put that code into the main loop at `$^i::`, save it, and Voilà, you are set! If it does not work multiple times in a row, change the positions ultil they work.

# Python
## About 
At first project was only for Windows, but I soon realized that many people do not have Windows, thus they cannot use this repository. That is why I added the Python folder. Python SHOULD be compatible with Mac and Linux, but it seems to not work. If you can, fork this repo and submit a pull request if you fix it.
## Prerequisites
Installing Python is a bit more complicated than AHK, but it is fairly straightforward. First, you will need Python 3.10.6. download that [here](https://www.python.org/downloads/release/python-3106/).  Next, you will need a Virtual Environment (venv). These can be a bit complicated, but they work. Watch the videos below for instructions:  

- [Windows](https://youtu.be/APOPm01BVrk?si=L-mjL20vjYLZV_P2)
- [Mac/Linux](https://youtu.be/Kg1Yvry_Ydk?si=v4lI9A4fV9bQa0RY)  

Terminal interfacing is really not all that bad after you get used to it. I have the `requirements.txt` in the python folder, so download that file into the same folder as your venv and run the following code in the Terminal:  
`pip install -r requirements.txt`  
If all goes well, you should see pip do its stuff and download the required python modules into the venv. To now run the script, go into its file and run  
`python B_M.1.py`.  
You do not need to modify the code to change mouse positions.

******
If you want to change the keybinds, refer to the [doc](https://www.autohotkey.com/docs/v2/Hotkeys.htm).  
This repo should be relatively secure and safe, but AHK can get stuck in loops!
