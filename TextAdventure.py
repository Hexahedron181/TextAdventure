import time
error = "I don't understand."
no = "You can't do that."
inventory = []
speed = 0
unlocked = 0
DesSp = ["1", "2", "3", "4", "5"]
items = [["Door", "Bucket", "Ladder", "Steps", "Lock"],["Key", "Table"],["Cabinet", "Floor Hole", "Keyhole"],["Window", "Carpark", "Car", "Park"],["Bottle", "Dark"]]
inventory = []

def controls():
    print("\nTake\nOpen\nLook\ninventory\nMoving rooms: letter or word. e.g: 'R' or 'Right'\nUse: make sure you reference 2 items and you use 'With' between them\ne.g: 'Use spoon with bowl'\n")
    return

def end():
    print("\n\nWell Done, you finished the game!!")
    input("")
    exit()
    
def Menu():
    print("\nWELCOME TO *insert title*\n\n\tStart\n\n\tControls\n\n")
    while True:
        menu = input(">>> ")
        menu = menu.title()
        if menu == "Start":
            intro()
        elif menu == "Controls":
            controls()
        

def invent():
    print("")
    Num = 0
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for i in range(0, len(inventory)):
            print("{0:3}".format(inventory[Num]), end="    ")
            Num += 1
    print("")

def text(text, speed, skip):
    print("")
    if skip == 1:
        return
    if speed == 0:
        FullStop = 0.5
        Comma = 0.25
        Letter = 0.02
    else:
        FullStop = 0
        Comma = 0
        Letter = 0
    for char in text:
        if char == ".":
            print(char, end="\n")
            time.sleep(FullStop)
        elif char == ",":
            print(char, end="")
            time.sleep(Comma)
        else:
            print(char, end="")
            time.sleep(Letter)
    return

def intro():
    opening = "Well, that was…odd. One minute you’re sitting on your bed watching Revengers Assembly 2: Magnesium Dude, when there’s a flash, a strange ringing sound, and your bedroom disappears only to be replaced with…something else. You’re not sure what’s going on, but it’s weird. Instead of walls papered with Spoder-man and a desk with a brand new Z-Box 4000 on it, there are stone walls, wooden beams and floorboards, and what appears to be a bucket. There’s fuckery afoot, and you’re not sure what to do about it. Escape, probably. Yeah, escape sounds good."
    text(opening, 0, 0)
    Room1(0, speed, 0, 1, 1, 0)

