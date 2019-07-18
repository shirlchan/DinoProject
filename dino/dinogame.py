print("You have been selected as a time travler and have been sent back to the jurastic age!")
name=input("What is your name?\n")
print("Hello "+ name)
def center():
    direction=input("Do you want to walk" + ' "left" ' + "or" + ' "right" \n')
    if direction=="left":
        dino()
    elif direction=="right":
        dinopoop()
def dinopoop():
    print("EW, you stepped on dino poop")
    a=input('type "back" to go back to the machine\n')
    if a=="back":
        center()
def dino():
    print("OH NO, you see a sleeping t-rex")
    b = input("What do you want to do?" + ' "pet the dino" ' + " or " + ' "walk away" \n')
    if b == "pet the dino":
        print("Are you really gonna pet a dinosaur? ok if you say so.")
        dinowakes()
    if b == "walk away":
        print("you trip and make a loud noise")
        dinowakes()
def dinowakes():
    print("RAWRRRRRRRR! The dino woke up!")
    c=input("What do you want to do?" + ' "run away" ' + " or " + ' "hide" \n')
    if c== "run away":
        dinosleep()
    elif c=="hide":
        dinobush()
def dinobush():
    print("you hear a little growl behind you and look back...")
    print("GAME OVER")
    tryAgain()
def dinosleep():
    print("While you're running you look back and see the t-rex fell back asleep.")
    d = input("Do you want to go back to the machine" + ' "yes" ' + "or" + ' "no" \n' )
    if d == "yes":
        broken()
    elif d == "no":
        print("Too bad you have no choice")
        broken()
def broken():
    e = input("You go to the time machine and realize that it's out of battery, but luckily theres another one to the northeast. Don't ask how it got there. Do you want to go through the"+ ' "forest" '+ " or"+ ' "plains"\n' )
    if e== "plains":
        print("As you travel through the plains, you look up and see a pteridactyl swooping down towards you with its mouth open...")
        print("GAME OVER")
        tryAgain()
    if e== "forest":
        forest()
def forest():
    f=input("As you travel through the forest, you see a velociraptor. Do you want to" + ' "run" '+ "or"+ ' "give up"\n' )
    if f=="run":
        print("Once you start running, the velociraptor chases after you and its friends come after you...")
        print("GAME OVER")
        tryAgain()
    if f=="give up":
        end()
def end(): 
    print("The velociraptor wanted a chase but now you're boring it and it leaves. ")
    g=input("You keep walking and you find the time machine. Do you want to go " + '"back to the future"'+ " or "+'"explore more"\n')
    if g=="back to the future":
        print("After "+name+" returns to the future,"+name+" becomes the world leading expert on dinosaurs.")
        print("THE END")
        print("Original story written by Shirley and Dahriel")
    if g=="explore more":
        print(name+" stays in the jurastic era. Years later,"+name+"'s fossil is found and people are confused at how there could be such a old human fossil.")
        print("THE END")
        print("Original story written by Shirley and Dahriel")
def tryAgain():
    want = input("Do you want to try again" + ' "yes" ')
    if want == "yes":
        print("Hello "+ name)
        center()
center()