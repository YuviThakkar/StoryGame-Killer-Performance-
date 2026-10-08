fates = {"Erin": "ALIVE", "Ben": "ALIVE", "Ollie": "ALIVE", "Andrew": "ALIVE", "Lune": "ALIVE", "Bob": "Alive"}
reye_died_early = True
juliet_final_words = 0
cassandra_five = 0
hayden_fate = 0

cassandra_hate = 0
hayden_like = 0

collectibles = 0

mom_text = False
rowe = ""
roe = ""
kid_looked = "none"
sleep = True
cbunk = False
timeslot = "a"
fin = 0
outside = True
bracelet = 0
loca = "a"

area_one_one = True
area_one_two = True
area_one_three = True
area_one_four = True
area_one_five = True
area_one_six = True
area_one_seven = True
area_one_eight = True
area_one_nine = True
area_one_key = False

area_two_one = True
area_two_two = True
area_two_three = True
area_two_four = True
area_two_five = True
area_two_six = True

area_three_one = True
area_three_two = True
area_three_three = True

area_four_one = True
area_four_two = True
area_four_three = True
area_four_four = True
area_four_five = True
area_four_six = True
area_four_seven = True

area_five_one = True
area_five_two = True
area_five_three = True
area_five_four = True
area_five_five = True
area_five_six = True
area_five_seven = True

area_six_one = True
area_six_two = True
area_six_three = True
area_six_four = True
area_six_five = True

final_area_one = True
final_area_two = True
final_area_three = True
final_area_four = True

def open_message():
    print("\n Welcome to the Killer Performance game.")
    start = input("\n Type 'start' to start: ")
    if start.lower() == "start":
        game()
    else:
        print("\n That is not a valid option for this prompt. The same message will now be repeated.")
        open_message()
        
def cassandra_bus():
    global juliet_final_words
    global collectibles
    global roe
    print("\n After getting kicked out of the 4th row by Cassandra, you realize that you luckily still have 19 other options.")
    print("\n Where do you go now?")
    ro = input("\n Once again, type a number 1-20 for the corresponding row, except for 4 since you have been kicked out of there: ")
    if ro == "1" or ro == "2" or ro == "5" or ro == "6" or ro == "8" or ro == "10" or ro == "12" or ro == "13" or ro == "14" or ro == "15" or ro == "16" or ro == "18" or ro == "19":
        print("")
        print(f" You walk over to row {ro}, and see no one sitting there. You sit down, alone by a window as you watch the bus begin to drive.")
    elif ro == "9":
        print("\n You go to the 9th row of the bus, and find no one sitting there. However, on one of the seats, you see a teddy bear.")
        print("\n Congratulations: you have found a Collectible item. You pick the teddy bear up and keep it in your pocket.")
        print("\n After you pick up the teddy bear, you look over at the window and watch as the bus begins driving.")
        collectibles += 1
    elif ro == "3":
        print("\n You go to the 3rd row and see a boy sitting there, looking down at a Nintendo Switch. His name is Ollie.")
        print('\n "Hey there," you say.')
        print('\n "Oh, hi," he replies nervously, looking up from his Switch and then looking right back down at it.')
        print("\n You sit next to Ollie as the bus begins driving.")
    elif ro == "4":
        print("\n You cannot go to the 4th row without losing your life. The prompt will now be repeated.")
        cassandra_bus()
    elif ro == "7":
        print("\n You head over to the seventh row, the lucky number! There, you see a girl sitting.")
        print('\n "Oh, hi! My name is Reye. What is yours!?" the girl says enthusiastically.')
        print('\n "Hey, my name is Erin," you tell Reye.')
        print('\n "Nice to meet you, Erin! What is your favorite color?!" Reye then asks.')
        print('\n "Uhm... Blue?" you reply.')
        print("\n Reye keeps on talking to you until you eventually zone out once the bus begins driving.")
    elif ro == "11":
        print("\n You walk over to the 11th row and see a girl sitting there.")
        print('\n "Oh, hey, I am Juliet," she says nervously.')
        print('\n "Hi, I am Erin," you reply.')
        print("\n You sit down next to Juliet as the bus begins driving.")
        juliet_final_words += 1
    elif ro == "17":
        print("\n You walk over to the 17th row and see a tall guy sitting there with headphones on. His name is Ben.")
        print('\n "Hi," you say, realizing he is kind of a handsome fella.')
        print("\n Ben then nods at you like how those cool teenage boys say hi and looks back at the window.")
        print("\n You then sit down next to him as the bus begins driving.")
    elif ro == "20":
        print("\n You go to the very last row and see a guy with an necklace sitting there.")
        print('\n "Oh, hello there, my name is Andrew," he says.')
        print('\n "Hi, I am Erin," you say after.')
        print("\n You sit next to Andrew as the bus begins driving.")
        roe = "20"
    else:
        print("\n That is not a valid response. The prompt will now be repeated.")
        cassandra_bus()
    
        
def bus():
    global juliet_final_words
    global cassandra_hate
    global collectibles
    global rowe
    print("")
    print(" You, 17 year old girl Erin steps onto the bus, heading to Camp Cottonwood. You have always loved theater, and once you were accepted into Camp Cottonwood, you knew it was just the perfect shot. Camp Cottonwood is renowned for producing Broadway and West End stars, and hearing this made you apply.")
    print("\n On the bus, you see 20 rows to sit in, some of them having kids and some of them not. Which row do you sit in?")
    row = input("\n Type a number 1-20 for the corresponding row: ")
    if row == "1" or row == "2" or row == "5" or row == "6" or row == "8" or row == "10" or row == "12" or row == "13" or row == "14" or row == "15" or row == "16" or row == "18" or row == "19":
        print("")
        print(f" You walk over to row {row}, and see no one sitting there. You sit down, alone by a window as you watch the bus begin to drive.")
    elif row == "9":
        collectibles += 1
        print("\n You go to the 9th row of the bus, and find no one sitting there. However, on one of the seats, you see a teddy bear.")
        print("\n Congratulations: you have found a Collectible item. You pick the teddy bear up and keep it in your pocket.")
        print("\n After you pick up the teddy bear, you look over at the window and watch as the bus begins driving.")
    elif row == "3":
        print("\n You go to the 3rd row and see a boy sitting there, looking down at a Nintendo Switch. His name is Ollie.")
        print('\n "Hey there," you say.')
        print('\n "Oh, hi," he replies nervously, looking up from his Switch and then looking right back down at it.')
        print("\n You sit next to Ollie as the bus begins driving.")
    elif row == "4":
        print("\n You go to the 4th row of the bus and see a girl sitting there, looking at a picture of a lambo with her shiny new iPhone. Her name is Cassandra.")
        print('\n "Uhm, excuse me??? What are you doing here?!" Cassandra says.')
        print("\n You stand there frozen, not knowing what to say.")
        print('\n "You think you can sit next to me? ME???? GET OUT!" Cassandra screams in a whiny tone.')
        cassandra_hate += 1
        cassandra_bus()
        rowe = "4"
    elif row == "7":
        print("\n You head over to the seventh row, the lucky number! There, you see a girl sitting.")
        print('\n "Oh, hi! My name is Reye. What is yours!?" the girl says enthusiastically.')
        print('\n "Hey, my name is Erin," you tell Reye.')
        print('\n "Nice to meet you, Erin! What is your favorite color?!" Reye then asks.')
        print('\n "Uhm... Blue?" you reply.')
        print("\n Reye keeps on talking to you until you eventually zone out once the bus begins driving.")
    elif row == "11":
        print("\n You walk over to the 11th row and see a girl sitting there.")
        print('\n "Oh, hey, I am Juliet," she says nervously.')
        print('\n "Hi, I am Erin," you reply.')
        print("\n You sit down next to Juliet as the bus begins driving.")
        juliet_final_words += 1
    elif row == "17":
        print("\n You walk over to the 17th row and see a tall guy sitting there with headphones on. His name is Ben.")
        print('\n "Hi," you say, realizing he is kind of a handsome fella.')
        print("\n Ben then nods at you like how those cool teenage boys say hi and looks back at the window.")
        print("\n You then sit down next to him as the bus begins driving.")
    elif row == "20":
        rowe = "20"
        print("\n You go to the very last row and see a guy with a necklace sitting there.")
        print('\n "Oh, hello there, my name is Andrew," he says.')
        print('\n "Hi, I am Erin," you say after.')
        print("\n You sit next to Andrew as the bus begins driving.")
    else:
        print("\n That is not a valid response. The prompt will now be repeated.")
        bus()
        

def review():
    global kid_looked
    if mom_text:
        print("\n You step onto the camp grounds after replying to the text your mother sent and then getting screamed at by the bus driver. You have officially reached Camp Cottonwood!")
    else:
        print("\n You step onto the camp grounds after ignoring the text your mother sent. You have officially reached Camp Cottonwood!")
    if rowe == "4" and roe == "20":
        print("\n As you walk through the grounds of Camp Cottonwood, you see three kids ahead of you. Two of them you recognize, the first being Cassandra, and the second being Andrew.")
        print("\n The third, however, you do not recognize. They seem to have been here the longer than you, Cassandra, or Andrew.")
        print("\n Who do you want to analyze? ")
        print("\n a) Cassandra")
        print(" b) Andrew")
        print(" c) The third kid")
        print(" d) None of them")
        rev = input("\n Type either 'a', 'b', 'c', or 'd': ")
    elif rowe == "4" and roe != "20":
        print("\n As you walk through the grounds of Camp Cottonwood, you see three kids ahead of you. The first you recognize, and it is Cassandra. The other two, however, you do not recognize.")
        print("\n The second kid is currently playing with his necklace. The third kid looks as if they had been there for much longer than you, Cassandra, or the second kid.")
        print("\n Who do you want to analyze? ")
        print("\n a) Cassandra")
        print(" b) The second kid")
        print(" c) The third kid")
        print(" d) None of them")
        rev = input("\n Type either 'a', 'b', 'c', or 'd': ")
    elif rowe == "20":
        print("\n As you walk through the grounds of Camp Cottonwood, you see three kids ahead of you. The first one looks quite full of herself, walking around with her shiny iPhone. The second you recognize, Andrew.")
        print("\n Similar to the first kid, you do not recognize the third. They look like they have been here for a lot longer than you, Andrew or the first kid.")
        print("\n Who do you want to analyze? ")
        print("\n a) The first kid")
        print(" b) Andrew")
        print(" c) The third kid")
        print(" d) None of them")
        rev = input("\n Type either 'a', 'b', 'c', or 'd': ")
    else:
        print("\n As you walk through the grounds of Camp Cottonwood, you see three kids ahead of you, all of them being kids you have never met before.")
        print("\n The first one looks quite full of herself, walking around with her shiny iPhone, while the second kid is currently playing with his necklace. Finally, the third kid looks like have they had been here for much longer than you or the other two kids.")
        print("\n Who do you want to analyze?")
        print("\n a) The first kid")
        print(" b) The second kid")
        print(" c) The third kid")
        print(" d) None of them")
        rev = input("\n Type either 'a', 'b', 'c', or 'd': ")
    if rev == "a":
        kid_looked = "Cassandra"
        if rowe == "4":
            print("\n You analyze Cassandra, the girl you tried to sit next to on the bus and rudely kicked you out. Her last name is Ward, and she looks extremely sassy and full of herself while taking selfies of herself and posting them on Instagram. She was only on the bus because her father forced her to go on it just once instead of being escorted to Camp Cottonwood through a private lambo like in previous years.")
        else:
            print("\n You analyze the first kid, named Cassandra Ward. Although you weren't next to her on the bus, she was unhappily there, as her dad told her to go on the bus for once instead of being taken around in a private lambo. You watch as she takes a selfie of herself with her shiny phone and posts it on Instagram.")
    elif rev == "b":
        kid_looked = "Andrew"
        if rowe == "20":
            print("\n You analyze Andrew, the guy you sat with on the bus. His last name is Lorn, and he is currently playing with the same necklace you saw him wearing on the bus. He’s much taller standing tall and likes to go to theater camp to get away from the troubles of school and life. He finds it funny that he is only himself when he’s not himself.")
        elif rowe == "4" and roe == "20":
            print("\n You analyze Andrew, the kid you sat with on the bus after getting kicked off the 4th row by Cassandra. His last name is Lorn, and he is currently playing with the same necklace you saw him wearing on the bus. He’s much taller standing tall and likes to go to theater camp to get away from the troubles of school and life. He finds it funny that he is only himself when he’s not himself")
        else:
            print("\n You analyze the second kid, named Andrew Lorn. Although you didn’t sit with him, he has the very back of the bus playing with his necklace, as he’s doing currently. He’s also quite tall and likes to go to theater camp to get away from the troubles of school and life. He finds it funny that he is only himself when he’s not himself.")
    elif rev == "c":
        kid_looked = "Hayden"
        print("\n You analyze the third kid, named Hayden. Their full name is Hayden Martin, and they do tech (things like lights) for the shows at Camp Cottonwood, and prefer back-stage roles. Their parents own Camp Cottonwood, which is why they look like they have been here longer than everyone, because they live on campus.")
    elif rev == "d":
        print("\n You choose to not analyze any of the kids.")
    else:
        print("That is not a valid keyword. Please type either the letter a, b, c, or d. The prompt will now be repeated.")
        
def mommy():
    print("\n You stay on the bus for one more moment and open up the text your mom sent. It says 'I hope you have fun honey!'. How do you reply?")
    print("\n a) Text 'I will!'")
    print(" b) Text 'I will not' with a laughing emoji")
    print(" c) Text 'Thank you!'")
    print(" d) Heart her text")
    reply = input("\n Type either 'a', 'b', 'c', or 'd': ")
    if reply == "a":
        print("\n You text your mom 'I will!' as you notice the bus driver stand up.")
        print('\n "HEY! YOU PLAN ON LEAVING ANYTIME SOON?!" he screams.')
        print("\n You then shuffle off the bus in fear.")
        review()
    elif reply == "b":
        print("\n You text your mom 'I will not' and add a laughing emoji at the end as you notice the bus driver stand up.")
        print('\n "HEY! YOU PLAN ON LEAVING ANYTIME SOON?!" he screams.')
        print("\n You then shuffle off the bus in fear.")
        review()
    elif reply == "c":
        print("\n You text your mom 'Thank you!' as you notice the bus driver stand up.")
        print("\n You text your mom 'I will not' and add a laughing emoji at the end as you notice the bus driver stand up.")
        print('\n "HEY! YOU PLAN ON LEAVING ANYTIME SOON?!" he screams.')
        print("\n You then shuffle off the bus in fear.")
        review()
    elif reply == "d":
        print("\n You heart the text that your mom sent as you notice the bus driver stand up.")
        print("\n You text your mom 'I will not' and add a laughing emoji at the end as you notice the bus driver stand up.")
        print('\n "HEY! YOU PLAN ON LEAVING ANYTIME SOON?!" he screams.')
        print("\n You then shuffle off the bus in fear.")
        review()
    elif reply == "#6767420gummywormsforlifelolxd":
        print("\n Unless you looked at the code or found all 7 collectibles on a seperate playthrough, the mathematical chance you came across this easter egg is just insane. To reward you, the killer is Andrew. Anyways, you typed an invalid keyword, so the prompt will now be repeated.")
        mommy()
    else:
        print("\n That is not a valid keyword for this decision. The same prompt will now be repeated.")
        mommy()
        
