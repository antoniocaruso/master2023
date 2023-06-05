
from threading import Thread
import time
import random
q = list()
a = 100

def produttore(name):
    global a
    i = 1
    while True:
        if a % 2 == 0:
            a = a + 2
        else:
            a = a + 1
        i = i + 1
        print(f"p({i}): {a}")

    # global q
    # print(f"thread {name} started")
    # working = True
    # for k in range(100):
    #     time.sleep(0.5)
    #     x = random.randint(0,100)
    #     q.insert(0,x)                   # estendi la lista
    #     print(f"From producer: {x}, q = {q}")
    #                             # scrivi x nel primo elemento
    #     if x == 100:
    #         working = False
    #         break
    # if working:
    #     q.insert(0,100)
    

def consumatore(name):
    global a
    i = 1
    while True:
        a = a + 1
        print(f"c({i}): {a}")
        i = i + 1

    
    # global q
    # working = True
    # print(f"thread {name} started")
    # while working:    
    #     print(f"Consumer: coda = {q}")
    #     if len(q) > 0:
    #         x = q.pop()
    #         if x == 100:
    #             working = False
    #         print(f"Consumer: popped {x}")
    #         time.sleep(0.5)
    # print(f"Consumer ended")

if __name__ == "__main__":
    thread1 = Thread(target=produttore, args=("Produttore",))
    thread2 = Thread(target=consumatore, args=("Consumatore",))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()



    