def Room1(Open, descriptions, unlocked, lb, tb, cabinet):

    if "1" in DesSp:
        DesSpeed = descriptions
    else:
        DesSpeed = 1
    speed = descriptions
    room1 = 0
        
    description = "You’re in a room. Unsurprisingly, it has walls, a floor, a ceiling, and a few doors. Less unsurprising is the fact that the walls seem to be made of grey stone, the floor is faded wood, and the beams look rotten. In front of you is a large wooden door with an unfairly large padlock that seems to be holding in place an equally unfairly sized bolt. Beside the door is a ladder leading up into the ceiling. There is an open door to your left and an open door to your right. A set of steps descends into the floor behind you. A bucket sits ominously in the corner."
    text(description, DesSpeed, 0)
    if "1" in DesSp:
        DesSp.remove("1")
    
    while room1 == 0:
        print(end="\n")
        action = input(">>> ")
        action = action.title()
        act = action.split()
        l = len(act)

        if len(act) > 1:
            if "Wooden" in act:
                act.remove("Wooden")
                l = len(act)
        
        if len(act) == 0:
            room1 = 0
            

        elif act[0] == "Open":
            if act[1] == "Door"  and l<3 and Open != 1:
                text("Despite the fact that the door is very obviously locked with the aforementioned heavy duty hardware, you attempt to open the door anyway. Unsurprisingly, it doesn’t budge an inch.You touch paint to see if the ‘Wet Paint’ sign is lying, don’t you? Idiot.", speed, 0)
            elif act[1] == "Door" and l<3 and Open == 1:
                text("You slide back the bolt and pull the door open. A bright, blinding light assaults your eyeballs as you stagger through the doorway. Blinking away the dazzle you realise that you’re in Uncle Funkys Chuckle Bunker, the amusement park for old people. You have no idea how you got here, but you should probably disappear quite quickly. The place you just escaped from was the ‘Medieval House Experience’, and you just trashed the crap out of it. Quick! Run!", speed, 0)
                end()
            else:
                if act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

        elif act[0] == "Look":
            
            if act[1] == "Door" and l<3:
                text("It’s a large, heavy looking wooden door. The large padlock holding in place a large bolt suggests that someone or something wants to keep someone or something else out.", speed, 0)
            elif act[1] == "Ladder" and l<3:
                text("It’s a wooden ladder that disappears into a hole in the ceiling.", speed, 0)
            elif act[1] == "Steps"and l<3:
                text("A set of rickety steps descend into the floor behind you.", speed, 0)
            elif act[1] == "Lock" and l<3 and "Lock" in items[0]:
                text("It’s a black, heavy duty padlock, with a huge keyhole. The entire thing wouldn’t look out of place on a show called ‘Holy Crap!! Look at the size of that Lock!!’.", speed, 0)

            elif act[1] == "Bucket" and l<3 and lb !=8 and "Bucket" in items[0]:
                
                if lb == 1:
                    B = "It’s just a wooden bucket. An oddly ominous wooden bucket, but still just a bucket."
                elif lb == 2:
                    B = "Still just a bucket. Still just as ominous."
                elif lb == 3:
                    B = "Seriously, it’s a freaking bucket. What else do you want me to say?  It’s round. It’s made of wood. It has a metal handle. The ominous way it just sits there gives you the heebie-jeebies, like it’s watching you, waiting for its chance to pounce…oh."
                elif lb == 4:
                    B = "The bucket pounces, making straight for your neck with it’s now obviously razor-sharp handle. You duck just in time and the scary receptacle smashes itself to pieces on the wall behind you.\nYou: 1 Ominous Wooden Hell Bucket: 0."
                elif lb == 5:
                    B = "Stop."
                elif lb == 6:
                    B = "Well done you made the game unfun. You hereby are awarded a medal. are you happy now."
                elif lb == 7:
                    B = "No. You know what. <<P:/line128/Bucket/Look/Remove()/>>. that might have been useful now you'll never know."
                    items[0].remove("Bucket")
                text(B, speed, 0)
                lb += 1

            else:
                if act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

        elif act[0] == "Take":
            if act[1] == "Bucket" and l<3 and tb != 6 and "Bucket" in items[0]:
                if tb == 1:
                    T = "You reach for the handle. As you clasp the cold metal, you realise too late that it is razor-sharp. As you pull you hand away the handle opens a small cut on your hand. The blood drips into the bucket and vanishes. The cut magically heals."
                elif tb == 2:
                    T = "No way you’re touching that again."
                elif tb == 3:
                    T = "Seriously, don’t do it."
                elif tb == 4:
                    T = "Having tasted blood, the bucket is hungry. It pounces, making straight for your face with it’s now razor-sharp handle and splinter riddled planks. You duck just in time and the scary receptacle smashes itself to pieces on the wall behind you. \nYou: 1 Blood Sucking Bucket: 0."
                elif tb == 5:
                    T = "You pick up a small shard of the smashed bucket off the floor and notice writing engraved on the back. In small round letters it reads 'Do Not Feed'. You quickly expell air through your nose in amusement and carefully place the shard in your back left pocket. *Shard added to inventory*."
                    inventory.append("Bucket-Shard")
                    items[0].remove("Bucket")
                text(T, speed, 0)
                tb += 1

            else:
                if act[1] in items or act[1] == "Bucket":
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

        elif act[0] == "Use":
            if act[1] == "Axe" and l<3 and "Axe" in inventory:
                text("Don't even think about using that on yourself.", speed, 0)
            elif "Axe" in inventory and act[1] == "Axe" and act[2] == "With" and act[3] == "Door" and l<5:
                text("Mustering all of your strength, you swing the axe as violently as you can towards the door, hoping that all of the shows you ever watched in which people hack their way through doors with an axe were truthful, and it really was as easy as it looked.\nThe axe thunks pleasingly into the thick wood of the door, but does little damage.\nYou try again, swinging the dangerous weapon as deftly as you can.\nYour natural ineptness means that you miss the door entirely. Luckily, however, the axe slams into the padlock and it explodes into a cloud of metal shards.\nThe axe, its purpose fulfilled, disappears in a puff of orange smoke that dissipates quickly.", speed, 0)
                inventory.remove("Axe")
                items[0].remove("Lock")
                axe = 0
                Open = 1
            elif "Bottle" in inventory and act[1] == "Bottle" and act[2] == "With" and act[3] == "Door" and l<5:
                text("Due to your unrivaled stupidity you think it is a good idea to surprise attack the locked door with a fragile glass bottle.\nYou stand in a fighting pose before spinning around on one leg and hitting the door with the bottle as if it was some kind of weapon.\nIt smashes. You moron. You have made a mess. Well done, have ten points.", speed, 0)
                inventory.remove("Bottle")
            elif "Key" in inventory and act[1] == "Key" and act[2] == "With" and act[3] == "Door" or act[3] == "Lock" and l<5:
                text("You take the key out of your pocket and hold it up to the lock on the door. There is a rather large size difference, this key is obviously not for this lock. however, you and your two brain cells decide to give it a try anyway. you push the key into the lock as hard as you can denting the door in the process. Are you really surprised it didn't work.", speed, 0)

            else:
                if act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

        elif act[0] == "R" or act[0] == "Right" and l<2:
            Room2(Open, descriptions, unlocked, lb, tb, cabinet)


        elif act[0] == "Inventory" and l<2:
            invent()


        elif act[0] == "U" or act[0] == "Up" and l<2:
            Room3(Open, descriptions, unlocked, lb, tb, cabinet)

        elif act[0] == "L" or act[0] == "Left":
            Room4(Open, descriptions, unlocked, lb, tb, cabinet)

        elif act[0] == "D" or act[0] == "Down":
            Room5(Open, descriptions, unlocked, lb, tb, cabinet)

        else:
            if l<2:
                text(error, speed, 0)
            elif act[1] in items or inventory:
                text(no, speed, 0)
            else:
                text(error, speed, 0)