def text():
    global mom_text
    print("\n After some time, the bus eventually reaches Camp Cottonwood and stops. Everyone gets up, excited, except for you. You see that you received a text from your mom. What do you do?")
    print("\n a) Stay seated to open the text")
    print(" b) Ignore it and get off the bus")
    message = input("\n Type 'a' or 'b' for the corresponding decision: ")
    if message == "a":
        mom_text = True
        mommy()
    elif message == "b":
        review()
    else:
        print("That is not 'a' or 'b'. The same prompt will now be repeated.")
        text()
        
def recep():
    global area_one_key
    print("\n You enter the receptionist office and see a girl waiting by the counter.")
    print('\n "Oh, hi, I am Lune, the receptionist. Are you here to check in?" the girl says.')
    print('\n "Yes, mam," you reply.')
    print('\n "Alright then. What is your full name?"')
    print('\n "Erin Jaquevius," you say.')
    print("\n Lune then types something into her computer.")
    print('\n "Okay, here is your key. The girls cabin is nearby," Lune says, handing you a key.')
    print('\n "Thanks," you reply, taking it.')
    print("\n You then leave the receptionist office and step outside.")
    area_one_key = True
    
    
def area_camp():
    global collectibles
    global area_one_one
    global area_one_two
    global area_one_three
    global area_one_four
    global area_one_five
    global area_one_six
    global area_one_seven
    global area_one_eight
    global area_one_nine
    global area_one_key
    if kid_looked == "none":
        print("\n You continue walking throughout the grounds of Camp Cottonwood, now heading over to the girls cabin, where you are supposed to stay. But you realize you have to check in at the receptionist office and get the key first.")
    else:
        print(f"\n After analyzing {kid_looked}, you decide to head over to the girls cabin, where you are supposed to stay. But you realize you have to check in at the receptionist office and get the key first.")
    print("\n You see a bunch of buildings everywhere. However, you do not know which one is the receptionist office.")
    print("\n Below is the list of places in the area you can check. Find the receptionist office and get the key to your cabin.")
    while True:
        print("")
        if area_one_one:
            print(" 1) The massive building directly in front of you")
        if area_one_two:
            print(" 2) The small building with a red plus on it to the left of the massive one")
        if area_one_three:
            print(" 3) The small building to the right of the massive one")
        if area_one_four:
            print(" 4) The first of the two medium sized buildings up ahead")
        if area_one_five:
            print(" 5) The second of the two medium sized buildings up ahead")
        if not area_one_five:
            print(" 5) The girls cabin")
        if area_one_six:
            print(" 6) The machine outside of the massive building")
        if area_one_seven:
            print(" 7) The somewhat large building near some trees")
        if area_one_eight:
            print(" 8) The trees around the camp")
        if area_one_nine:
            print(" 9) The cliff in the distance")
        aone = input("\n Type a number 1-9 for the corresponding place to check: ")
        if aone == "1":
            if not area_one_key:
                if area_one_one:
                    print("\n You walk over to the massive building in front of you. In front, there is a sign that says:")
                    print("\n 'THE THEATER'")
                    print('\n "So it is not the receptionist office then..." you think.')
                else:
                    print("\n You have already checked the theater. The receptionist office is not there.")
                area_one_one = False
            else:
                if area_one_one:
                    print("\n You go to the massive building, and from a sign you learn it is the theater.")
                else:
                    print("\n You have already been here.")
                area_one_one = False
        elif aone == "2":
            if not area_one_key:
                if area_one_two:
                    print("\n You make your way over to the building with a red plus on it. Turns out, it's the nurse's office.")
                    print("\n It makes sense, considering that usually if it has a big red plus on it it is medical-related.")
                else:
                    print("\n You have already checked the nurse's office. It isn't the receptionist office.")
                area_one_two = False
            else:
                if area_one_two:
                    print("\n You walk over to the building with a red plus on it and learn it's the nurse's office, hence why there was a red plus on it.")
                else:
                    print("\n You have already been here.")
        elif aone == "5":
            if not area_one_key:
                if area_one_five:
                    print("\n You go to the second of the medium-sized buildings in the distance. You see a note on it that reads: ")
                    print("\n 'GIRLS CABIN: Cassandra, Juliet, Reye, Erin'")
                    print("\n It is not the receptionist, but at least you now know where the girls cabin is.")
                else:
                    print("\n You cannot enter the girls cabin without a key, which is why you still need to go to the receptionist office and check in.")
                area_one_five = False
            else:
                if area_one_five:
                    print("\n You walk over to the second of the two medium-sized buildings. On it, you see a sign that reads: ")
                    print("\n 'GIRLS CABIN: Cassandra, Juliet, Reye, Erin'")
                    print("\n This is it! Using the key, you unlock the door and go inside.")
                    break
                else:
                    print("\n You walk back over to the girls cabin.")
                    print("\n You open the door using the key and go inside.")
                    break
        elif aone == "4":
            if not area_one_key:
                if area_one_four and area_one_five:
                    print("\n You go to the first of the two medium-sized buildings further ahead. You see a note on it that reads: ")
                    print("\n 'BOYS CABIN: Andrew, Ben, Ollie'")
                    print("\n It is not the receptionist office, but this means the girls cabin must be close...")
                elif area_one_four and not area_one_five:
                    print("\n You go to the other medium-sized building. You see a note on it that reads: ")
                    print("\n 'BOYS CABIN: Andrew, Ben, Ollie'")
                    print("\n It makes sense, seeing as the girls cabin is right next door. But it is sadly still not the receptionist office.")
                else:
                    print("\n You have already checked here. It is not the receptionist office.")
                area_one_four = False
            else:
                if area_one_four:
                    print("\n You walk over to the first of the medium-sized buildings, and see a note on it that reads:")
                    print("\n 'Andrew, Ben, Ollie'")
                else:
                    print("\n You have already been here.")
                area_one_four = False
        elif aone == "3":
            if not area_one_key:
                if area_one_three:
                    print("\n You go to the small building to the right of the massive one. Near it, there is a sign that reads: ")
                    print("\n 'Receptionist Office: Check in here'")
                    print("\n Congratulations: you have found the receptionist office.")
                    recep()
                    if not area_one_five:
                        print("\n Now that you have the key, go back to the girls cabin.")
                    else:
                        print("\n Now that you have the key, find the girls cabin.")
                else:
                    print("\n You have already been here. Now go to the girls cabin.")
                area_one_three = False
            else:
                print("You have already been here and gotten the key.")
        elif aone == "6":
            if not area_one_key:
                if area_one_six:
                    if area_one_one:
                        print("\n You check the machine outside of the massive building. It seems to just be a vending machine.")
                    else:
                        print("\n You check the machine outside of the theater. It seems to just be a vending machine.")
                else:
                    print("\n You have already checked the vending machine. There is no receptionist office inside.")
                area_one_six = False
            else:
                if area_one_six:
                    print("\n You walk over to the machine you see. Turns out, it is a vending machine.")
                else:
                    print("\n You have already been here.")
                area_one_six = False
        elif aone == "7":
            if not area_one_key:
                if area_one_seven:
                    print("\n You look over at the building near a couple trees. It is a house.")
                    if kid_looked == "Hayden":
                        print("\n It could be the house Hayden and their parents live in since you know they live on campus, but it is definitely not the receptionist office.")
                    else:
                        print("\n Since it is just a house, it cannot be the receptionist office.")
                else:
                    print("\n You have already checked here. It is not the receptionist office.")
                area_one_seven = False
            else:
                if area_one_seven:
                    if kid_looked == "Hayden":
                        print("\n You look over at the building you see near some trees and see it is a house. It could be where Hayden and their parents live, since you know they live on campus.")
                    else:
                        print("\n You look over at the building you see near some trees. It is just a house. You do not know who lives inside.")
                else:
                    print("You have already looked here.")
                area_one_seven = False
                pass
        elif aone == "8":
            if not area_one_key:
                if area_one_eight:
                    collectibles += 1
                    print("\n You walk over to the trees nearby. From what you can see, there are no signs of buildings in the forest.")
                    print("\n However, you do find a crow stuffed animal on the ground.")
                    print("\n Congratulations: you have found a Collectible item. You keep the crow stuffed animal in your pocket.")
                else:
                    print("\n You have already looked at the trees. There are no buildings in the forest from what you can see, and therefore no receptionist office.")
                area_one_eight = False
            else:
                if area_one_eight:
                    collectibles += 1
                    print("\n You look at the trees nearby. They seem to be just trees.")
                    print("\n However, you find a small crow stuffed animal on the ground.")
                    print("\n Congratulations: you have found a Collectible item. You keep the crow stuffed animal in your pocket.")
                else:
                    print("\n You have already looked here.")
                area_one_eight = False
        elif aone == "9":
            if not area_one_key:
                if area_one_nine:
                    print("\n You look over at the cliff in the distance. No way the receptionist office is up there.")
                else:
                    print("\n You have already looked at the cliff. There is no chance the receptionist office is there.")
                area_one_nine = False
            else:
                if area_one_nine:
                    print("\n You look over at the cliff in the distance. Seems like a dangerous place to accidentally fall.")
                else:
                    print("\n You have already looked here.")
                area_one_nine = False
        else:
            print("\n That is not a number from 1 to 9.")
            

def juliet_bunk():
    global juliet_final_words
    global sleep
    if cbunk:
        print("\n After Cassandra screams at you, Juliet walks up to you.")
        print('\n "Hey, uhm, sorry about that. You want to share a bunk with me instead? " she asks.')
        print("\n What do you do?")
        print("\n a) Agree to share a bunk with Juliet")
        print(" b) Sleep on the floor instead")
        juju = input("\n Type 'a' or 'b' for the corresponding action: ")
    else:
        print("\n As you are getting ready to sleep on the floor, Juliet stops you. She offers to let you share a bunk with her.")
        print("\n What do you do?")
        print("\n a) Agree to share a bunk with her")
        print(" b) Still decide to sleep on the floor")
        juju = input("\n Type 'a' or 'b' for the corresponding action: ")
    if juju == "a":
        print("\n You agree to the offer and share a bunk with Juliet. That night, you sleep pretty normally.")
        juliet_final_words += 1
    elif juju == "b":
        print("\n You tell Juliet it is fine and that you will sleep on the floor. That night, you do not get much sleep.")
        sleep = False
    else:
        print("\n That is not a valid option. Please type a valid keyword next time. The prompt will now be repeated.")
        juliet_bunk()
    
    

def bunk():
    global cbunk
    global cassandra_hate
    global juliet_final_words
    global sleep
    print("\n You take off your bag and settle down in the girls cabin for the rest of the day.")
    print("\n A few hours pass, and night eventually falls. You and the 3 other girls, Cassandra, Reye, and Juliet get ready for bed.")
    print("\n After you finish brushing your teeth, you realize there are only 3 bunk beds and each of the other girls have already chosen one.")
    print("\n Who do you share a bunk with?")
    print("\n a) Juliet")
    print(" b) Reye")
    print(" c) Cassandra")
    print(" d) Sleep on the floor")
    share = input("\n Type either 'a', 'b', 'c', or 'd' for the corresponding decision: ")
    if share == "a":
        print("\n You choose to share a bunk with Juliet.")
        print('\n "Oh, sure," she says after you ask her if she is okay with it.')
        print("\n That night, you sleep pretty normally.")
        juliet_final_words += 1
    elif share == "b":
        sleep = False
        print("\n You choose to share a bunk with Reye.")
        print('\n "Alright, great!" Reye enthusiastically says when you ask if she is okay with it.')
        print("\n Reye ends up talking to you for the whole night. You get no sleep.")
    elif share == "c":
        if rowe != "4":
            cbunk = True
            print("\n You choose to share a bunk with Cassandra.")
            print('\n "EXCUSE ME??? WE ARE NOT SHARING A BUNK. I DESERVE MY OWN BUNK BED!" Cassandra yells at you.')
            cassandra_hate += 1
            juliet_bunk()
        else:
            print("\n You choose to share a bunk with Cassandra.")
            print('\n "SO FIRST YOU TRY TO SIT WITH ME ON THE BUS, AND NOW YOU ARE TRYING TO SHARE A BUNK!? WHAT DO YOU NOT UNDERSTAND ABOUT NO!!! Cassandra screams."')
            cassandra_hate += 2
            juliet_bunk()
    elif share == "d":
        print("\n You choose to sleep on the floor.")
        juliet_bunk()
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        bunk()
        
