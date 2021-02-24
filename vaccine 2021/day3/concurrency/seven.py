import multiprocessing
import time

def taska():
    for i in range(12, 0, -1):
        print("task A left with", i, "seconds")
        time.sleep(1)
        
def taskb():
    for i in range(15, 0, -1):
        print("task B left with", i, "seconds")
        time.sleep(1)
        
pa = multiprocessing.Process(target=taska)
pb = multiprocessing.Process(target=taskb)

pa.start()
pb.start()
