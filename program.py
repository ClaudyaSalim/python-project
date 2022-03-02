# countdown
import time
sec = int(input())
for i in range (sec, 0, -1):
    if (i%60==0):
        print(i/60, "minutes left")
    else:
        if (i==30 or i<=10):
            print(i, "seconds left")
        else:
            if ((i+1)%60==0 or (i+1)== 30):
                print("...")
            elif (i==sec):
                print("...")
    time.sleep(1)