def ori():
    if sleep:
        print("\n The next morning, you wake up well-rested, ready for the important day. You get ready for orientation, where everyone is supposed to meet.")
        print("\n Once you finish getting ready, you head over to the theater, the biggest building in the whole camp. There, you see a bunch of kids and two adults sitting and take a seat.")
        print('\n "Hi everyone, my name is Bob, and I am the stage manager here at Camp Cottonwood." the first adult says.')
        print('\n "And I am Lune, the receptionist. I am pretty sure I have met all of you." the other says.')
        print('\n "First off, let us start by each going around saying our full name and pronouns. Starting with you, young lady," Bob then says, turning to the girl next to him.')
        print('\n "Cassandra Ward, she/her," the first girl says with an extremely annoying tone.')
        print('\n "Andrew Larn, he/him," the boy next to her says after.')
        print('\n "Hayden Martin, they/them," the next says.')
        print('\n "Juliet Samuels, she/her,"')
        print('\n "Reye Taser, she/her,"')
        print('\n "Ben Glost, he/him,"')
        print('\n "Ollie Moore, he/they,"')
        print("\n And before you knew it, it was your turn.")
        print('\n "Erin Jaquevius, she/her," you say nervously.')
    else:
        print("\n The next morning, you wake up exhausted, since you got no sleep. You then make your way over to orientation where everyone is supposed to be.")
        print('\n "HEY! YOU!" you hear a voice scream suddenly.')
        print('\n "Wha- wha, what is going on?!" you say frantically, lifting your head up.')
        print("\n Turns out, you had fallen asleep during the middle of orientation. The stage manager, named Bob, had woken you up.")
        print('\n "Cassandra, Andrew, Hayden, Juliet, Reye, Ben and Ollie have all already gone. What is your full name and pronouns?" Bob then asks.')
        print("\n Everyone around you except Bob are visibly trying their hardest not to laugh, but are failing miserably.")
        print('\n "Oh, my name is Erin Jaquevius and my pronouns are she/her," you say, yawning.')
    print('\n "Great, we have finally finished the boring part. The musical that Camp Cottonwood will be putting on this year is Heathers." Bob then says.')
    print("\n You hear chatters as people around you are whispering and celebrating.")
    print('\n "I am sure many of you know about it, and that some of you do not. If you have never heard of Heathers, I suggest you use a tool called Google. But I will tell you that the lead female role is Veronica, and the lead male role is Jason Dean."')
    print("\n Eventually, orientation finishes up. The last thing Bob says is that auditions for the show are today.")
    
def h_agree():
    global hayden_like
    print("\n After Cassandra storms off, Hayden walks up to you.")
    print('\n "Hey, thanks for backing me up there, but there is something you should know..." Hayden says.')
    print('\n "Oh, what is it?" you ask.')
    print('\n "I actually... Was the one who switched her cabin." Hayden admits.')
    print("\n What do you say?")
    print('\n a) "Makes sense, she is so annoying,"')
    print(' b) "Why would you do that!?!"')
    print(' c) "Oh, well, okay then,"')
    print(' d) "Whatever you think is best, I suppose,"')
    h = input("\n Type either 'a', 'b', 'c', or 'd' to pick what to say: ")
    if h == "a":
        hayden_like += 1
        print('\n "Makes sense, she is so annoying," you tell Hayden.')
        print('\n "RIGHT!?! Thanks for agreeing with me," Hayden replies.')
        print("\n You both then leave the theater.")
    elif h == "b":
        hayden_like -= 1
        print('\n "Why would you do that!?!" you ask Hayden angirly.')
        print('\n "She deserved it! She is just a whiny, annoying, spoiled brat!" Hayden responds.')
        print("\n Hayden then leaves, and eventually, you leave as well.")
    elif h == "c":
        print('\n "Oh, well, okay then," you say to Hayden.')
        print("\n You both then leave the theater.")
    elif h == "d":
        print('\n "Whatever you think is best, I suppose," you say.')
        print("\n You both then leave the theater.")
    else:
        print("\n That is not a valid option. Please type a valid keyword. The prompt will now be repeated.")
        h_agree()
        
def c_agree():
    global cassandra_hate
    print("\n After Hayden leaves the theater, Cassandra comes up to you.")
    print('\n "They are so annoying," she says.')
    print("\n What do you say?")
    print('\n a) "Yeah, totally,"')
    print(' b) "No, you are,"')
    print(' c) "I guess,"')
    print(' d) "Maybe,"')
    c = input("\n Type either 'a', 'b', 'c', or 'd' to choose what to say: ")
    if c == "a":
        cassandra_hate -= 1
        print('\n "Yeah, totally," you say to Cassandra.')
        print("\n Cassandra is pleased with your response and then walks away. You eventually leave the theater as well.")
    elif c == "b":
        cassandra_hate += 2
        print('\n "No, you are," you tell Cassandra.')
        print('\n "EXCUSE ME!?!" Cassandra yells.')
        print("\n Cassandra then stomps away. You eventually leave the theater as well.")
    elif c == "d":
        cassandra_hate += 1
        print('\n "Maybe," you say.')
        print('\n "What do you mean, maybe???" Cassandra asks.')
        print("\n Cassandra then walks away, annoyed. You eventually leave the theater as well.")
    elif c == "c":
        print('\n "I guess," you say to Cassandra.')
        print("\n Cassandra then leaves the theater. You do too, eventually.")
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        c_agree()
    

def argue():
    global bracelet
    global hayden_like
    global cassandra_hate
    print("\n As everybody is packing up and getting ready to leave, you hear two of the kids, Hayden and Cassandra, arguing.")
    print('\n "I KNOW YOU SWITCHED MY CABIN, HAYDEN!!!" Cassandra yells.')
    print('"\n I DID NOT! I PROMISE!" Hayden yells back.')
    print("\n You learn that although you are currently sharing a cabin with Cassandra, she originally requested a private one.")
    print('\n "IT HAD TO HAVE BEEN YOU! YOU ARE THE KID OF THE CAMP DIRECTORS!!!" Cassandra screams.')
    print('\n "I ALREADY TOLD YOU, I DID NOT SWITCH YOUR CABIN!!" Hayden yells back.')
    print("\n The argument begins getting worse and worse.")
    print("\n Who do you side with? ")
    print("\n a) Cassandra")
    print(" b) Hayden")
    agree = input("\n Type either 'a' or 'b' for who you want to side with: ")
    if agree == "a":
        cassandra_hate -= 2
        hayden_like -= 2
        print('\n "Yeah, Hayden, why would you switch her cabin?" you say, siding with Cassandra.')
        print('\n "I ALREADY SAID- YOU KNOW WHAT?? WHATEVER." Hayden says, walking away.')
        c_agree()
    elif agree == "b":
        bracelet += 1
        hayden_like += 3
        cassandra_hate += 3
        print('\n "Cassandra, they did not switch your cabin," you say, siding with Hayden.')
        print('\n "WHAT DO YOU KNOW ABOUT THIS?!?! UGH!!!" Cassanra screams, stomping off.')
        h_agree()
    else:
        print("\n That is not either 'a' or 'b'. The prompt will now be repeated.")
        argue()
        
def time():
    global timeslot
    print("\n After leaving the theater, you see a clipboard and a pencil outside of it.")
    print("\n 'AUDITION TIME SLOTS' the top of the paper reads.")
    print("\n You realize you still need to sign up. There are 4 time slots remaining. It is currently 10:00am.")
    print("\n What time slot do you choose? ")
    print("\n a) 11:30am to 11:45am")
    print(" b) 12:00pm to 12:15pm")
    print(" c) 1:30pm to 1:45pm")
    print(" d) 6:15pm to 6:30pm")
    slot = input("\n Type either 'a', 'b', 'c', or 'd' for the following time slot: ")
    if slot == "a":
        print("\n You choose to audition from 11:30 to 11:45 and go back to your cabin.")
    elif slot == "b":
        print("\n You choose to audition from 12:00 to 12:15 and go back to your cabin.")
        timeslot = "b"
    elif slot == "c":
        print("\n You choose to auditon from 1:30 to 1:45 and go back to your cabin.")
        timeslot = "c"
    elif slot == "d":
        print("\n You choose to audition from 6:15 to 6:30 and go back to your cabin.")
        timeslot = "d"
    else:
        print("\n That is not a valid choice. The prompt will now be repeated.")
        time()
    
    
def before():
    print("\n Some time passes, and it is now almost time for your audition.")
    if timeslot == "a":
        print("\n In your cabin, you notice that Reye and Juliet are currently talking. Probably about the show or their upcoming auditions.")
    elif timeslot == "b":
        print("\n In your cabin, you notice it is only you currently there. The other girls must be out for their auditions or something.")
    elif timeslot == "d":
        print("\n In your cabin, you notice Cassandra, Reye, and Juliet all are currently here. They must have already finished their auditions.")
    else:
        print("\n In your cabin, you see Cassandra peacefully scrolling on her bed, as if she knew she was going to get the lead role.")
        

def area_prep():
    global area_two_one
    global area_two_two
    global area_two_three
    global area_two_four
    global area_two_five
    global area_two_six
    global fin
    print("\n Below is a list of things you can do. Get ready for your audition.")
    while True:
        print(" ")
        if area_two_one:
            print(" 1) Practice your audition")
        if area_two_two:
            print(" 2) Do vocal warm-up")
        if area_two_three:
            print(" 3) Change your clothes")
        if area_two_four:
            print(" 4) Do your hair")
        if area_two_five:
            print(" 5) Silence your phone")
        if area_two_six:
            print(" 6) Mentally prepare brain")
        prep = input("\n Type a number 1-6 to do the corresponding action: ")
        if prep == "1":
            if area_two_one:
                print("\n You practice the audition you had already prepared before reaching Camp Cottonwood. You now feel ready for it.")
                fin += 1
            else:
                print("\n You have already practiced your audition. No need to practice anymore.")
            area_two_one = False
        elif prep == "2":
            if area_two_two:
                print("\n You do a quick vocal warm-up for your voice. Your voice is now warmed-up.")
                fin += 1
            else:
                print("\n You have already done a vocal warm-up. You do not need to do another one.")
            area_two_two = False
        elif prep == "3":
            if area_two_three:
                print("\n You go to the bathroom and put on a new pair of clothes. You now feel fresh.")
                fin += 1
            else:
                print("\n You have already changed your clothes. You do not need to change them again.")
            area_two_three = False
        elif prep == "4":
            if area_two_four:
                print("\n You do your hair nicely. It now looks good.")
                fin += 1
            else:
                print("\n You have already done your hair. It does not need to be done again.")
            area_two_four = False
        elif prep == "5":
            if area_two_five:
                print("\n You silence your phone. It now cannot go off during your audition.")
                fin += 1
            else:
                print("\n You have already silenced your phone. Double-silencing is not a thing.")
            area_two_five = False
        elif prep == "6":
            if area_two_six:
                print("\n You mentally prepare your brain for the audition by taking deep breathes. You are now not as stressed for it as before.")
                fin += 1
            else:
                print("\n You have already mentally prepared your brain. It is prepared enough.")
            area_two_six = False
        else:
            print("\n That is not a valid number from 1 to 6.")
        
        if fin == 6:
            print("\n You have officially fully prepared for your audition.")
            break
        

def nervous():
    print("\n You leave your cabin and head on over to the theater, where the audition is. Once you reach, you go inside, and see Bob and Lune waiting for you.")
    print('\n "Alright, next up... Erin Jaquevius," Lune says.')
    print('\n "Alright, Erin. This audition is going to go like any other. You will sing the song you practiced, perform the monologue you practiced, and do a quick scene from the musical of our choosing in any order." Bob explains.')
    print('\n "Are you feeling nervous, Erin?" Lune asks after.')
    print("\n What do you say?")
    print('\n a) "DEFENITELY!"')
    print(' b) "Not really,"')
    print(' c) "A little bit,"')
    print(' d) "Nope, not at all!"')
    nervo = input("\n Type either 'a', 'b', 'c', or 'd' for the following dialogue option: ")
    if nervo == "a":
        print('\n "DEFENITELY!" you say.')
        print('\n "Do not worry, just do your best!" Lune says after, comforting you.')
    elif nervo == "b":
        print('\n "Not really," you tell Lune.')
        print('\n "Good to hear," Lune replies.')
    elif nervo == "c":
        print('\n "A little bit," you say to Lune.')
        print('\n "Just do your best and it will be fine," Lune replies, comforting you.')
    elif nervo == "d":
        print('\n "Nope, not at all!" you say confidently.')
        print('\n "Well that is always good to hear!" Lune says after.')
    else:
        print("\n That is not either a, b, c, or d. The prompt will now be repeated.")
        nervous()
        
def area_audition():
    global area_three_one
    global area_three_two
    global area_three_three
    print('"\n You may now begin," Bob tells you.')
    print("\n Below is a list of things you can do. Perform your audition.")
    while True:
        print("")
        if area_three_one:
            print(" 1) Sing your song")
        if area_three_two:
            print(" 2) Perform your monologue")
        if area_three_three:
            print(" 3) Do the side")
        aud = input("\n Type a number 1-3 for corresponding action: ")
        if aud == "1":
            if area_three_one:
                if area_three_three and area_three_two:
                    print("\n You choose to start your audition by singing your song. You begin, feeling nervous. During your song, Lune and Bob bop their heads as if they love it. But then you realize that is what the people hosting an audition always do.")
                else:
                    print("\n You perform your song next. During your song, Lune and Bob bop their heads as if they love it. But then you realize that is what the people hosting an audition always do.")
            else:
                print("\n You have already sang your song. Bob and Lune do not want you to do it again.")
            area_three_one = False
        elif aud == "2":
            if area_three_two:
                if area_three_one and area_three_three:
                    print("\n You choose to do your monologue first. You begin performing it, feeling quite nervous but trying your best nonetheless.")
                else:
                    print("\n Next, you perform your monologue. You begin, trying your absolute best to do well.")
            else:
                print("\n You have already performed your monologue. Bob and Lune do not want you to perform it again.")
            area_three_two = False
        elif aud == "3":
            if area_three_three:
                if area_three_one and area_three_two:
                    print("\n You decide to do your side first, a shocker to Bob and Lune. Usually, sides are the thing done last in an audition. But nevertheless, you choose to do it first, and Bob and Lune ask you to act as Veronica, the lead, for a scene. That has to be a good sign!")
                elif area_three_one and not area_three_two:
                    print("\n You decide to your side second, which kind of surprises Lune and Bob. Typically, sides are the last thing done in an audition. But nevertheless, you do it second, and Bob and Lune ask you to act as Veronica, the lead, for a scene. That has to be a good sign!")
                elif area_three_two and not area_three_one:
                    print("\n You decide to your side second, which kind of surprises Lune and Bob. Typically, sides are the last thing done in an audition. But nevertheless, you do it second, and Bob and Lune ask you to act as Veronica, the lead, for a scene. That has to be a good sign!")
                else:
                    print("\n Finally, you do the side. This does not surprise Bob or Lone, considering the fact that sides are almost always done last in an audition. Bob and Lune ask you to act as Veronica, the lead, for a scene. That has to be a good sign!")
            else:
                print("\n You have already done your side. Lune and Bob do not want you to do it again.")
            area_three_three = False
        else:
            print("\n That is not a valid option.")
        
        if not area_three_one and not area_three_two and not area_three_three:
            print("\n Congratulations: you have officially completed your audition.")
            print('\n "Alright, see you in rehearsal, Erin. You did great!" Lune says enthusiastically.')
            print("\n You then leave the theater, feeling good about your audition.")
            break
        
    
