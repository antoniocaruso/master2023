import threading
import multiprocessing
import time


def presentazione(name):
    me = threading.current_thread()
    print(f"I am the thread with id: {me.name} with args {name}.")
    time.sleep(3)      # calcolo qualcosa inerente al TSP
    print(f"Fine {me.name}.")


if __name__ == "__main__":
    P = multiprocessing.cpu_count()
    print(f"Sto girando su una macchina con {P} core")
    threads = []
    print(f"Start {P} threads")
    for i in range(P):
        t = threading.Thread(target=presentazione, name = "Antonio"+str(i), args = (i,))
        t.start()
        threads.append(t)
    print("continue with main")
    for i in range(10):
        print(f"{i}")
    print("fine lavoro main..voglio terminare")
    for t in threads:
        t.join()        # attesa con blocco...
    print("Qui la main finisce..e finisce il programma alias processo...")
