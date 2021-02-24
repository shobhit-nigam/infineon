import time
import threading

def taska():
    for i in range(3, 0, -1):
        print("task A left with", i, "seconds")
        time.sleep(1)

def taskb():
    for i in range(6, 0, -1):
        print("task B left with", i, "seconds")
        time.sleep(1)

def taskc():
    for i in range(9, 0, -1):
        print("task C left with", i, "seconds")
        time.sleep(1)

ta = threading.Thread(target=taska)
tb = threading.Thread(target=taskb)
tc = threading.Thread(target=taskc)

tc.start()
tb.start()
ta.start() 