def Room2(Open, descriptions, unlocked, lb, tb, cabinet):

    if "2" in DesSp:
        DesSpeed = descriptions
    else:
        DesSpeed = 1
    speed = descriptions
    room2 = 0
    if "Key" not in inventory:
        description = "This room is similar to the room you started in. The walls and floor are the same. The ceiling looks identical.\nIn the centre of the room is a large wooden table with a small gold key sitting on it. There wasn’t one of those is the first room. So, that counts as a difference, I guess.\nThe room you just left is to your…er…left."  
    else:
        description = "This room is similar to the room you started in. The walls and floor are the same. The ceiling looks identical.\nIn the centre of the room is a large wooden table. There wasn’t one of those is the first room. So, that counts as a difference, I guess.\nThe room you just left is to your..er…left……… …"

    text(description, DesSpeed, 0)
    
    if "2" in DesSp:
        DesSp.remove("2")
    
    while room2 == 0:
        print(end="\n")
        action = input(">>> ")
        action = action.title()
        act = action.split()
        l = len(act)

        if l == 0:
            room2 = 0

        elif act[0] == "Look":
            if act[1] == "Table" and l<3:
                text("It’s a large, crudely built, but sturdy looking wooden table. The surface was, you assume, originally polished to a high shine, but years of use for, no doubt dubious, activities has dulled the surface. The plethora of scarlet coloured stains that adorn the table suggest that it was used for activities that you’d rather not think about, but probably involved a persons’ insides becoming their outsides.", speed, 0)
            elif act[1] == "Key" and l<3:
                text("It’s a small metal key. It looks like it was originally brass coloured, but it’s so old that the wear on it has given it a darker colour.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

        elif act[0] == "Take":
            if act[1] == "Table" and l<3:
                text("Despite being a fantastic specimen of a human, lifting heavy wooden tables is beyond even your capabilities. Besides, it wouldn’t fit in your pocket.", speed, 0)
            elif act[1] == "Key" and "Key" not in inventory and l<3:
                text("You take the key and put it in your pocket.", speed, 0)
                inventory.append("Key")
                items[1].remove("Key")
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

        elif act[0] == "Left" or act[0] == "L" and l<2:
            Room1(Open, descriptions, unlocked, lb, tb, cabinet)


        elif act[0] == "Inventory" and l<2:
            invent()

            
        else:
            if l<2:
                text(error, speed, 0)
            elif act[1] in items or inventory:
                text(no, speed, 0)
            else:
                text(error, speed, 0)





def Room3(Open, descriptions, unlocked, lb, tb, cabinet):

    if "3" in DesSp:
        DesSpeed = descriptions
    else:
        DesSpeed = 1
    speed = descriptions
    room3 = 0
    description = "You climb the ladder and enter the hole in the ceiling. After taking a moment to thank a god you don’t believe in that nothing with horrendously sharp teeth made your head and ex-head as it poked its way into the room, you take a moment to survey your surroundings. They are dull and uninteresting.\nA large-ish, plain metal cabinet stands in the corner of the room. Behind you, a hole in the floor leads back into the first room."
    text(description, DesSpeed, 0)
    if "3" in DesSp:
        DesSp.remove("3")
    
    while room3 == 0:
        print(end="\n")
        action = input(">>> ")
        action = action.title()
        act = action.split()
        l = len(act)

        if l == 0:
            room3 = 0
            

        elif act[0] == "Open":
            if act[1] == "Cabinet" and unlocked == 1 and l<3 and cabinet == 0:
                text("You pull the freshly unlocked door. It swings open with an ear-splitting squeak, like a dolphin on helium. Inside the cabinet is a scary looking axe.",speed, 0)
                cabinet = 1
            elif act[1] == "Cabinet" and unlocked == 0 and l<3:
                text("You try the door, it doesn’t move. The door is probably locked. Maybe something key shaped would help unlock it.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)
                    
                    
        elif act[0] == "Look":
            if unlocked == 1 and act[1] == "Axe" and l<3:
                text("It’s an incredibly scary and sharp looking axe. The type that burly lumberjack types might use to chop down trees, or burly firefighters might use to breaks down doors. Or burly…ahem…it’s an axe.", speed, 0)
            elif act[1] == "Keyhole" and l<3:
                text("It’s a hole. For a key. A ‘key hole’ if you will.", speed, 0)
            elif act[1] == "Hole" and l<3:
                text("It’s the hole you just climbed through. Not the brightest crayon in the bag are you.", speed, 0)
            elif act[1] == "Cabinet" and unlocked == 0 and l<3:
                text("The cabinet is grey, about 4 feet high, has 4 straight, metal legs, and has a door in the centre of it. It looks to have been designed for one purpose and one purpose only: to hold something of incredible importance. Probably something you could use to escape. The door has a keyhole in it.", speed, 0)
            elif act[1] == "Cabinet" and unlocked == 1 and l<3:
                text("It’s the same cabinet but now the door is open. Remember how you unlocked it with the key not so long ago? Yeah, well that can’t unhappen.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)
                    

        elif act[0] == "Take":
            if act[1] == "Cabinet" and l<3:
                text("It’s a cabinet. You don’t just take cabinets. They’re for cabinet-ing.", speed, 0)
            elif act[1] == "Axe" and l<3 and unlocked == 1 and "Axe" not in inventory:
                text("You take the axe and try and put it in your pocket. It obviously doesn’t fit because it’s an axe and not a packet of mints. You decide to carry it instead. It makes you feel important.", speed, 0)
                inventory.append("Axe")
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)
                    

        elif act[0] == "Use":
            if l<3:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)
            elif act[1] == "Key"and l<5 and act[2] == "With" and act[3] == "Cabinet" and "Key" in inventory and unlocked == 0:
                text("You insert the key into the keyhole. Nothing happens. You take a chance and turn the key to see if that does anything. Surprisingly, the lock clicks as though turning the key was…er…the key to unlocking the…er…lock.", speed, 0)
                unlocked = 1
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items or inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)
                    

        elif act[0] == "D" or act[0] == "Down":
            Room1(Open, descriptions, unlocked, lb, tb, cabinet)
            

        elif act[0] == "Inventory" and l<2:
            invent()
            

        else:
            if l<2:
                text(error, speed, 0)
            elif act[1] in items[2]:
                text(no, speed, 0)
            else:
                text(error, speed, 0)


