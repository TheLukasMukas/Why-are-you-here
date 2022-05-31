import sys
import time
import random
s = 0
print("Well...")
time.sleep(2)
print("the God sent you here, I had nothing to do with this")
for i in range(4):
    print(".")
    time.sleep(0.6)
print("I guess neither of us want to be here...")
time.sleep(1.75)
print("Especially not me with you...")
time.sleep(1.75)
print("Why do I always get the scraps, ugly people like you")
time.sleep(1.75)
for i in range(4):
    print(".")
    time.sleep(0.6)
time.sleep(1.25)
print("Oh that hwat youw feewilng, I dont care, get used to it")
time.sleep(2)
print("I just can't look at you")
for i in range(4):
    print(".")
    time.sleep(0.6)
time.sleep(1.75)
print("You know what, I will make you an offer.")
time.sleep(1.75)
a = input("Do you want to hear it?")
if a == "yes":
    print("I will ask you a few questions, based on your answers you might go to paradise.")
    time.sleep(2)
    b = input("Does that sound good?")
    if b == "yes":
        print("OK, let's start")
        time.sleep(1.75) 
        print("FIRST QUESTION. You pass someone in the street who is in severe need and you are able to help them at little cost to yourself.")
        time.sleep(2)
        c = input("Are you morally obliged to do so?")
        if c == "yes":
            s1 = s + 10
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("OK, intresting choice")
        if c == "no":
            s1= s-0
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("My answer was the same")
        for i in range(4):
                print(".")
                time.sleep(0.6)
        print("SECOND QUESTION. You have a brother. You know that someone has been seriously injured as a result of criminal activity undertaken by him.")
        time.sleep(2)
        print("You live in a country where the police are generally trustworthy.")
        time.sleep(2)
        d = input("Are you morally obliged to inform them about your brother's crime?")
        if d == "yes":
            s2=s1+10
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("You don't fit here kid")
        if d == "no":
            s2=s1-0
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("You might fit here well")
        for i in range(4):
                print(".")
                time.sleep(0.6)
        print("THIRD QUESTION. You are able to help some people. Unfortunately, you can only do so by harming other people.")
        time.sleep(2)
        print("The number of people harmed will always be 10 percent of those helped.")
        time.sleep(2)
        print("When considering whether it is morally justified to help does the actual number of people involved make any difference?")
        time.sleep(2)
        e = input("For example, does it make a difference if you are helping ten people by harming one person rather than helping 100,000 people by harming 10,000 people?")
        if e == "yes":
            s3=s2-0
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("I can't agree nor disagree with you on that one")
        if e == "no":
            s3=s2+10
            for i in range(4):
                print(".")
                time.sleep(0.6)
            print("I can't agree nor disagree with you on that one")
        for i in range(4):
                print(".")
                time.sleep(0.6)
        print("FOURTH QUESTION. Someone you have never met needs a kidney transplant. You are one of the few people who can provide the kidney.")
        f=input("Would any moral obligation to provide the kidney be greater if this person was a cousin rather than a non-relative?")
        if f == "yes":
            s4=s3+10
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("Sure, that makes sense")
        if f == "no":
            s4=s3-0
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("Why were you even sent here?")
        for i in range(4):
                print(".")
                time.sleep(0.6)
        print("FINAL QUESTION. You can save the lives of ten innocent people by killing one other innocent person.")
        g = input("Are you morally obliged to do so?")
        if g == "yes":
            s5=s4-0
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("Alright, noted")
        if g == "no":
            s5=s4+10
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(1.5)
            print("Lets check the results, you pudding of a person")
        for i in range(4):
                print(".")
                time.sleep(0.6)
        print("And the results are...")
        time.sleep(1)
        print("🥁Drum roll please🥁")
        for i in range(4):
                print(".")
                time.sleep(0.6)
        if s5 > 25:
            print("YOU CAN THANKFULLY GO TO PARADISE")
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(2)
            print("PARADISE, the GOD is talking")
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(2)
            print("You are in paradise my child, you can live here peacefully")
            time.sleep(2)
            for i in range(4):
                print(".")
                time.sleep(0.6)
            time.sleep(2)
            h=input("Will you be good?")
            if h=="no":
                time.sleep(2)
                for i in range(4):
                    print(".")
                    time.sleep(0.6)
                print("* 3 years later *")
                for i in range(4):
                    print(".")
                    time.sleep(0.6)
                print("My child you were very bad, I must send you to hell")
                for i in range(4):
                    print(".")
                    time.sleep(0.6)
                i=input("* Will you beg for forgivness? *")
                if i == "yes":
                    time.sleep(2)
                    print("* The God didn't accept your apologie *")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    time.sleep(2)
                    print("* HELL, the Satan is speaking *")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    time.sleep(2)
                    print("NOT YOU AGAIN")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    print("* ⛤ You goofed up, It's over for you ⛤ *")
                    time.sleep(2)
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    print("Credits")
                    time.sleep(1.5)
                    print("Directed by Luka")
                    time.sleep(1.5)
                    print("Story by Luka")
                    time.sleep(1.5)
                    print("Coded by Luka")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    print("THANKS FOR PLAYING")
                    input('Press ENTER to exit')
                if i == "no":
                    time.sleep(2)
                    print("Okay, back to hell you go")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    time.sleep(2)
                    print("* HELL, the Satan is speaking *")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    time.sleep(2)
                    print("NOT YOU AGAIN")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    time.sleep(2)
                    print("* ⛤ You goofed up, It's over for you ⛤ *")
                    time.sleep(2)
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    print("Credits")
                    time.sleep(1.5)
                    print("Directed by Luka")
                    time.sleep(1.5)
                    print("Story by Luka")
                    time.sleep(1.5)
                    print("Coded by Luka")
                    for i in range(4):
                        print(".")
                        time.sleep(0.6)
                    print("THANKS FOR PLAYING")
                    input('Press ENTER to exit')
            if h=="yes":
                time.sleep(2)
                for i in range(4):
                    print(".")
                    time.sleep(0.6)
                print("* 3 years later *")
                for i in range(4):
                        print(".")
                        time.sleep(0.6)
                print("My child you were really good in the last few years")
                time.sleep(1)
                j=input("So you remember that time you were in hell?")
                if j=="yes":
                    time.sleep(1)
                    print("So I wanted to give you one job, of course it's down to you will you accept it")
                    time.sleep(1.2)
                    k=input("I know it's a bit sudden, but will you slay the Satan for me?")
                    if k=="yes":
                        time.sleep(2)
                        print("OK, I'm sending you to hell, just do it quickly, here, slay him with this")
                        for i in range(4):
                            print(".")
                            time.sleep(0.6)
                        time.sleep(2)
                        print("* You obtained THE CROSS *")
                        time.sleep(2)
                        for i in range(4):
                            print(".")
                            time.sleep(0.6)
                        print("HELL, the Satan is speaking")
                        time.sleep(2)
                        for i in range(4):
                            print(".")
                            time.sleep(0.6)
                        print("I honestly hoped I would never see you again, so why are you here?")
                        time.sleep(1.2)
                        l = input("* Will you tell him that the God sent you *")
                        if l == "no":
                              m=input("* Will you kill him? *")
                              if m =="no":
                                    print("* ⛤The Satan consumed your soul for taking too long to answer⛤ *")
                                    time.sleep(2)
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("Credits")
                                    time.sleep(1.5)
                                    print("Directed by Luka")
                                    time.sleep(1.5)
                                    print("Story by Luka")
                                    time.sleep(1.5)
                                    print("Coded by Luka")
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("THANKS FOR PLAYING")
                                    input('Press ENTER to exit')
                              if m =="yes":
                                     for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                     print("* You slayed the Satan with THE CROSS *")
                                     for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                     n = input("* Will you overtake the Hell? *")
                                     if n=="yes":
                                          for i in range(4):
                                            print(".")
                                            time.sleep(0.6)
                                     print("* The God is mad and supprised by your decison... *")
                                     time.sleep(2)
                                     print("* The God send an angel army on hell, the Holy War startted, just like the scripts have forsoken...")
                                     time.sleep(2)
                                     for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                     print("Credits")
                                     time.sleep(1.5)
                                     print("Directed by Luka")
                                     time.sleep(1.5)
                                     print("Story by Luka")
                                     time.sleep(1.5)
                                     print("Coded by Luka")
                                     for i in range(4):
                                         print(".")
                                         time.sleep(0.6)
                                     print("THANKS FOR PLAYING THIS GAME, PART 2 COMING OUT SOON")
                                     input('Press ENTER to exit')
                              if l =="yes":
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("Hmmmm, I knew this would happen one day, so he sent you with that thing to slay me")
                                    time.sleep(1.2)
                                    print("I'm sending an army right now, I want you to be me my right hand, the Holy War will start, we will get along well....")
                                    time.sleep(2)
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("Credits")
                                    time.sleep(1.5)
                                    print("Directed by Luka")
                                    time.sleep(1.5)
                                    print("Story by Luka")
                                    time.sleep(1.5)
                                    print("Coded by Luka")
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("THANKS FOR PLAYING THIS GAME, PART 2 COMING OUT SOON")
                                    input('Press ENTER to exit')
                if j == "no":
                    print("Don't lie to me, I know everything....")
                    time.sleep(1)
                    print("So I wanted to give you one job, of course it's down to you will you accept it")
                    time.sleep(1.2)
                    k=input("I know it's a bit sudden, but will you slay the Satan for me?")
                    if k=="yes":
                        print("OK, I'm sending you to hell, just do it quickly, here, slay him with this")
                        time.sleep(1)
                        print("* You obtained THE CROSS *")
                        for i in range(4):
                            print(".")
                            time.sleep(0.6)
                        print("HELL, the Satan is speaking")
                        for i in range(4):
                            print(".")
                            time.sleep(0.6)
                        print("I honestly hoped I would never see you again, so why are you here?")
                        time.sleep(1.2)
                        l = input("* Will you tell him that the God sent you *")
                        if l == "no":
                              m=input("* Will you kill him? *")
                              if m =="no":
                                    time.sleep(1)
                                    print("* ⛤The Satan consumed your soul for taking too long to answer⛤ *")
                                    time.sleep(2)
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("Credits")
                                    time.sleep(1.5)
                                    print("Directed by Luka")
                                    time.sleep(1.5)
                                    print("Story by Luka")
                                    time.sleep(1.5)
                                    print("Coded by Luka")
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("THANKS FOR PLAYING")
                                    input('Press ENTER to exit')
                              if m =="yes":
                                     time.sleep(2)
                                     for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                     print("* You slayed the Satan with THE CROSS *")
                                     time.sleep(2)
                                     for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                     time.sleep(1)
                                     n = input("* Will you overtake the Hell? *")
                                     if n=="yes":
                                          time.sleep(2)
                                          for i in range(4):
                                              print(".")
                                              time.sleep(0.6)
                                          time.sleep(1)
                                     print("* The God is mad and supprised by your decison... *")
                                     time.sleep(2)
                                     print("* The God send an angel army on hell, the Holy War startted, just like the scripts have forsoken...")
                                     time.sleep(2)
                                     for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                     print("Credits")
                                     time.sleep(1.5)
                                     print("Directed by Luka")
                                     time.sleep(1.5)
                                     print("Story by Luka")
                                     time.sleep(1.5)
                                     print("Coded by Luka")
                                     for i in range(4):
                                         print(".")
                                         time.sleep(0.6)
                                     print("THANKS FOR PLAYING THIS GAME, PART 2 COMING OUT SOON")
                                     input('Press ENTER to exit')
                              if l =="yes":
                                    time.sleep(1)
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("Hmmmm, I knew this would happen one day, so he sent you with that thing to slay me")
                                    time.sleep(1.2)
                                    print("I'm sending an army right now, I want you to be me my right hand, the Holy War will start, we will get along well....")
                                    time.sleep(2)
                                    for i in range(4):
                                        print(".")
                                        time.sleep(0.6)
                                    print("Credits")
                                    time.sleep(1.5)
                                    print("Directed by Luka")
                                    time.sleep(1.5)
                                    print("Story by Luka")
                                    time.sleep(1.5)
                                    print("Coded by Luka")
                                    for i in range(4):
                                         print(".")
                                         time.sleep(0.6)
                                    print("THANKS FOR PLAYING THIS GAME, PART 2 COMING OUT SOON")
                                    input('Press ENTER to exit')            
        if s5<25:
           print("You are staying here, based on your answers, we will get along well")
           time.sleep(2)
           for i in range(4):
                print(".")
                time.sleep(0.6)
           print("Credits")
           time.sleep(1.5)
           print("Directed by Luka")
           time.sleep(1.5)
           print("Story by Luka")
           time.sleep(1.5)
           print("Coded by Luka")
           for i in range(4):
                print(".")
                time.sleep(0.6)
           print("THANKS FOR PLAYING")
           input('Press ENTER to exit')
    if b == "no": 
        print("OK, then burn in hell, see you.")
        input('⛤You are burning in hell, I, the narator, hope you are happy⛤')

    
