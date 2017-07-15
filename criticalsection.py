import threading

# Normal Lock
class SharedCounter:
    def __init__(self,initial_value=0):
        self.value = initial_value
        self.value_lock = threading.Lock()

    def incrementValue(self,x):
        with self.value_lock:
            self.value += x

    def decrementValue(self,x):
        with self.value_lock:
            self.value -= x

# RLock

value_rlock = threading.RLock()
class SharedCounter:
    def __init__(self,initial_value=0):
        self.value = initial_value

    def incrementValue(self,x):
        with SharedCounter.value_rlock:
            self.value += x

    def decrementValue(self,x):
        with SharedCounter.value_rlock:
            self.value -= x

# Semaphores
from threading import Semaphore
import urllib.request

mysem = Semaphore(5)

def fetchUrl(url):
    with mysem:
        return urllib.request.urlopen(url)
