print("You have been selected as a time travler and have been sent back to the jurastic age!")
name=input("What is your name?")
print("Hello "+ name)
def center():
    direction=input("Do you want to walk left or right?")
    if direction=="left":
        dino()
    elif direction=="right":
        dinopoop()
def dinopoop():
    print("EW, you stepped on dino poop")
    a=input('type "back" to go back to the machine')
    if a=="back":
        center()
def dino():
    print("OH NO, you see a sleeping t-rex")
    b = input("What do you want to do?" + ' "pet the dino" ' + " or " + ' "walk away" ')
    if b == "pet the dino":
        print("Are you really gonna pet a dinosaur? ok if you say so.")
        dinowakes()
    if b == "walk away":
        print("you trip and make a loud noise")
        dinowakes()
def dinowakes():
    print("RAWRRRRRRRR! The dino woke up!")
    c=input("What do you want to do?" + ' "run away" ' + " or " + ' "hide" ')
    if c== "run away":
        dinosleep()
    elif c=="hide":
        dinobush()
def dinobush():
    print("you hear a little growl behind you and look back...")
    print("GAME OVER")
def dinosleep():
    print("While you're running you look back and see the t-rex fell back asleep.")
    d = input("Do you want to go back to the machine" + ' "yes" ' + "or" + ' "No" ' )
    if d == "yes":
        broken()
    elif d == "no":
        print("Too bad you have no choice")
        broken()
def broken():
    e = input("You realize the time machine is out of battery, but luckily theres another one to northeast. Don't ask how it got there")
        
        
        


























































center()