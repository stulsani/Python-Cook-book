import time

def countdownfunc(n):
    while n > 0:
        print("N--> ",n)
        n -= 1
        time.sleep(1)

from threading import Thread
t = Thread(target = countdownfunc, args=(10,))
t.start()
