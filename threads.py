import threading
import multiprocessing
import time
import numpy as np
from math import sin,cos

def f(x):
    return x+3*sin(x/100)-cos(x/100)

def presentazione(tid,v,p):
    me = threading.current_thread()
    N = len(v)
    s = N // p
    print(f"I am the thread with id: {me.name} with args {tid}, {N}, {p}, {s}.")
    start, end = tid*s,(tid+1)*s   # mapping tra l'id del thread e segmenti disgiunti nei miei dati.
    print(f"Thread {tid} work on [{start},{end})")
    t0 = time.perf_counter()
    v = list(map(f,valori[start:end]))
    t1 = time.perf_counter()
    print(f"Tempo di esecuzione per {tid} = {t1-t0} sec.")

def compute_main(n,valori):
    t0 = time.perf_counter()
    v = list(map(f,valori))
    t1 = time.perf_counter()
    print(f"Tempo di esecuzione = {t1-t0} sec.")


if __name__ == "__main__":
    N = 100_000_000
    valori = np.arange(N)
    # compute_main(N,valori)
    P = multiprocessing.cpu_count()
    print(f"Sto girando su una macchina con {P} core")
    threads = []
    print(f"Start {P} threads")
    for i in range(P):
        t = threading.Thread(target=presentazione, name = "Antonio"+str(i), args = (i,valori,10))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()        # attesa con blocco...