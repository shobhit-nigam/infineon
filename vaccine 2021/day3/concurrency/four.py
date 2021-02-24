import time
import threading

def taska():
    for i in range(9, 0, -1):
        print("task A left with", i, "seconds")
        time.sleep(1)

def taskb():
    for i in range(6, 0, -1):
        print("task B left with", i, "seconds")
        time.sleep(1)

def taskc():
    for i in range(9, 0, -1):
	print(threading.current_thread().name)
	time.sleep(1)

ta = threading.Thread(target=taska, name="file write")
tb = threading.Thread(target=taskb, name="db creation")
tc = threading.Thread(target=taskc)

#tc.start()
tb.start()
ta.start() 


for i in range(3, 0, -1):
	print("main left with", i, "seconds")
	time.sleep(1)

#ta.join()
tb.join()

print("last line of two.py")





