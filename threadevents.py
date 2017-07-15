import time
from threading import Thread,Event

def countdownfunc(n, started_event):
    print("Thread started to execute!!")
    started_event.set()
    while n > 0:
        print("N--> ",n)
        n -= 1
        time.sleep(1)

started_event = Event()

print("Launching the Event")
t = Thread(target=countdownfunc,args=(10,started_event))
t.start()

started_event.wait()
print("Now start executing this part of code!!")
