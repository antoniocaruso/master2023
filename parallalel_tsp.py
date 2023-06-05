
import random
from itertools import permutations
import time
from multiprocessing import Process, cpu_count
from multiprocessing import queues
import sys

City = complex
def X(city): return city.real
def Y(city): return city.imag

def distance(a,b): return abs(b-a)

def Cities(n, w=900, h=600, seed=1):
    # creo n punti a caso sul piano.
    random.seed(seed)
    return frozenset(City(random.randrange(w),random.randrange(h)) for _ in range(n))

Tour = list

def alltours(cities):
    start = cities[0]
    return [[start] + Tour(r) for r in permutations(cities[1:])]

def tour_length(t):
    return sum(distance(t[i-1],t[i]) for i in range(len(t)))

def minimo_tours(x: list):
    return min(x,key=tour_length)
  
def bruteforce(c):
    l = list(c) 
    t0 = time.perf_counter()
    m = minimo_tours(alltours(l))
    print("Soluzione sequenziale:")
    s = [l.index(m[i]) for i in range(len(l))]
    print(s,"len = ", tour_length(m))
    t1 = time.perf_counter()
    print(f"Tempo di esecuzione sequenziale = {t1-t0} sec.")
    return m
 
def worker(id,N,cities):
    print(f"Started process   {id}")
    t0 = time.perf_counter()
    c = list(cities)
    citta_first = c[0]
    citta_id = c[id]
    c.remove(citta_first)
    c.remove(citta_id)
    s = [[citta_first,citta_id] + Tour(r) for r in permutations(c)]
    m = minimo_tours(s)
    t1 = time.perf_counter()
    c = list(cities)
    indici = [c.index(x) for x in m]
    print(f"Process {id}: ",indici,tour_length(m),t1-t0)

if __name__ == "__main__":
    N = 10
    C = Cities(N)
    print("------ Città: -------")
    for i,c in enumerate(C):
        print(i,"\t",c)
    print("-"*40)    
    bruteforce(C)
    P = N-1     # multiprocessing.cpu_count()
    process_list = []
    for i in range(1,P+1):
        p = Process(target=worker,args=(i,N,C))
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()
    print("Fine")