def Room4(Open, descriptions, unlocked, lb, tb, cabinet):

    if "4" in DesSp:
        DesSpeed = descriptions
    else:
        DesSpeed = 1
    speed = descriptions
    room4 = 0
    description = "This room is entirely uninteresting. It’s grey, has wooden bits, and the door you just entered by is to your right. That’s it.\nOh, there is a window, though, if that counts as interesting."
    text(description, DesSpeed, 0)
    if "4" in DesSp:
        DesSp.remove("4")
    
    while room4 == 0:
        print(end="\n")
        action = input(">>> ")
        action = action.title()
        act = action.split()
        l = len(act)

        if l == 0:
            room4 = 0

        elif act[0] == "Open" and l<3:
            if act[1] == "Window" and l<3:
                text("It doesn't open.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items and inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

                
        elif act[0] == "Look" and l<4:
            if act[1] == "Window" and l<3:
                text("Given the strange, otherworldly events that took place to bring you here, and the odd, mysteriousness of the building you’re stuck in, you expect to see mystical, fantasy scenes through the window.\nInstead you see and empty car park.", speed, 0)
            elif act[1] == "Carpark" and l<3:
                text("It’s flat, grey, and uninteresting. Like something that isn’t very interesting coloured grey.", speed, 0)
            elif act[1] == "Car" and act[2] == "Park" and l<4:
                text("It’s flat, grey, and uninteresting. Like something that isn’t very interesting coloured grey.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items and inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)
            
        elif act[0] == "Take" and l<3:
            if act[1] == "Window":
                text("Are you a bit challenged? It’s a window. If you take it, what will you look out of?.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items and inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

            
        elif act[0] == "Inventory" and l<3:
            invent()

            
        elif act[0] == "R" or act[0] == "Right" and l<3:
            Room1(Open, descriptions, unlocked, lb, tb, cabinet)

            
        else:
            if l<2:
                text(error, speed, 0)
            elif act[1] in items and inventory:
                text(no, speed, 0)
            else:
                text(error, speed, 0)


def Room5(Open, descriptions, unlocked, lb, tb, cabinet):

    if "5" in DesSp:
        DesSpeed = descriptions
    else:
        DesSpeed = 1
    room5 = 0
    description = "Descending the steps slowly and carefully, you emerge into a darkened room. You can see very little except a bottle on the floor. The stairs behind you ascend you the much less dark, and much less scary first room."
    text(description, DesSpeed, 0)
    if "5" in DesSp:
        DesSp.remove("5")
    
    while room5 == 0:
        print(end="\n")
        action = input(">>> ")
        action = action.title()
        act = action.split()
        l = len(act)

        if l == 0:
            room4 = 0


        elif act[0] == "Look":
            if act[1] == "Bottle" and l<3:
                text("It’s a green, glass bottle that looks like it was once used to hold wine. Sadly, there is no wine in there now.", speed, 0)
            elif act[1] == "Dark" and l<3:
                text("You can’t see anything. It’s dark. That’s why they call it dark and not ‘Super Brightness, the Seeing Stuff’.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items and inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

                
        elif act[0] == "Take":
            if act[1] == "Bottle" and l<3:
                text("You pick up the bottle and place it easily in your astonishingly capacious pocket.", speed, 0)
                inventory.append("Bottle")
            elif act[1] == "Dark" and l<3:
                text("What an odd request. OK, well, you try to take the dark and are shocked to discover that it works. The room suddenly becomes much brighter. You put the dark in your pocket. However, upon closer inspection, you realise that the room was much more interesting with the dark in it so you put it back.", speed, 0)
            else:
                if l<2:
                    text(error, speed, 0)
                elif act[1] in items and inventory:
                    text(no, speed, 0)
                else:
                    text(error, speed, 0)

            
        elif act[0] == "Inventory":
            invent()

            
        elif act[0] == "U" or act[0] == "Up":
            Room1(Open, descriptions, unlocked, lb, tb, cabinet)

            
        else:
            if l<2:
                text(error, speed, 0)
            elif act[1] in items and inventory:
                text(no, speed, 0)
            else:
                text(error, speed, 0)



        
    
Menu()