def scream():
    global outside
    print("\n Eventually, the clock hits 9:30pm. After having a quick bite and walking around the camp, you ahead back to your cabin. As you enter, you see Cassandra walking out of the bathroom. When she walks out, she sees something. That something is blocked by the door being half-closed, as you had just startd opening it. Cassandra then screams.")
    print("\n What do you do? ")
    print("\n a) Step away")
    print(" b) Walk in")
    door = input("\n Type either 'a' or 'b' for the following decision: ")
    if door == "a":
        print("\n You step away, quietly closing the door. You are now just waiting outside.")
        outside = False
    elif door == "b":
        print("\n You step inside, trying to figure out what is going on.")
    else:
        print("\n That is not a valid keyword. Please type either a or b. The prompt will now be repeated.")
        scream()
        
def inout():
    if outside:
        print("\n You hear Cassandra screaming something inside. You overhear something about kissing.")
        print("\n Suddenly, Cassandra bursts out of the door, screaming and running. A few seconds later, Juliet runs out and chases her, seeming extremely angry.")
        print("\n You then go inside, and see Reye sitting there, silent.")
        print("\n You piece together that what happened was Cassandra walked out of the bathroom and saw Reye and Juliet kissing, and probably got disugsted and ran off.")
    else:
        print("\n You see that where the door was blocking stood Reye and Juliet. They quicky pull away from each other.")
        print('\n "YOU ARE OUT HERE IN THE MIDDLE OF THE GIRLS CABIN KISSING!?!?! EW!!!!!!!!" Cassandra screams.')
        print("\n Suddenly, Cassandra bursts out of the door, screaming.")
        print('\n "UGH, YOU ARE SO ANNOYING!!!" Juliet screams.')
        print("\n Juliet then chases after here. Now, just you and Reye stand there, silent.")
        
def cast():
    print("\n Not wanting to get involved in all this drama, you go to sleep, nervous for the tommorow, the day the cast list drops.")
    print("\n You wake up late the next day. Today is more a free day, whereas rehearsals start tommorow.")
    print("\n You instantly reach over for your phone for your annual dopamine session at the start of each morning, and you see you got an email.")
    print("\n The title of the email is bold and clear: ")
    print("\n 'CAST LIST' it reads.")
    print("\n Your heart begins racing as you slowly open the email.")
    print("\n Veronica………………………………………Erin Jaquevius")
    print("\n Jason Dean…………………………………Ben Glost")
    print("\n Heather Chandler…………………Cassandra Ward")
    print("\n Heather Duke……………………………Ollie Moore")
    print("\n Heather McNamara…………………Reye Taser")
    print("\n Martha Dunnstock…………………Maysliee Donner")
    print("\n Kurt…………………………………………………Andrew Lorn")
    print("\n Ram……………………………………………………Michael Mell")
    print("\n Veronica U/S……………………………Terri Smith")
    print("\n Jason Dean U/S………………………Caspian Conners")
    print("\n Heather Chandler U/S………Juliet Samuels")
    print("\n Heather Duke U/S…………………Lela Marksman")
    print("\n Heather McNamara U/S………Isla View")
    print("\n You had done it! You had successfully landed the female lead role, Veronica!")
 
def crashout():
    global cassandra_hate
    cassandra_hate += 1
    print("\n Suddenly, Cassandra bursts into the cabin.")
    print('\n "ERIN STUPID STUPID JAQUEVIUS!!!!!" she screams violently.')
    print('\n "Oh no," you think, already able to guess why she is mad.')
    print('\n "YOU STOLE HER! YOU STOLE VERONICA!!! VERONICA WAS MINE. I GET THE LEAD ROLE EVERY YEAR. EVERY. SINGLE. YEAR. WHAT DO YOU HAVE TO SAY FOR YOURSELF!?!" she yells.')
    print("\n What do you do?")
    print("\n a) Apologize to Cassandra")
    print(" b) Fight back")
    crash = input("\n Type either 'a' or 'b' for the following choice: ")
    if crash == "a":
        cassandra_hate += 1
        print('\n "Look, I am sorry, I truly am, I just... I cannot control the casting," You say softly.')
        print('\n "UGH!!! WHATEVER," Cassandra replies, storming off.')
    elif crash == "b":
        cassandra_hate += 2
        print('\n "Oh, shut up, Cassandra! Just deal with it, you did not get the lead role ONE TIME. And it is probably for a reason!" you tell Cassandra.')
        print('\n "UGH, YOU ARE THE MOST ANNOYING PERSON I HAVE EVER MET! UGH!!!!!" Cassandra screams, storming off.')
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        crashout()
        
def date():
    print("\n After Cassandra leaves, you see Reye and Juliet together. They both are wearing nice clothes, as if they are going on a date.")
    print('\n "I AM SO HAPPY I GOT HEATHER MCNAMARA, IT IS LITERALLY MY DREAM ROLE!" Reye says happily.')
    print('\n Juliet looks a little sad. You remember that she was cast as a U/S, meaning she was just an Understudy.')
    print('\n "I have to an understudy for CASSANDRA..." Juliet says, annoyed.')
    print("\n Reye comforts her as they walk out for their dinner.")
    
def rehearsal():
    print("\n A few weeks go by. Rehearsal is going well, and Reye and Juliet are really happy together. In your cabin, you see Cassandra still sleeping, and she is coughing a lot.")
    print('\n "Someone is going to be late to rehearsal," you think.')
    print("\n Today, you are rehearsing a scene where the character Cassandra is playing dies by getting poisoned with drain cleaner.")
    print("\n You walk on over to the theater for rehearsal. As you enter, you see Ben stand up, ready to rehearse.")
    print('\n "Odd," you think.')
    print("\n To your left, you see Hayden, the kid doing lights and set design looking over at the drain cleaner being used. In reality, it is just blue soda from the restaurant, since you cannot actually give Cassandra drain cleaner. Or who knows, maybe you can.")
    print('\n "Alright, let us start!" Bob says.')
    print('\n "Wait, where is Cassandra? We need Heather Chandler for this scene." Hayden points out.')
    print("\n Suddenly, someone in the costume for Heather Chandler runs on stage, giving Bob a thumbs up. They were fully in costume, explaining why they were late.")
    print("\n A bit later, you finish the scene. But then you remember something. Cassandra was back in her bed, sick.")
    print("\n 'Uhm, Cassandra? The scene is over, drama queen,' you hear Bob say.")
    print("\n The person in the Heather Chandler costume was not standing up.")
    print('\n "Uhm, guys? This drain cleaner.... It.. Is actually drain cleaner. It is not blue soda." Ben says.')
    print("\n Blood starts coming out of the mouth of Cassandra. Except....")
    print('\n "Wait... JULIET!" you think.')
    print("\n You remember Juliet saying she was the understudy for Cassandra weeks ago, and you remember the cast list.")
    if juliet_final_words >= 2:
        print("\n As Juliet is dying, she looks up at you and tries to reach for your help, but cannot. She does not have the strength for it.")
    elif juliet_final_words == 1:
        print("\n As Juliet is dying, she gives smiles at you, but it quickly fades away.")
    else:
        print("\n As Juliet is dying, she stares at the wall blankly.")
    print("\n Coincidentally, and heartbreakingly, Reye then walks in. Once she sees Juliet, she drops against the wall.")
    print('\n "Reye..... I am so sorry......" you say as she begins crying.')
    print("\n Congratulations: you have discovered your only goal. Find the murderer.")
    
def area_crime():
    global area_four_one
    global area_four_two
    global area_four_three
    global area_four_four
    global area_four_five
    global area_four_six
    global area_four_seven
    print("\n Below is a list of things you can investigate. Look around for clues as to what happened.")
    while True:
        print("")
        if area_four_one:
            print(" 1) Juliet's body")
        if area_four_two:
            print(" 2) The bottle of drain cleaner")
        if area_four_three:
            print(" 3) Backstage")
        if area_four_four:
            print(" 4) Under Bob's desk")
        if area_four_five:
            print(" 5) On top of Bob's desk")
        if area_four_six:
            print(" 6) Your script")
        if area_four_seven:
            print(" 7) The entrance to the theater")
        scene = input("\n Type a number 1-7 for the corresponding thing to investigate: ")
        if scene == "1":
            if area_four_one:
                print("\n You take a close look at Juliet's body. You don't see anything unsual besides... The unusual.")
            else:
                print("\n You have already looked at Juliet's body. No need to look at it again.")
            area_four_one = False
        elif scene == "2":
            if area_four_two:
                print("\n You check the drain cleaner. It's not full, but it's not empty. Juliet defenitely took a sip, but it defenitely didn't taste great.")
            else:
                print("\n You have already checked the drain cleaner. You don't need to check it again.")
            area_four_two = False
        elif scene == "3":
            if area_four_three:
                print("\n You go backstage, and see no one, and nothing out of the ordinary.")
            else:
                print("\n You have already been backstage. No need to go back.")
            area_four_three = False
        elif scene == "4":
            if area_four_four:
                print("\n You check under Bob's desk. Nothing.")
            else:
                print("\n You have already checked under Bob's desk. There was nothing there.")
            area_four_four = False
        elif scene == "5":
            if area_four_five:
                print("\n You look on top of Bob's desk. Just a bunch of scripts, papers, and useless junk.")
            else:
                print("\n You have already looked on top of Bob's desk. There was nothing there.")
            area_four_five = False
        elif scene == "6":
            if area_four_six:
                print("\n You look at your script. It's just a script, nothing more.")
            else:
                print("\n You have already looked at your script. It's just a script.")
            area_four_six = False
        elif scene == "7":
            if area_four_seven:
                print("\n You check the entrance to the theater. Other than Reye, no one has entered or left recently.")
            else:
                print("\n You have already checked the entrance to the theater. Nothing.")
            area_four_seven = False
        else:
            print("That is not a valid number from 1 to 7.")
        if not area_four_one and not area_four_two and not area_four_three and not area_four_four and not area_four_five and not area_four_six and not area_four_seven:
            print("\n Congratulations: you have investigated the entire theater. But unfortunately, you found nothing.")
            break
        
        
def cops():
    print("\n After Bob calls the police, you wait there silently. Reye is currently just sitting in the corner, depressed.")
    print("\n Eventually, the police arrive. Bob and Lune talk to them. You talk over to see what's going on.")
    print('\n "We have concluded that it was a mix-up, a mistake regarding the placement of the drain cleaner. There is no murderer." the first officer says.')
    print("\n What do you say?")
    print('\n a) "Oh, I see,"')
    print(' b) "Okay, well, thank you officer,"')
    print(' c) "Are you sure?"')
    print(' d) "That cannot be right!"')
    ask = input("\n Type either 'a', 'b', 'c', or 'd' for the following choice: ")
    if ask == "a":
        print('\n "Oh, I see," you say. The cops then head out, finishing their investigation.')
    elif ask == "b":
        print('\n "Okay, well, thank you officer," you say to the cop.')
        print('\n "No problem, madam. Have a good day, everyone," the cop says after.')
        print("\n The cops then head out, finishing their investigation.")
    elif ask == "c":
        print('\n "Are you sure?" you ask the cop.')
        print('\n "Yes, we have logically concluded that the only explanation is a mix-up." The cop responds.')
        print("\n The cops then head out, finishing their investigation.")
    elif ask == "d":
        print('\n "That cannot be right!" you say to the cop.')
        print('\n "Excuse me?" the cop responds.')
        print('\n "Mam, please do not interfere with authority business." Another cop says to you.')
        print('\n "After thorough investigation, we have formally decided the only explanation is a mix-up." the first cop then says.')
        print("\n The cops then head out, finishing their investigation.")
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        cops()
        
def area_find():
    global collectibles
    global area_five_one
    global area_five_two
    global area_five_three
    global area_five_four
    global area_five_five
    global area_five_six
    global area_five_seven
    print("\n Rehearsals were paused for the next week until Camp Cottonwood figured out what to do.")
    print("\n You think about the situation. The cops said it was a mix-up, but it did not really make sense. No one would accidentally but a bottle of REAL drain cleaner in that spot. It had to have been a deliberate murder.")
    print("\n You realize that to solve the murder, all you needed to do was get access to the security footage. But you knew you could not just barge in on the directors, who you have not even seen yet, and force them to give you the security footage.")
    print("\n But there is something you can do: ask their child, Hayden.")
    print("\n Below is a list of places you can check. Find Hayden.")
    while True:
        print("")
        if area_five_one:
            print(" 1) The restaurant")
        if area_five_two:
            print(" 2) The theater")
        if area_five_three:
            print(" 3) The receptionist office")
        if area_five_four:
            print(" 4) The cliff")
        if area_five_five:
            print(" 5) The nurse's office")
        if area_five_six:
            print(" 6) The vending machine")
        if area_five_seven:
            print(" 7) The private cabin")
        locate = input("\n Type a number 1-7 for the corresponding place to check for Hayden: ")
        if locate == "1":
            if area_five_one:
                print("\n You go over to the restaurant, but see it's closed, meaning Hayden can't be there.")
            else:
                print("\n You have already checked the restaurant. It's closed, so Hayden can't be there.")
            area_five_one = False
        elif locate == "2":
            if area_five_two:
                print("\n You head over to the theater, but don't see Hayden. You suspect it's because rehearsal just ended.")
            else:
                print("\n You have already checked the theater. Hayden isn't there.")
            area_five_two = False
        elif locate == "3":
            if area_five_three:
                print("\n You go to the receptionist office and see Lune working there but no Hayden.")
                print("\n However, you find a blue bracelet on the ground.")
                print("\n Congratulations: you have found a Collectible item. You pick up the blue bracelet and wear it.")
                collectibles += 1
            else:
                print("\n You have already checked the receptionist office. Lune's there, but not Hayden.")
            area_five_three = False
        elif locate == "4":
            if area_five_four:
                print("\n You look over at the cliff. No way Hayden's over there.")
            else:
                print("\n You have already looked at the cliff. Hayden isn't there.")
            area_five_four = False
        elif locate == "5":
            if area_five_five:
                print("\n You go over to the nurse's office, but you remember that although Juliet was, Hayden wasn't hurt in any way, so they won't be there.")
            else:
                print("\n You have already checked the nurse's office. Hayden isn't there.")
            area_five_five = False
        elif locate == "6":
            if area_five_six:
                print("\n You walk over to the vending machine. Hayden... Luckily didn't get stuck inside.")
            else:
                print("\n You have already checked the vending machine. Hayden isn't there.")
            area_five_six = False
        elif locate == "7":
            print("\n You go over to the private cabin. Knowing that Hayden is the kid of the camp's directors, you know they must be here.")
            print("\n Congratulations: you have officially found where Hayden is.")
            print("\n You knock on the door, waiting for a response.")
            break
        else:
            print("\n That is not a valid number from 1 to 7.")
            
