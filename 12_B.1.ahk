^m::
xpos := ""
ypos := ""
MouseGetPos xpos, ypos 
MsgBox The cursor is at (%xpos%,%ypos%) ; Returns the Mouse Position as an ordered pair.
return

^t::             ; Testing Macro
Sleep 350
Click 600, 325   ; Clicks to answer question. The Click function works with x then y.
Sleep 10
Click 600, 375   ; Clicks lower to make sure it did not miss
Sleep 10
Send {Enter}     ; Submit Answer
Sleep 900
Click 1220, 505  ; Clicks "Got it" just in case the answer was incorrect
Sleep 10
Click 1220, 525  ; Clicks lower to make sure it did not miss
Sleep 10
Click 1220, 590  ; Clicks lower to make sure it did not miss
return

$^i::
{
   Loop {
      Sleep 350
      Click 600, 325
      Sleep 10
      Click 600, 375
      Sleep 10
      Send {Enter}
      Sleep 900
      Click 1220, 505
      Sleep 10
      Click 1220, 525
      Sleep 10
      Click 1220, 590
   }
Return
}

Esc::
Suspend, Off
Pause, Off, 1
If (toggle := !toggle) {
   Suspend, On
   Pause, On, 1
}
