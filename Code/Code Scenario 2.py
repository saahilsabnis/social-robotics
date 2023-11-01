from mistyPy.Robot import Robot

misty = Robot("192.168.0.92")

misty.changeLED(255, 255, 255)
misty.drive_time(0, 0, 0, 1000)
misty.display_image("e_DefaultContent.jpg")

misty.display_image("e_EcstacyJoy.jpg")

misty.move_head(-40, 0, 40, 60)

misty.move_arm("right", 90, 60)

misty.speak("I am stuck, please help me")


misty.move_head(-40, 0, 30, 120)

misty.changeLED(0, 255, 0)

misty.display_image("e_Joy2.jpg")

misty.drive(40, 0, 5000)
