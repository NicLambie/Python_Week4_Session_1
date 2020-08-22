# question 1

moths_in_the_house = True

if moths_in_the_house:
    print("Get the moths, Roary!")
else:
    print("No threat detected, Rorary.")

#question2

moths_in_the_house = True
mitch_is_home = True

if moths_in_the_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")

moths_in_the_house = False
mitch_is_home = False

if not moths_in_the_house and not mitch_is_home:
    print("No threats detected.")

moths_in_the_house = True
mitch_is_home = False

if moths_in_the_house and not mitch_is_home:
    print("Meoooooow! Hissssss!")

moths_in_the_house = False
mitch_is_home = True

if not moths_in_the_house and mitch_is_home:
    print("Climb on Mitch.")


#question3

#need to define light colour
#light colour will be red, amber or green
#car_detected will be true or false



light_colour = "red"
car_detected = False

if light_colour is red and not car_detected:
    print("Do nothing.")