from mistyPy.Robot import Robot

misty = Robot("192.168.0.92")

misty.changeLED(255, 255, 255)
misty.display_image("e_DefaultContent.jpg")

#driving for delivery
misty.drive_time(40, 20, 500)

#gets stuck

#red light starts blinking
misty.transition_led(255, 0, 0, 0, 0, 0, 'Blink', 30)

#sad expression
misty.display_image("e_EcstacyJoy.jpg")

#looks towards the user
misty.move_head(-40, 0, 30, 120)

#looks back at the door
misty.move_head(0, 0, 0, 120)

#points to the door
misty.move_arm("right", 90, 80)

#looks back at the user
misty.move_head(-40, 0, 30, 120)
#and says
misty.speak("Hi there! I'm a delivery bot who's here to deliver a package. I am stuck. Could you do me a favor and open the door for me? Your kindness is much appreciated. Thank you!”)
            
#looks back at the door
misty.move_head(0, 0, 0, 120)
#and changes the LED to white
misty.changeLED(255, 255, 255)

#becomes content after the help is provided
misty.display_image("e_Joy2.jpg")
misty.speak("Thank you for your kindness. I genuinely appreciate your assistance. Have a wonderful day.")
misty.changeLED(0, 255, 0)

#drives away
misty.drive(40, 0)
misty.halt()
