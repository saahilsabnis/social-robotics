from mistyPy.Robot import Robot

misty = Robot("192.168.0.92")

misty.changeLED(0, 0, 255)
misty.drive(40, 20)
misty.halt()
misty.display_image("e_DefaultContent.jpg")
misty.speak("Hello, world!")
misty.display_text("Hello, world!")