def footage():
    print("\n After waiting for a moment, someone opens the door. It's Hayden.")
    print("\n What do you say?")
    print('\n a) "I need your help,"')
    print(' b) "Can you help me solve the murder?"')
    print(' c) "I need to see the security footage."')
    print(' d) "Can I see the security footage?"')
    helpme = input("\n Type either 'a', 'b', 'c', or 'd' for the following dialogue option: ")
    if helpme == "a":
        print('\n "I need your help," you tell Hayden.')
        print('\n "Uhm, okay? With what?" they ask.')
        print('\n "We both know what happened with Juliet was no accident. We can easily figure out what happened if we look at the security footage.')
        print('\n "So, what do you need my help for?" Hayden then asks.')
        print('\n "Well, your parents probably will not just show me the security footage. But I know you can. Please, just help me out here," you say.')
        print("\n You see Hayden thinking for a moment.")
        print('\n "Alright, let us solve this murder." Hayden then says.')
    elif helpme == "b":
        print('\n "Can you help me solve the murder?" you ask directly.')
        print('\n "Uh- what?" Hayden asks.')
        print('\n "We both know what happened was no accident, and your parents probably will not just show me the security footage. But I know you can," you tell Hayden.')
        print('\n "Uhm, okay?" Hayden then says.')
        print('\n "So, can you help me?" you then ask.')
        print("\n You see Hayden thinking for a moment. They seem a little surprised as to what was going on.")
        print('\n "Um, alright sure, I guess," Hayden says.')
    elif helpme == "c":
        print('\n "I need to see the security footage." you tell Hayden.')
        print('\n "Um, excuse me? Why?" Hayden asks after.')
        print('\n "We both know what happened with Juliet was no accident, right?" you ask.')
        print('\n "Right," Hayden replies, intrigued.')
        print('\n "So, if we can get our hands on the security footage, we can solve the murder. What do you say?" you say after.')
        print("\n You see Hayden thinking for a moment, interested in your idea.")
        print('\n "Alright, sure. Let us do this," they then say.')
    elif helpme == "d":
        print('\n "Can I see the security footage?" you ask Hayden directly.')
        print('\n "Um, okay? Why?" Hayden asks.')
        print('\n "We both know what happened with Juliet was no accident, right?" you ask.')
        print('\n "Right," Hayden replies, intrigued.')
        print('\n "So, if we can see security footage, we can solve the murder. What do you say?" you say after.')
        print("\n You see Hayden thinking for a moment.")
        print('\n "Alright, sure. Let us do this," they then say.')
    else:
        print("That is not a valid keyword. The prompt will now be repeated.")
        footage()
        
def car():
    global fates
    print("\n On your way to Hayden's office, you see a car nearby. Suddenly, Cassandra comes up from you.")
    print('\n "GOODBYE, ERIN!!!" she screams angirly, heading for the exit of the camp.')
    print('\n "Uh- what?" you say.')
    print('\n "YOU HAVE SINGLE-HANDEDLEY RUINED MY ENTIRE EXPERIENCE AT CAMP COTTONWOOD THIS YEAR. SO I AM DONE. GOODBYE!!!" Cassandra screams, walking off.')
    print("\n Suddenly, the car drives forward as Cassandra tries to exit, hitting her.")
    print('\n "AHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!" Cassandra screams in pain.')
    print("\n You watch as Cassandra bleeds out and dies. The person driving the car then gets out. It's Bob.")
    print('\n "BOB, WHAT IN THE-" you try saying.')
    print('\n "What?" he says, playing dumb.')
    print('\n "YOU JUST HIT CASSANDRA WITH A CAR!!!!!" you yell.')
    print("\n Bob then looks around.")
    print('\n "No I did not," Bob then says.')
    print("\n What do you do?")
    print("\n a) Call the cops")
    print(" b) Let it go")
    crash = input("\n Type either 'a' or 'b' for the following decision: ")
    if crash == "a":
        fates["Bob"] = "DEAD"
        print('\n "Alright, I am calling the cops," you say.')
        print("\n Bob looks bummed out.")
        print('\n "Oh, come on, man! I do NOT want to spend the rest of my days in jail." Bob then says.')
        print("\n Bob then tries to run away, but another car hits him and he dies.")
        print('\n "K- karma?" you think as the other car speeds off.')
        print("\n You realize you could go after the other car, but you have more important things to worry about. There could be a literal murderer on the loose.")
        print("\n And so, you leave, continuing your walk over to Hayden's office.")
    elif crash == "b":
        print('\n "I- I will choose to let it go, since it was an accident and Cassandra was not exactly a great person..." you tell Bob.')
        print('\n "Let what go?" Bob asks, confused.')
        print("\n You sigh as Bob walks off. You remember you have more important matters to deal with, as there could be a murderer out there.")
        print("\n And so, you leave, continuing your walk over to Hayden's office.")
    else:
        print("\n That is not a valid keyword. Please type either a or b. The prompt will now be repeated.")
        car()
    
def backflip():
    global fates
    print("\n On your way to Hayden's office, you see a car. It then stops as the driver notices you, and he then gets out of the car and walks over to you.")
    print('\n "It is time. I AM GOING TO DO IT!" Bob says, excited.')
    print('\n "Do what?" you ask, pausing.')
    print('\n "A BACKFLIP! I am SO excited. Ready!?!" Bob then says.')
    print("\n You go silent.")
    print('\n "3........ 2.............." Bob begins saying.')
    print("\n What do you do?")
    print("\n a) Stop him")
    print(" b) Let him")
    flip = input("\n Type either 'a' or 'b' for the following decision: ")
    if flip == "a":
        print('\n "Bob... How about we.... No, just no," you say.')
        print("\n Bob looks over at you in pure despair.")
        print('\n "Ugh, fine... You are right. I knew I was not ready yet..." Bob says, walking off.')
        print("\n You then leave, continuing your walk over to Hayden's office.")
    elif flip == "b":
        fates["Bob"] = "DEAD"
        print("\n You let Bob do a backflip. He goes ahead, and... Failes. Miserably.")
        print('\n "Um......... Okay," you think akwardly.')
        print("\n He's dead. Bob died from failing the backflip.")
        print("\n While digging up his grave, you realize, you have more important matters to attend to. There could be an actual murderer out there.")
        print("\n And so, you leave, continuing your walk over to Hayden's office.")
    else:
        print("\n That is not a valid option. The prompt will now be repeated.")
        backflip()
        
def branch_one():
    global cassandra_five
    print("\n You had successfully convinced Hayden to help you solve the murder. They then say they'll meet you in their parents' office, where the security footage is. So, you head over there.")
    if cassandra_hate >= 5:
        car()
    else:
        cassandra_five += 1
        backflip()
    
def see():
    global hayden_like
    print("\n Eventually, you reach Hayden's office. After waiting for about a minute, they arrive.")
    print('\n "You ready for this?" Hayden asks.')
    print("\n What do you say?")
    print('\n a) "Not really,"')
    print(' b) "I think so,"')
    print(' c) "Yeah,"')
    print(' d) "Yep, we got this,"')
    say = input("\n Type either 'a', 'b', 'c', or 'd' for the following decision: ")
    if say == "a":
        hayden_like += 1
        print('\n "Not really," you tell Hayden honestly.')
        print('\n "Yeah, me neither," Hayden replies, agreeing with you.')
        print("\n You and Hayden then enter the office.")
    elif say == "b":
        print('\n "I think so," you say unconfidently.')
        print("\n You and Hayden then enter the office.")
    elif say == "c":
        print('\n "Yeah," you say.')
        print("\n You and Hayden then enter the office.")
    elif say == "d":
        print('\n "Yep, we got this," you say confidently.')
        print('\n "Glad one of us ready at least," Hayden says.')
        print("You and Hayden then enter the office.")
    else:
        print("\n That is not a valid keyword. Please type either 'a', 'b', 'c', or 'd'. The prompt will now be repeated.")
        see()

def bracelets():
    global hayden_like
    global collectibles
    print("\n While walking towards the security cameras, Hayden looks over at you.")
    print('\n "Hey, do you like my bracelet? I just got it recently," Hayden asks.')
    print("\n The bracelet is bright orange.")
    print("\n What do you say?")
    print('\n a) "Yeah, I do,"')
    print(' b) "No, it is ugly,"')
    print(' c) "I love it,"')
    print(' d) "Not an orange fan really,"')
    orange = input("\n Type either 'a', 'b', 'c', or 'd' for the following dialogue choice: ")
    if orange == "a":
        hayden_like += 1
        print('\n "Yeah, I do," you say.')
        print("\n Hayden smiles, happy that you like their bracelet.")
        print("\n As you smile back, you see the security cameras.")
    elif orange == "b":
        hayden_like -= 1
        print('\n "No, it is ugly," you say.')
        print('\n "Hey!" Hayden says, not sure if you were joking or not.')
        print("\n It gets a little silent, but you eventually see the security cameras, cutting out the akwardness.")
    elif orange == "c":
        hayden_like += 2
        print('\n "I love it," you tell Hayden.')
        if bracelet == 1:
            collectibles += 1
            print('\n "Aw, thanks! You know what, here, take it." Hayden says.')
            print("\n Congratulations: you have found a Collectible item. You put the bracelet on.")
            print('\n "Oh, and there are the cameras!" Hayden says, spotting them.')
        else:
            print('\n "Oh, thanks!" Hayden says, genuinely happy.')
            print("\n You feel good to have made Hayden happy.")
            print('\n "Oh, there are the cameras," Hayden says, spotting them.')
    elif orange == "d":
        print('\n "Not an orange fan, really," you say honestly.')
        print('\n "Oh," Hayden says, indifferent.')
        print("\n Eventually, you spot the security cameras.")
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        bracelets()
        
def watching():
    print("\n Hayden sits down, turning on the cameras. They then begin running through the footage, looking for the day Juliet died.")
    print('\n "Here. A camera of the supply closet," they say, finding the exact date.')
    print('\n "You watch as Andrew, one of the kids you remember from orientation, walk into the supply closet. He then grabs something, but it is unclear what. Hayden then pauses the recording."')
    print('\n "So I guess Andrew is a suspect for grabbing an unknown item," you say.')
    print('\n "Yeah. But what even was the item? And why would he want to kill Juliet?" Hayden says.')
    print('\n "Yeah, that is true. Weird," you say as Hayden switches to another camera.')
    print("\n The camera Hayden switched to was of the stage. There was a bottle of drain cleaner on it.")
    print("\n You wait for awhile. No one comes on. But then, just when you least expect it, someone finally walks in, replacing the bottle of drain cleaner on the stage with an new one.")
    print("\n   YOU.")
    cont = input("\n Type 'continue' to continue playing: ")
    if cont.lower() == "continue":
        print('\n "What............" Hayden says, quietly.')
        print("\n It makes zero sense. You have no memory of this.")
    else:
        print("\n That is not a valid option for this prompt. The same message will now be repeated.")
        watching()
        
def defense():
    print("\n What do you say?")
    print('\n a) "Hayden, I promise, I have no memory of this!"')
    print(' b) "Hayden, this is bad. I must have been manipulated!"')
    defe = input("\n Type either 'a' or 'b' for the following dialogue choice: ")
    if defe == "a":
        if bracelet == 1:
            print('\n "Hayden, I promise, I have no memory of this!" you say.')
            print('\n "Yeah, this is weird. You... have to have been drugged," Hayden says, worried.')
            print('\n "DRUGGED!?!" you panic.')
        else:
            print('\n "Hayden, I promise, I have no memory of this!" you say.')
            print('\n "It... Just does not make sense. If it was you, why would you come to report the murder and TELL me to look at the cameras? You had to have been drugged," Hayden says.')
            print('\n "DRUGGED?!!" you panic.')
    elif defe == "b":
        if bracelet == 1:
            print('\n "Hayden, this is bad. I must have been manipulated!" you say.')
            print('\n "Yeah. You... you had to have been... Drugged," Hayden replies.')
            print('\n "DRUGGED?!?" you panic.')
        else:
            print('\n "Hayden, this is bad. I must have been manipulated!" you say.')
            print('\n "It... Just does not make sense. If it was you, why would you come to report the murder and TELL me to look at the cameras? You had to have been drugged," Hayden says.')
            print('\n "DRUGGED!??" you panic.')
    else:
        print("\n That is not a valid option. Please type either 'a' or 'b'. The prompt will now be repeated.")
        defense()
        
def goback():
    print("\n You head back to your cabin, ready to finally relax after one crazy day.")
    print("\n After some relaxing, someone knocks on your cabin's door. You go to open it, and see Ollie, another kid at camp.")
    print('\n "Hey, sorry but random question, but have you seen Reye? No has seen her for a bit, and the last time someone saw her she was going towards the cliff for some reason." Ollie says.')
    print('\n "No, I have not. Let me go look for her," you say.')
    print("\n You head over to the cliff to look for Reye. It's oddly silent and peaceful there.")
    print("\n You slowly and carefuly walk up the cliff, looking for Reye.")
    print('\n "Reye?" you say.')
    print("\n But you get no response. It is DEAD silent.")
    print('\n "Where could she be?" you think.')
    print("\n What do you say?")
    print('\n a) "Reye, where are you?!"')
    print(' b) "Hello?!?"')
    print(' c) "Reye, are you here???"')
    print(' d) "What is going on?!"')
    huh = input("\n Type either 'a', 'b', 'c', or 'd' for the corresponding dialogue option: ")
    if huh == "b":
        print('\n "Hello?!?" you say.')
    elif huh == "a":
        print('\n "Reye, where are you?!" you say.')
    elif huh == "c":
        print('\n "Reye, are you here???" you say.')
    elif huh == "d":
        print('\n "What is going on?!" you say.')
    else:
        print("\n That is not a valid keyword. Please type either 'a', 'b', 'c', or 'd'. The same message will now be repeated.")
        goback()
    print("\n But you get no response. Eventually, you make it over to the edge of the cliff.")
    print("\n You peak over, looking down. Frightened by what you see, you peak a little too far over.")
    print("\n You then feel yourself fall.")
    print("\n Down.")
    print("\n Down.")
    print("\n Down.")
    print("\n THUD.")

