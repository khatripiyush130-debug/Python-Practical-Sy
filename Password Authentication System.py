import time

attempt=0

while True:
    i=input("Enter Password=")

    if(i=="Piyushk92"):
        print("Password Verified.")
        print("You can Enter in system.")
        break
    else:
        attempt=attempt+1
        print("Password is wrong.Try Again.")

        if(attempt==3):
            print("System Locked.Try Later.")
            print("Weit for 30 Seconds....")

            countdoun=30
            while countdoun>0:
                print("weit for",countdoun,"seconds....")
                time.sleep(1)
                countdoun-=1
            print("System Unlocked.You can try again.")

        