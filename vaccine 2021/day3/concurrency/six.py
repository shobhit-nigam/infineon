import threading
task = 0

l = threading.Lock()


def task1():
    # some code
    global l
    print("task1 requests for lock")
    l.acquire()
    global task
    task = task + 1
    print("task", task, "will start")
    for i in range (100000000):
        n = i*i
        pass
        # some code
    print("task", task, "will end now & release the lock")
    l.release()
    
    
def task2():
    # some code
    global l
    print("task2 requests for lock")
    l.acquire()
    global task
    task = task + 1
    print("task", task, "will start")
    for i in range (100000000):
        n = i*i
        pass
        # some code
    print("task", task, "will end now & release the lock")
    l.release()
    
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
