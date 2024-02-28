### I need to update this!
******

## An IXL Bot
I don't like IXL but I do like to code, so I decided to make this. This repo uses Auto Hot Key (AHK) to automatically answer questions for IXL. As of now it can only do B.1 in twelvth grade.

## Disclaimer!!
Please do not use this to cheat on IXL. Answer quiestions by hand until you understand the lopic, and if you are doing a leaderboard, use this for Goofs and Giggles. Use the honor system!

## Prerequisites 
To use this script, you need Windows 10/11 and to install AHK from [here](https://www.autohotkey.com/download/ "AHK Download"). Be sure to install the latest version. 

## Setup
To start, copy the `12_B.1` file onto your computer, making sure that it is still an `.ahk` file. Right click it and open it with the AHK launcher. Go to [B.1](https://www.ixl.com/ela/grade-12/which-text-is-most-formal) in twelvth grade and hit `Ctrl+Caps+i` to start the macro. If it works fine, Congrats! If it does not, you will need to fix it! **PS: Hit `enter` to kill the script!**

## Modifying the Code
All of the mouse positions in this program are hardcoded, meaning that you may have to modify them by going into the file and tweaking them individually (Sorry!). To change the positions, open the file be right clicking on it and opening it with Notepad or something of the like. You should now see the code. Navagate to where it says `^t::`. This is the testing macro. You will see multiple `Click` functions, and those are what you need to modify. Go back to IXL and hit `Ctrl+m` over the first answer to get the mouse position. Put that number into the first `Click`, and make the y-value for the second click a bit higher, but keep the x-value the same. Back in IXL, get the question wrong and find the `Got it` button. Hit `Ctrl+m` over the top of the buttion and put it into the 3rd `Click`. Keep the x-value the same for all three, but make the y-value a bit higher each time. Save the script and run it. Go to IXL and hit `Ctrl+t` to test it. If it works a few times in a row, put that code into the main loop at `$^i::`, save it, and Voilà, you are set! If it does not work multiple times in a row, change the positions ultil they work.
******
If you want to change the keybinds, refer to the [doc](https://www.autohotkey.com/docs/v2/Hotkeys.htm).  
This repo should be relatively secure and safe, but AHK can get stuck in loops!