def gocliff():
    print("\n You decide to calm your mind by taking a walk.")
    print("\n After some walking, you end up near the cliff. It's a very peaceful place, and you enjoy your walk there.")
    print("\n But suddenly, you see Reye. She is starring off into the distance.")
    print('\n "Reye? What are you doing here?" you ask, confused.')
    print('\n "I... Have been thinking, Erin. I... I.. I am so sad about Juliet. Not only did she die... But I think it was my fault. I was the one in charge of replacing the drain cleaner with blue soda. And I could have sworen I did. But I do not know.... I think I killed Juliet." Reye said, sadly.')
    print('\n At first you feel confused, but then it makes sense. Reye must have put the original bottle which was ACTUALLY blue soda, but you, being drugged, replaced it.')
    print('\n "Reye... You did not kill Juliet." you say.')
    print('\n "What? How do you know?" Reye says seriously, walking over to you.')
    print('\n "Because I did," you say honestly.')
    print("\n Reye's eyes then light up. You realize the way you said what you said was not the way you should have said what you said.")
    print("\n Reye then approaches you, feeling nothing but pure rage.")
    print("\n What do you say now?")
    print('\n a) "NO- PLEASE-"')
    print(' b) "WAIT, LET ME EXPLAIN-"')
    print(' c) "No, No, NO, NO-"')
    print(' d) "WAIT WAIT WAIT WAIT-"')
    ohno = input("\n Type either 'a', 'b', 'c', or 'd' for following dialogue option: ")
    if ohno == "a":
        print('\n "NO- PLEASE-" you try saying.')
    elif ohno == "b":
        print('\n "WAIT, LET ME EXPLAIN-" you try saying.')
    elif ohno == "c":
        print('\n "No, No, NO, NO-" you try saying.')
    elif ohno == "d":
        print('\n "WAIT WAIT WAIT WAIT-" you try saying.')
    else:
        print("\n That is not a valid keyword. Please type either 'a', 'b', 'c', or 'd'. The same message will now be repeated.")
        gocliff()
    print("\n But it is far too late. Reye then grabs you and pushes you down the cliff.")
    print("\n You then feel yourself fall.")
    print("\n Down.")
    print("\n Down.")
    print("\n Down.")
    print("\n THUD.")


def after():
    global reye_died_early
    print("\n A few hours pass. Hayden had been desperately looking through more cameras while you walked around Camp Cottonwood, shocked.")
    print("\n What do you do now?")
    print("\n a) Go back to your cabin")
    print(" b) Go on a walk")
    where = input("\n Type either 'a' or 'b' for the following place to go: ")
    if where == "a":
        goback()
    elif where == "b":
        reye_died_early = False
        gocliff()
        
def area_forest():
    global reye_died_early
    global collectibles
    global area_six_one
    global area_six_two
    global area_six_three
    global area_six_four
    global area_six_five
    if reye_died_early:
        print("\n After falling, you wake up in the middle of the forest, having completed rolled down the cliff, not sure how you're alive.")
    else:
        print("\n After Reye pushed you down the cliff, you wake up in the middle of the forest, having completed rolled down the cliff, not sure how you're alive.")
    print("\n Below is a list of places you can check. Find your way back to the main camp area.")
    while True:
        print("")
        if area_six_one:
            print(" 1) The bush ahead of you")
        if area_six_two: 
            print(" 2) Behind the tree next to you")
        if area_six_three:
            print(" 3) To the right")
        if area_six_four:
            print(" 4) To the left")
        if area_six_five:
            print(" 5) Where you fell")
        escape = input("\n Type a number 1-5 for the corresponding place to check: ")
        if escape == "5":
            if area_six_five:
                collectibles += 1
                print("\n You check back where you fell. It's a dead end, but, you do see your blue sweater. It must have fallen off of you while rolling down.")
                print("\n Congratulations: you have found a Collectible item. You put your sweater back on.")
            else:
                print("\n You have already been here. It's a dead end.")
            area_six_five = False
        elif escape == "1":
            if area_six_one:
                print("\n You check the bush ahead of you. No luck.")
            else:
                print("\n You have already been here. There is no path ahead of the bush.")
            area_six_one = False
        elif escape == "2":
            print("\n You look behind the tree next to you, and see a path back to the camp.")
            print("\n Congratulations: you have found the way out.")
            print("\n You walk along the path to head back to the camp.")
            break
        elif escape == "3":
            if area_six_three:
                print("\n You check to your right. Nothing.")
            else:
                print("\n You have already looked to your right. It's nothing but a dead end.")
            area_six_three = False
        elif escape == "4":
            if area_six_four:
                if reye_died_early:
                    print("\n You look to your left. You then see the same gruesome thing you saw right before you fell down.")
                    print("\n A dead body.")
                    print("\n Reye's.")
                    print("\n You need to find out how to get back. As quickly as possible.")
                else:
                    print("\n You look to your left. Nothing.")
            else:
                if reye_died_early:
                    print("\n You have already checked here. No use in staring at Reye's dead body.")
                else:
                    print("\n You have already checked here. It is not the way back.")
            area_six_four = False
        else:
            print("That is not a valid nuber from 1 to 5.")
            
def cass():
    global cassandra_five
    print("\n As you walk through the forest, you see someone also walking around. It's Cassandra.")
    print('\n "Cassandra? What are you doing here?" you ask.')
    print('\n "Um, just... Thinking. I talked to Ollie earlier and he said some things... That I need to think about." Cassandra said.')
    print("\n You feel surprised, having heard Cassandra say something in a somewhat normal tone.")
    print('\n "Well, it does not matter. I do NOT need to explain myself to you." Cassandra then says, walking off.')
    print("\n As Cassandra walks off, you see her walking further and further away from the camp.")
    print("\n What do you do?")
    print("\n a) Tell her to stop")
    print(" b) Keep walking")
    two = input("\n Type either 'a' or 'b' for the corresponding action: ")
    if two == "a":
        cassandra_five += 1
        print('\n "Cassandra, stop. You do not know what is out there, it is probably dangerous." you tell Cassandra.')
        print("\n Cassandra then turns around.")
        print('\n "And plus, why go further away from the camp? There is a murderer on the loose. It... is just not safe." you then say.')
        print("\n Cassandra then stares at you.")
        print('\n "Ugh, whatever," Cassandra then says, walking back to the camp.')
        print("\n You then continue on walking back to the camp.")
    elif two == "b":
        print("\n You continue on walking, letting Cassandra go deeper into the wilderness.")
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        cass()
        
def bird():
    print("\n While walking back to the camp, you see a bird on the ground, seemingly suffering lots of pain.")
    print("\n What do you do?")
    print("\n a) Let it be")
    print(" b) End its suffering")
    chirp = input("\n Type either 'a' or 'b' for the following action: ")
    if chirp == "a":
        print("\n You let the bird be, watching it suffer as you walk away.")
    elif chirp == "b":
        print("\n You stomp on the bird with your foot quite hardly, killing it and putting it out of its misery.")
        print("\n You then continue on walking back to the camp.")
    elif chirp == "tell me who the killer is RIGHT NOW.":
        print("\n Okay, fine! It's Andrew. There, you happy?")
        print("\n Anyways, that's not a valid option, so please type either 'a' or 'b' next time.")
        bird()
    else:
        print("\n That is not a valid option. The prompt will now be repeated.")
        bird()
            
def walking():
    if cassandra_five > 0:
        cass()
    else:
        bird()
        
def comeback():
    print("\n After some time, you eventually return to the camp, seeing Hayden looking stressed.")
    print('\n "Erin! Where were you?!" Hayden screams.')
    if reye_died_early:
        print('\n "I was at the cliff looking for Reye after Ollie told me she disappeared, I after I fell down I saw her........ Dead," you tell Hayden.')
        print('\n "WHAT!?!?!?" Hayden screams.')
        print('\n You go silent.')
        print('\n "Did you... See the killer?!" Hayden asks.')
        print('\n "No... It was in the middle of the woods." you respond.')
        print('\n "Did it look like she died falling of the cliff?" Hayden then asks.')
        print('\n "Yeah," you respond.')
        print('\n Hayden then goes silent.')
        print('\n "Maybe... I do NOT want to have to say this... But maybe she.... Caused her own..." Hayden then says.')
        print('\n "Oh no..... After Juliet, it.... Kind of makes sense," you then say.')
        print('\n "It is either that or the killer was jealous about Reye and Juliet for whatever reason." Hayden then says.')
        print("\n You and Hayden then leave, as the situation had become quite sad.")
    else:
        print('\n "I was taking a walk at the cliff and saw Reye. I told her about what we saw on the cameras and she pushed me down the cliff," you tell Hayden.')
        print("\n Hayden then gasps.")
        print('\n "So... Reye tried to kill you?!" Hayden then says.')
        print('\n "Yeah, I guess," you reply.')
        print('\n "So.... What do we do?" Hayden then asks.')
        print('\n "I.... Am not sure," you respond honestly.')
        print("\n You and Hayden then leave, as the situation had become quite akward.")
        
def branch_two():
    if fates["Bob"] == "ALIVE":
        print("\n While walking back to your cabin, you see Bob, heading towards the exit of the camp..")
        if cassandra_hate >= 5:
            print('\n "Oh, hey Erin," Bob then says.')
            print('\n "Bob? Where are you going?" you ask.')
            print('\n "I just... I cannot do this anymore. The guilt of hitting a poor kid with a car...." Bob then says.')
            print('\n You then remember what had happened with Cassandra.')
            print('\n "I am leaving. I.... Need to rest. With my family. And plus, I do NOT want to be killed." Bob says.')
        else:
            print('\n "Oh, hi Erin!" Bob then says, happily.')
            print('\n "Hey Bob, where are you headed?" you ask.')
            print('\n "Well... You helped me realize something, Erin. I need more training in backflipping." Bob then says.')
            print("\n You then remember that earlier Bob was about to do a backflip but you warned him not to.")
            print('\n "I need to take more backflip lessons before I am ready. And plus, I do not want to be murdered," Bob explains.')
        print("\n You then watch as Bob gets in his car and drives off, leaving Camp Cottonwood.")
    else:
        print("\n While walking back to your cabin, you accidentally bump into Andrew. He then grabs his necklace instinctively.")
        print('\n "Oops, sorry," you say.')
        print("\n Staring at his necklace making sure it is okay, Andrew then walks off.")
        print('\n "Well, that was weird," you think.')
        
def branch_three():
    print("\n Around an hour passses, and you are just chilling in your cabin, extremely stressed from the case.")
    print("\n You then get a knock on the cabin door. It's Hayden.")
    if cassandra_five == 2:
        print('\n "Hey, I just wanted to warn you that Cassandra is in quite the mood." Hayden says.')
        print('\n "What do you mean?" you respond, remembering seeing her back in the forest.')
        print('\n "Well, apparently she spoke with Ollie and now she is thinking about stuff. So I just wanted to warn you about that," Hayden then says.')
        print('\n "Oh, okay. Well, thanks, I guess," you say.')
        print("\n Hayden then leaves.")
    elif cassandra_five == 1:
        print('\n "Erin, we have a situation. Like, a bad one. A REALLY, REALLY bad one." Hayden says.')
        print('\n "What is it?!" you ask nervously.')
        print('\n "Cassandra has been found dead." Hayden then says.')
        print('\n "WHAT?!?!" you scream.')
        print('\n "Yeah. Police said it was an animal attack far out in the woods." Hayden explains.')
        print("\n You then remember you decided to let Cassandra keep walking into the woods, which is why she out there in the first place.")
        print('\n "So what do we do?!?!?!" you say.')
        print('\n "Just... Do not worry. As I said I have already called the police, they can take it from here." Hayden then says.')
        print('\n "Alright, well, thanks for letting me know...." you say, horrified.')
        print("\n Hayden then leaves.")
    else:
        print('\n "Erin, we have a situation. Like, a bad one. A REALLY, REALLY bad one." Hayden says.')
        print('\n "What is it?!" you ask nervously.')
        print('\n "Cassandra has been found dead." Hayden then says.')
        print('\n "WHAT?!?!" you scream.')
        print('\n "Yeah. Police said it was a car crash. They have been trying to find who crashed the car, but no luck so far." Hayden explains.')
        print("\n You then remember the incident with Bob. You also remember him leaving earlier, likely explaining why the police hasn't caught him yet.")
        print('\n "So, what do we do?!?!?!" you say.')
        print('\n "Just... Do not worry. As I said I have already called the police, they can take it from here." Hayden then says.')
        print('\n "Alright, well, thanks for letting me know...." you say, horrified.')
        print("\n Hayden then leaves.")
        
def room():
    print("\n While sitting in your room, you feel useless, having nothing to do on your end until Hayden checked the other security cameras.")
    print("\n You then notice a few things could be done to clean up the room.")
    print("\n What do you do?")
    print("\n a) Clean up the bathroom")
    print(" b) Put all of the shoes in the shoe closet")
    print(" c) Tidy up your area and bed")
    print(" d) Ignore all of these problems")
    cleanup = input("\n Type either 'a', 'b', 'c', or 'd' for the corresponding action: ")
    if cleanup == "a":
        print("\n You clean up the bathroom, unfortunately having to endure it's horrible smell.")
    elif cleanup == "b":
        print("\n You place all of the shoes in the dedicated shoe closet. Now no one will slip on them.")
    elif cleanup == "c":
        print("\n You tidy up your area, realizing it's not your job to handle the other girls' messes.")
    elif cleanup == "d":
        print("\n You decide to ignore all of these problems, realizing you don't got time for that.")
    elif cleanup == "whoeverbuiltthisgameisanabsolutegenius":
        print("\n Why thank you!")
        print("\n Well, anyway, it hurts me to say that that's not a valid keyword. The prompt will now be repeated.")
        room()
    else:
        print("\n That is not a valid keyword. Please type either 'a', 'b', 'c', or 'd'. The prompt will now be repeated.")
        room()
        
