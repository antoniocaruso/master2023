import math
import sys


def main(dt):
    """
    Risolve il calcolo dell'orbita di un pianeta sotto l'influenza di una forza centrale
    gravitazione. (Sole - Pianeta). Si usa solo Python standard.
    Il modello molto semplice: 
      $a = -1/|r|^2 * r/|r|$. nota che (-r/|r|) è il versore diretto verso il Sole
      le masse sono poste M1+M2 = 1 e M1>>>M2
    Si usa Eulero per integrazione:  v = v + a*dt, r = r + v*dt
    Controllo Conservazione Energia: e_cinetia = 1/2 v^2 e e_pot = -1/r
    """

    r = [1,0,0]
    v = [0,0.5,0]
    #dt = float(input("Inserisci il timestep: "))
    N = int(10/dt)
    print("dt : ",dt," passi = ",N)
    
    # calcolo l'energia cinetica e potenziale al tempo zero
    ekin_start = 0.5 * (v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    epot_start = -1.0 / math.sqrt( r[0]*r[0]+r[1]*r[1]+r[2]*r[2] )
    
    a = [0,0,0]
    t = 0
    while t <= 10:
        r2 = r[0]*r[0]+r[1]*r[1]+r[2]*r[2]
        r3 = r2*math.sqrt(r2)
        a[0] = -r[0]/r3       # non posso fare a = -r/r3 con le liste di python.
        a[1] = -r[1]/r3       # si lavora componente per componente.
        a[2] = -r[2]/r3       # se preferite etihette come x,y,z basta usare
                              # x,y,z = 0,1,2 prima del while. e poi: a[x],a[y],a[z]
        r[0] += v[0]*dt
        r[1] += v[1]*dt
        r[2] += v[2]*dt
        
        v[0] += a[0]*dt
        v[1] += a[1]*dt
        v[2] += a[2]*dt
        
        print("{:.5f}, {:.5f}, {:.5f}".format(t,r[0],r[1]))
        t += dt       # se dimenticate questo il loop non termina.
    
    # alla fine calcolo e stampo l'energia finale
    # attenzione al livello di tabulazione
    ekin_end = 0.5 * (v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    epot_end = -1.0 / math.sqrt( r[0]*r[0]+r[1]*r[1]+r[2]*r[2] )
    print("Energia Iniziale = {}".format(ekin_start+epot_start))
    print("Energia Finale = {}".format(ekin_end+epot_end))      
    
if __name__ == '__main__':
    # Se l'utente passa un valore per dt su linea di comando, usa quello
    # stampa le coordinate dell'orbita.
    dt = 0.01
    if len(sys.argv) == 2:
        dt = float(sys.argv[1])
    main(dt)