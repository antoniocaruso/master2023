import sys
import numpy as np
import matplotlib.pyplot as plt

def main(dt: float, f=True):
    """
    Risolve il calcolo dell'orbita di un pianeta sotto l'influenza di una forza centrale
    gravitazione. (Sole - Pianeta). Si usa solo Python standard.
    Il modello molto semplice: 
      $a = -1/|r|^2 * r/|r|$. nota che (-r/|r|) è il versore diretto verso il Sole
      le masse sono poste M1+M2 = 1 e M1>>>M2
    Si usa Eulero per integrazione:  v = v + a*dt, r = r + v*dt
    Controllo Conservazione Energia: e_cinetia = 1/2 v^2 e e_pot = -1/r
    """
    r = np.array([1,0,0])
    v = np.array([0,0.5,0])
    #dt = float(input("Insert the timestep: "))
    N = int(10/dt)
    print("dt : ",dt," passi = ",N)
    px = np.zeros(N)
    py = np.zeros(N)
    # usando numpy posso fare calcolo vettoriale.
    # notare l'uso degli operatori del linguaggio su un tipo definito
    # da un modulo esterno
    
    for ns in range(N):
    	rl = np.sqrt(r.dot(r))
    	a = -r/(rl**3)
    	r = r + v*dt
    	v = v + a*dt
    	px[ns] = r[0]
    	py[ns] = r[1]

    if f == False:
        return (px,py)

    fig = plt.figure(figsize=(8,8), dpi=200)
    ax = fig.add_subplot(111)
    #plt.xlim([-0.5,1.2])
    #plt.ylim([-0.8,0.8])
    ax.set_aspect('equal')
    ax.set_title('Planet Orbit with dt = {}'.format(dt))
    ax.plot(px,py,"o",markersize=0.1)                                   # orbita
    ax.plot([0],[0],'o',color='red', alpha=0.9, markersize=8)           # sole
    ax.plot(px[-1],py[-1],'o',color='blue', alpha=0.9, markersize=4)    # pianeta
    plt.tight_layout()                                                  # stringi la figura
    fig.savefig("orbita.pdf",dpi=400)                                   # salvo la figura
    return (px,py)
    # plt.show()

    
if __name__ == '__main__':
    # Se l'utente passa un valore per dt su linea di comando, usa quello
    # stampa le coordinate dell'orbita.
    dt = 0.01
    if len(sys.argv) == 2:
        dt = float(sys.argv[1])
    main(dt)