def crush():
    global loca
    global hayden_fate
    print("\n A little bit later, you are near your cabin, walking around when Hayden walks up to you.") 
    print('\n "Oh, there you are, Erin," Hayden says.')
    print('\n "Oh, hey, what is going on?" you reply.')
    print('\n "So... I know this may be a weird time, but there is something I have been wanting to tell you." Hayden then says.')
    print('\n "Alright, what is it?" you ask.')
    print('\n "I know we are investigation partners... But I like you more than that. I do not know if you feel the same way, but..." Hayden says.')
    print("\n What do you do?")
    print("\n a) Say yes")
    print(" b) Reject Hayden")
    cruhsh = input("Type either 'a' or 'b' for the following decision: ")
    if cruhsh == "a":
        hayden_fate += 1
        print('\n "I... I feel the same way," you tell Hayden.')
        print('\n Hayden smiles and giggles, happily. They then grab your hand.')
        print("\n You two then walk off together, glad to have found a little happiness in this mess.")
    elif cruhsh == "b":
        loca = "b"
        print('\n "Hayden, I think you are a great friend, but... I do not feel the same way." you say honestly.')
        print("\n Hayden then looks down at their shoes, dejected.")
        print("\n You two then go your separate ways, as it had become quite awkward.")
    else:
        print("\n That is not a valid option. The prompt will now be repeated.")
        crush()

def second():
    global loca
    print("\n A little bit later, you are walking around. It's strangely calm and peaceful.")
    print("\n You walk over to the center of the campus, where on the ground, you see someone lay.")
    print('\n "NO......................" you think.')
    print("\n The person has a knife in their chest.")
    print("\n It's Hayden.")
    print("\n What do you do?")
    print("\n a) Follow the trail of blood")
    print(" b) Run away")
    death = input("\n Type either 'a' or 'b' for the following choice: ")
    if death == "a":
        loca == "c"
        print("\n You boldly choose to follow the trail of blood, having no idea where it could lead to.")
    elif death == "b":
        loca == "d"
        print("\n You run away as fast as you can, going as far away as possible.")
    else:
        print("\n That is not a valid option. The prompt will now be repeated.")
        second()
        
def branch_four():
    global hayden_fate
    if hayden_like >= 4:
        hayden_fate += 1
        crush()
    else:
        second()
        
def branch_five():
    if loca == "a":
        print("\n You keep walking with Hayden, happy to be together.")
        print("\n 'Alright, I am going to head out now, see you later!' Hayden says happily.")
        print("\n You then wave goodbye and head on out.")
        print("\n Suddenly, as you are walking back to your cabin, someone grabs you. They cover your eyes and mouth as your vision fades to black.")
    elif loca == "b":
        print("\n You then head back to your cabin.")
        print("\n As you're walking, someone suddenly grabs you. They cover your eyes and mouth as your vision fades to black.")
    elif loca == "c":
        print("\n You walk down the path created by the blood, terrified.")
        print("\n Suddenly, someone grabs you. They cover your eyes and mouth as your vision fades to black.")
    else:
        print("\n As you run, you eventually hear footsteps behind you. You realize someone is chasing you.")
        print("\n Before you can look back to see who it is, they grab you, covering your eyes and mouth. Your vision then fades to black.")
        
def wakeup():
    print("\n As your vision comes back to you, you are horrified by what you see.")
    print("\n In your own, bloody hands, you have a pole. On the ground, lays Ollie, completely beat up.")
    print('\n "OLLIE!??!!" you scream.')
    print("\n He doesn't say anything.")
    print("\n What do you do?")
    print("\n a) Help Ollie")
    print(" b) Run")
    wakiewakie = input("\n Type either 'a' or 'b' for the following decision: ")
    if wakiewakie == "a":
        print("\n You drop the pole in terror and help Ollie up. You carry him away as he bleeds and bleeds.")
    elif wakiewakie == "b":
        fates["Ollie"] = "DEAD"
        print("\n You drop the pole in terror and spring away in fear, at a loss for words. As you look back, you watch as Ollie dies.")
    else:
        print("\n That is not a valid response. The prompt will now be repeated.")
        wakeup()
        
def passby():
    print("\n As you are walking, you see a car pass by.")
    print('\n "HEY!" you scream, waving over to it.')
    print("\n The car then stops. It's Lune.")
    print('\n "Erin? Your hands are SUPER bloody, are you okay!?"')
    if fates["Ollie"] == "DEAD":
        print("\n You look down at your hands, remembering what had just happened.")
        print('\n "Erin, WHAT IS GOING ON?!" Lune then asks.')
    else:
        print("\n You then reveal Ollie to Lune.")
        print('\n "WHA- NO, NO.... NO!!!!" Lune then says.')
    print("\n What do you say?")
    print('\n a) "Lune, go warn the others!"')
    print(' b) "Lune, please help me!"')
    passing = input("\n Type either 'a' or 'b' for the corresponding thing to say: ")
    if passing == "a":
        print('\n "Lune, go warn the others!" you say.')
        print('\n "Ar- are you sure??" Lune asks.')
        print('\n "YES, I AM! NOW GO!" you say confidently.')
        print("\n Lune then reluctantly drives off, following your request.")
    elif passing == "b":
        fates["Lune"] = "DEAD"
        print('\n "Lune, please help me!" you say desperately.')
        print('\n "Okay, get in!" Lune tells you, unlocking the door to the back side of the car.')
        print("\n You then get into the car. Lune then frantically drives off.")

def branch_six():
    if fates["Ollie"] == "DEAD" and fates["Lune"] == "DEAD":
        print("\n Lune drives as you sit in the back of the car, feeling extremely guilty for leaving Ollie behind. You suspect he has most likely died from blood loss already.")
        print("\n Just as you begin calming down, Lune screams.")
        print('\n "WHAT IN THE-"')
        print("\n You look up, and see a shadowed figure. Lune turns a bit too quickly, trying to avoid hitting them.")
        print('\n "BRACE FOR IMPA-"')
        print("\n The car then crashes. As your vision fades back, you see Lune's dead body sitting right next to you.")
        print('\n "OH NO," you scream.')
        print("\n Quickly, you get out of the car and run into the forest, trying to escape the shadowed figure.")
    elif fates["Ollie"] == "ALIVE" and fates["Lune"] == "DEAD":
        print("\n You use a spare shirt Lune had to cover up Ollie's injuries as Lune frantically drives.")
        print("\n But just as everything begins calming down, Lune screams.")
        print('\n "WHAT IN THE-"')
        print("\n You look up, and see a shadowed figure. Lune turns a bit too quickly, trying to avoid hitting them.")
        print('\n "BRACE FOR IMPA-"')
        print("\n The car then crashes. As your vision fades back, you see Lune's dead body sitting right next to you.")
        print('\n "OH NO," you scream.')
        print("\n Luckily, with you and Ollie being in the back, you two weren't hit too badly.")
        print("\n Quickly, you open the door to the car, grab Ollie's body and run into the forest, trying to escape the shadowed figure.")
    elif fates["Ollie"] == "DEAD" and fates["Lune"] == "ALIVE":
        print("\n After Lune drives off, you make your way back over to camp, feeling really guilty about leaving Ollie behind. You suspect he has most likely died from blood loss already.")
        print("\n After a lot of walking, you eventually see someone.")
        print('\n "Who is that?" you think.')
        print("\n But as you look closer, you realize it was the shadowed figure from earlier.")
        print('\n "Ohhhhhhhh no," you think.')
        print("\n The figure then notices you. You then rush into the forest, trying to escape them.")
    else:
        print("\n After Lune drives off, you make your way back over to camp, carrying Ollie on the way. You covered up his injuries with a shirt you found laying around.")
        print("\n After a lot of walking, you eventually see someone.")
        print('\n "Who is that?" you think.')
        print("\n But as you look closer, you realize it was the shadowed figure from earlier.")
        print('\n "Ohhhhhhhh no," you think.')
        print("\n The figure then notices you. You then rush into the forest, still carrying Ollie, trying to escape them.")

def quick():
    print("\n As you are running, you see Ben walking in the forest.")
    if fates["Ollie"] == "DEAD":
        print('\n "Erin? What is going on?" he asks.')
    else:
        print('\n "WHA- WHAT HAPPENED TO OLLIE?!!" he screams.')
    print("\n Ben then backs up, afraid.")
    print("\n What do you do?")
    print("\n a) Tell Ben to run")
    print(" b) Tell Ben to hide")
    ben = input("\n Type either 'a' or 'b' for the corresponding decision: ")
    if ben == "a":
        print('\n "BEN, RUN!!!" you scream.')
        print("\n Ben then turns around and runs. The two of you run together from the shadowed figure, who you think you have lost, but are not sure.")
    elif ben == "b":
        fates["Ben"] == "DEAD"
        print('\n "Ben, hide," you whisper.')
        print("\n You and Ben then hide behind a tree as the shadowed figure runs in.")
        print('\n "You can run but you cannot hide," they say.')
        print("\n As you hear this, you make a run for it, but Ben is too late. As you run, you hear Ben scream.")
    else:
        print("\n That is not a valid keyword. Please type either 'a' or 'b'. The prompt will now be repeated.")
        quick()

def reye():
    print("\n After looking around the theater, you see Reye.")
    print('\n "Oh, E- Er- Erin.." she says, feeling a bit akward after having attempetd to kill you earlier.')
    print("\n Suddenly, the shadowed figure comes back in. They then grab Reye. Reye screams as the person turns the corner with her in their arms.")
    print("\n You turn the corner, but it's too late. Reye is already lying on the floor, bleeding out. The shadowed figure then runs away.")
    print("\n You look down at Reye. She is groaning in pain, very clearly suffering immense pain.")
    print('\n "E- Er- Erin... Pl- please... Just... End my pain..." Reye says.')
    print("\n What do you do?")
    print("\n a) End Reye's suffering")
    print(" b) Leave her to die")
    pain = input("\n Type either 'a' or 'b' for the following decision: ")
    if pain == "a":
        print('\n "Oh... Okay," you tell Reye.')
        print("\n You walk up to Reye, close your eyes, and do what she asked for. You then get up, trying to forget what had just happened.")
        print("\n You then see the shadowed figure in the distance and chase them.")
    elif pain == "b":
        print("\n You look at Reye in digust. After all, she did try to kill you earlier.")
        print("\n You then walk straight past her, completely ignoring her pain.")
        print("\n You then see the shadowed figure in the distance and chase them.")
    else: 
        print("\n That is not a valid option. Please type either 'a' or 'b'.")
        reye()

def adrenaline():
    if fates["Ben"] == "ALIVE":
        print("\n Eventually, you and Ben reach back, having lost the shadowed figure.")
        print('\n "I will go look for help. You check the theater!" Ben says, running off.')
        print("\n As Ben suggested, you run into the theater, looking for help.")
    else:
        print("\n Eventually, you reach back, having lost the shadowed figure.")
        print("\n You run into the theater, trying to find someone or some way to call the police.")
    if fates["Ollie"] == "ALIVE":
        print("\n You place Ollie on one of the couches and cover him with a blanket, letting him rest. You then look around the theater.")
    if reye_died_early:
        print("\n After some time looking around the theater, you see the shadowed figure in the distance. You then chase after them as they run away.")
    else:
        reye()

def somehow():
    global cassandra_five
    print("\n As you chase the shadowed figure, you eventually see Cassandra walk by.")
    print('\n "OH MY-"')
    print("\n The shadowed figure crashes into Cassandra. They then beat her up really badly, especially her left leg, clearly trying to kill her. Just as you catch up, they run off.")
    print('\n "Erin... Keep... Chasing..." Cassandra says, in extreme pain.')
    print("\n The theater is very close. You could get Cassandra there, but you may lose the shadowed figure.")
    print("\n What do you do?")
    print("\n a) Help Cassandra")
    print(" b) Keep chasing the figure")
    gameover = input("\n Type either 'a' or 'b' for the corresponding decision: ")
    if gameover == "a":
        cassandra_five += 1
        print("\n You help Cassandra, dragging her over to the theater.")
        print("\n Once inside, you get Cassandra on one of the couches.")
        print('\n "It is fine, I can look for something for my leg. Just keep chasing them!" Cassandra says.')
        print("\n You nod, heading out to keep chasing the figure.")
        print("\n But once you step out, you see that the shadowed figure is nowhere to be seen. But they couldn't have gone far.")
    elif gameover == "b":
        print("\n You nod to Cassandra, and chase after the shadowed figure.")
        print("\n You keep chasing them until eventually you slowly start losing them.")
        print('\n "NO!!!" you think.')
        print("\n Eventually, after triping on a rock, you completely lose them. But it's only been a few seconds, so they couldn't have gone far.")
    else:
        print("\n Sorry, but that is not a valid keyword. The prompt will now be repeated.")
        somehow()

def chase():
    print("\n You keep on chasing the shadowed figure, slowly and slowly getting more tired.")
    if cassandra_five == 2:
        somehow()
    else:
        print("\n After a bunch of chasing, you eventually lose the shadowed figure. But they couldn't have gone far.")

def area_finale():
    global collectibles
    global final_area_one
    global final_area_two
    global final_area_three
    global final_area_four
    print("\n Below is a list of things you can check. Find the shadowed figure.")
    while True:
        print("")
        if final_area_one:
            print(" 1) Around the corner")
        if final_area_two:
            print(" 2) Back in the theater")
        if final_area_three:
            print(" 3) In the trash bin")
        if final_area_four:
            print(" 4) The stairs to the roof of the theater")
        farea = input("Type a number 1-4 for the corresponding place to check: ")
        if farea == "4":
            print("\n You check the stairs to the roof and see the shadowed figure running up.")
            print("\n Congratulations: you have tracked down the shadowed figure. You follow them up to the roof of the theater.")
            break
        elif farea == "3":
            if final_area_three:
                print("\n You open the trash bin to see if the shadowed figure is hiding there. Nothing.")
            else:
                print("\n You have already checked the trash bin. The shadowed figure is not there.")
            final_area_three = False
        elif farea == "2":
            if final_area_two:
                print("\n You quicky look back in the theater just to make sure the shadowed figure isn't there. Nothing.")
            else:
                print("\n You have already checked back in the theater. The shadowed figure is not there.")
            final_area_two = False
        elif farea == "1":
            if final_area_one:
                collectibles += 1
                print("\n You check around the corner for the shadowed figure, but they aren't there. However, you see a TV laying on the ground.")
                print("\n Congratulations: you have found a Collectible item. You place the TV back into the box laying next to it and close the box.")
            else:
                print("\n You have already checked around the corner. The shadowed figure is not there.")
            final_area_one = False
        else:
            print("Sorry, but that is not a valid number from 1 to 4.")


