import threading
import time
task = 0

def task1():
    global task
    task = task + 1
    print("task", task, "will start")
    for i in range (100000000):
        n = i*i
        pass
        # some code
    print("task", task, "ends now")
    
    
def task2():
    global task
    task = task + 1
    print("task", task, "will start")
    for i in range (100000000):
        n = i*i
        pass
        # some code
    print("task", task, "ends now")
    
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
