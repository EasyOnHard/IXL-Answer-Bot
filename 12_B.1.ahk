t::
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

return

$^i::
{
 Loop
 {
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