def finale_one():
    global collectibles
    print("\n You chase the shadowed figure up to the top of the roof. And that's it.")
    print('\n "STOP! You know it is over. We have already called the police!" you say, bluffing.')
    print("\n Though in hindsight, it probably would have just been easier to find a phone and call the police.")
    print('\n "Fine," the shadowed figure says, taking off their mask.')
    print("\n It's Andrew.")
    print('\n "It has been me doing all of this." Andrew says.')
    print("\n You nod in fear.")
    print('\n "Whelp, since I have lost, I may as well give you an explanation." Andrew then says.')
    print('\n "That, literally makes no se-"')
    print('\n "So recently, I learned hypnosis. Remember when I chased you earlier and when you woke up you had attacked Ollie? Yep, that was me. But at first, it was innocent. Just for fun. But then, I realized I could use it for my revenge. See, me and Cassandra used to be friends. Best friends. But being the horrible person she is, she turned on me one day. Suddenly, the Camp Cottonwood that I loved turned into a place I had to see Cassandra. So when I realized her character was going to die in the musical through drain cleaner, I thought it would be the perfect oppurtunity to poison her. Even though it would have just looked like an accident with real drain cleaner instead of fake drain cleaner, I took a precaution, and made you do it by hypnotization. I made you place the drain cleaner on the stage. If you ever checked the cameras, you would have seen that. It almost worked, except for the fact that Juliet had subbed-in for Cassandra that day, killing her instead. As for all the other bad things I did, I did them to attempt to not get caught. Any questions?" Andrew says.')
    print("\n What do you say or do?")
    print('\n a) "You hated Cassandra... THAT MUCH??"')
    print(' b) "Where could you have possibly learned hypnosis??"')
    print(' c) "YOU ARE CRAZY, ANDREW!!!!"')
    print(' d) Grab his necklace so he cannot hypnotize you"')
    necklace = input("\n Type either 'a', 'b', 'c' or 'd' for following decision: ") 
    if necklace == "a":
        print('\n "You hated Cassandra... THAT MUCH??" you scream.')
        print('\n "She RUINED my favorite place in the world! She ruined everything!!!" Andrew screams back.')
    elif necklace == "b":
        print('\n "Where could you have possibly learned hypnosis??" you ask concerned.')
        print('\n "I have my ways..." he responds cryptically.')
    elif necklace == "c":
        print('\n "YOU ARE CRAZY, ANDREW!!!!" you scream.')
        print('\n "None of this would have happened if it were not for Cassandra. SHE IS THE CRAZY ONE!!" Andrew screams back.')
    elif necklace == "d":
        print("\n You grab Andrew's necklace before he can hypnotize you.")
        print("\n Congratulations: you have found a Collectible item. You keep it in your pocket before Andrew can grab it back.")
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        finale_one()


def finale_two():
    print("What do you choose to do now?")
    print("\n a) Grab Andrew's phone and call the cops")
    print(" b) Push Andrew off the ledge")
    fin = input("\n Type either 'a' or 'b' for the following decision: ")
    if fin == "a":
        keep_andrew()
    elif fin == "b":
        fates["Andrew"] = "DEAD"
        push_andrew()
    else:
        print("\n That is not a valid keyword. The prompt will now be repeated.")
        finale_two()

def keep_andrew():
    print("\n You grab Andrew's phone and quickly dial 911. You figure that he won't bother doing anything as he's already lost.")
    print("\n But, suddenly, Andrew lunges at you and grabs you.")
    print('\n "SHOOT!" you scream.')
    print('\n "HAHAHAHAHAHA, WHAT ARE YOU GOING TO DO NOW, ERIN?!" he says egotistically.')
    print("\n What do you do?")
    print("\n a) Nothing")
    print(" b) Punch his face")
    erindies = input("\n Type either 'a' or 'b' for the following decision: ")
    if erindies == "a":
        fates["Erin"] == "DEAD"
        print("\n You choose to do nothing.")
        print('\n You gave up too easily..." Andrew says evily."')
        print("\n Andrew then throws you off the ledge. You then begin falling to your death.")
    elif erindies == "b":
        print("\n You punch Andrew straight in the face. He then falls down to the floor.")
        print('\n "OWWWW!!!!!!" Andrew screams.')
        print("\n While he's down, you slam your leg into him, making sure he doesn't get up. You then call the police.")
        survival()
    else:
        print("\n That is not a valid keyword. Please type either 'a' or 'b'. The prompt will now be repeated.")
        keep_andrew()

def push_andrew():
    print("\n You quickly lunge at Andrew and push him off the ledge.")
    print('\n Andrew then screams in shock.')
    print("\n But at the last moment, he grabs your arm while he's falling.")
    print('\n "If I die, you die with me!" he then says like a comic book villain.')
    print("\n As you're both falling, you grab onto the edge of the building.")
    print("\n Now, you're hanging off the edge of the building with Andrew grabbing your leg from below.")
    print("\n What do you do?")
    print("\n a) Shake him off")
    print(" b) Let go")
    andrewdies = input("Type either 'a' or 'b' for the corresponding action: ")
    if andrewdies == "a":
        print("\n You start trying to shake Andrew off of you.")
        print("\n Eventually, it works.")
        print('\n "NOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!" Andrew screams as he falls to his death.')
        print("\n You then climb back up to the top of the building.")
        survival()
    elif andrewdies == "b":
        fates["Erin"] == "DEAD"
        print("\n You let go of the ledge.")
        print('\n "YOU FOOL!!!!!!!!" Andrew screams.')
        print('\n "What? You got what you wanted." you say, remembering his previous words.')
        print("\n You both then fall to your deaths.")

def survival():
    print("\n The next day, you wake up, ready to leave Camp Cottonwood.")
    if fates["Andrew"] == "ALIVE":
        print("\n Yesterday, the police eventually came and arrested Andrew. You suspect that you are not going to see him for a long time.")
    else:
        print("\n Yesterday, you eventually called the police, but they didn't get you in trouble as not only did you murder a murderer which is a gray area but he most likely would have murdered you if you didn't do what you did. Or at least that's what you told the police.")
        print("\n You grab your bag and head out of your cabin.")

    if cassandra_five == 0:
        print("\n On your way to the bus, you remember Cassandra, who died in a car crash with Bob. You remember how she never got the chance to change and how Andrew ended up getting what he wanted in a way.")
    elif cassandra_five == 1:
        print("\n On your way to the bus, you remember Cassandra, who died in an animal attack in the woods. You remember how she never got the chance to chance and Andrew ended up getting what he wanted in a way.")
    elif cassandra_five == 2:
        print("\n On your way to the bus, you see Cassandra. She has crutches.")
        print('\n "Oh, hey Erin," Cassandra says.')
        print('\n "Hey, how is your leg doing?" you ask.')
        print('\n "It still hurts a lot, but it is defenitely getting better." Cassandra replies.')
        print('\n "Well, that is good to hear, at least," you respond.')
        print('\n "Yeah. But hey, you made the right chocice. If you stayed to help me then Andrew could have gotten away." Cassandra then says.')
        print('\n "Thanks," you say.')
        print('\n "Of course," Cassandra says, walking off.')
        print("\n You two are about to split ways when she stops.")
        print('\n "Oh, wait. I am sorry for everything I did. I am very sorry. I am going to try to be better. I was so bad that... Someone tried to kill me. I will change, I promise," Cassandra says.')
        print("\n Cassandra then leaves.")
    else:
        print("\n On your way to the bus, you see Cassandra.")
        print('\n "Oh, hey Erin!" she says.')
        print('\n "Oh, hi Cassandra!" you respond.')
        print('\n "Thank you so much for helping me back there. My leg would not have been okay if you did not help me." Cassandra says.')
        print('\n "Yeah, of course," you tell her.')
        print('\n "And also, I am sorry for everything I did. I am very sorry. I am going to try to be better. I was so bad that... Someone tried to kill me. I will change, I promise," Cassandra then says.')
        print("\n Cassandra then leaves.")

    if hayden_fate == 0:
        print("\n You then think about Hayden, and how they tragically died because of Andrew.")
    elif hayden_fate == 1:
        print("\n You then see Hayden while you are walking, and remember that you rejected them.")
        print('\n "Have a good rest of your summer, Erin," Hayden says, not making eye contact.')
        print('\n "You too," you say as they walk off.')
    else:
        print("\n You then see Hayden while you are walking.")
        print('\n "Erin! I am really glad you are okay," they say, hugging you.')
        print("\n You hug them back.")
        print('\n "Thanks. And you too. Who knows what could have happened," you respond.')
        print('\n "Whelp, my parents are waiting for me. Have a good rest of your summer!" Hayden says to you.')
        print('\n "You too! Bye!" you say.')
        print("\n Hayden then walks off.")

    if fates["Ollie"] == "ALIVE" and fates["Ben"] == "ALIVE":
        print("\n As you reach the bus, you see Ben helping Ollie get on.")
        print('\n "Hey guys! Ollie, I am glad to see you are healing," you say.')
        print('\n "Thanks, Erin. And thank you so much for helping me. I would have died without you." Ollie then says.')
        print('\n "Of course," you tell Ollie.')
        print("\n You, Ollie and Ben then get into the bus.")
    elif fates["Ollie"] == "ALIVE" and fates["Ben"] == "DEAD":
        print("\n As you reach the bus, you see Ollie struggling to get on.")
        print('\n "Here, let me help you," you say.')
        print('\n "Oh, thanks! And thanks a lot for helping me earlier. I would have died without you." Ollie then says.')
        print('\n "Of course," you tell Ollie.')
        print("\n You and Ollie then get on the bus.")
    elif fates["Ollie"] == "DEAD" and fates["Ben"] == "ALIVE":
        print("\n As you reach the bus, you see Ben walking on.")
        print('\n "Hey Ben," you say.')
        print('\n "Oh, hey Erin," Ben says.')
        print("\n You and Ben then climb onto the bus.")
    else:
        print("\n As you reach the bus, you see no one walking on.")
        print("\n You remember people like Ben and Ollie who would have been here if they were alive.")
        print("\n You then get onto the bus, trying to push these negative thoughts to the side.")

    if mom_text:
        print("\n As you get onto the bus, the bus driver notices you.")
        print('\n "Oh, not this kid again! Please get off the bus on time this time. I do not care if you get a text from your mom." the bus driver then says.')
    else:
        print("\n As you get onto the bus, the bus driver notices you.")
        print('\n "Oh, you are the kid who ignored the text her mom sent to get off the bus in time. Respect," the bus driver then says.')

    print("\n As you go to the back of the bus, only one thought races your mind.")
    print('\n "I will probably be back here someday. But hopefully not."')


def stats():
    print("")
    print("\t Congratulations: you have officially finished the Killer Performance game! Below some stats regarding the choices you made throughout the game.")

    print("\n What did Juliet do in her final moments?")

    if juliet_final_words >= 2:
        print("\n Juliet tried to reach for your help in her final moments (1 in 3 playthroughs).")
    elif juliet_final_words == 1:
        print("\n Juliet smiled at you in her final moments (1 in 3 playthroughs).")
    else:
        print("\n Juliet looked at the wall blankly in her final moments (1 in 3 playthroughs).")

    print("\n How did Reye end up dying?")

    if reye_died_early:
        print("\n Reye fell off the cliff after Juliet died (1 in 2 playthroughs).")
    else:
        print("\n Reye was killed by Andrew in his final rampage (1 in 2 playthroughs).")

    print("\n What was Hayden's final fate?")

    if hayden_fate == 0:
        print("\n Hayden was killed by Andrew (1 in 3 playthroughs).")
    elif hayden_fate == 1:
        print("\n Hayden survived but was rejected by you (1 in 3 playthroughs).")
    else:
        print("\n Hayden was your romantic partner (1 in 3 playthroughs).")

    print("\n What was Cassandra's final fate?")

    if cassandra_five == 0:
        print("\n Cassandra died in a car crash with Bob (1 in 4 playthroughs).")
    elif cassandra_five == 1:
        print("\n Cassandra died in an animal attack (1 in 4 playthroughs).")
    elif cassandra_five == 2:
        print("\n Cassandra survived but had a leg injury (1 in 4 playthroughs).")
    else:
        print("\n Cassandra survived with a healthy body thanks to you (1 in 4 playthroughs).")

    print("\n What was the fate of every other determinant character?")

    print("")
    for i in fates:
        print(f"{i}: {fates[i]}")
    print("(1 in 64 playthroughs).")

    print("\n How many collectibles did you find?")

    if collectibles == 0 or collectibles == 7:
        print(f"\n You found {collectibles} / 7 collectibles (3072 out of 396,216 possible playthroughs).")
    elif collectibles == 1 or collectibles == 6:
        print(f"\n You found {collectibles} / 7 collectibles (21,504 out of 396,216 possible playthroughs).")
    elif collectibles == 2 or collectibles == 5:
        print(f"\n You found {collectibles} / 7 collectibles (64,512 out of 396,216 possible playthroughs).")
    elif collectibles == 3 or collectibles == 4:
        print(f"\n You found {collectibles} / 7 collectibles (107,520 out of 396,216 possible playthroughs).")
    if collectibles == 7:
        print("\n As a reward for finding all 7 collectibles, here is how find one of the few secret codes throughout the game: You must choose to reply to your mom's text on the bus at the start of the game, and when it asks you what you want to reply with, type '#6767420gummywormsforlifelolxd'")

    print("\n And that's it! Thank you for playing. I hope you enjoyed the game!")


def game():
    bus()
    text()
    area_camp()
    bunk()
    ori()
    argue()
    time()
    before()
    area_prep()
    nervous()
    area_audition()
    scream()
    inout()
    cast()
    crashout()
    date()
    rehearsal()
    area_crime()
    cops()
    area_find()
    footage()
    branch_one()
    see()
    bracelets()
    watching()
    defense()
    after()
    area_forest()
    walking()
    comeback()
    branch_two()
    branch_three()
    room()
    branch_four()
    branch_five()
    wakeup()
    passby()
    branch_six()
    quick()
    adrenaline()
    chase()
    area_finale()
    finale_one()
    finale_two()
    stats()
    
open_message()