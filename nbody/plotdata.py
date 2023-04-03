import matplotlib.pyplot as plt
import sys
import math

def plot_orbit(px,py,dt):
    fa = (math.sqrt(5.0)-1.0)/2.0
    fig = plt.figure(figsize=(6,6*fa))
    ax = fig.add_subplot(111)
    #ax.xlim([-0.5,2.5])
    #ax.ylim([-1,1])
    ax.set_title("Planet orbit with dt = {:.2f}".format(dt))
    ax.set_aspect('equal')
    ax.plot(px,py,'o',markersize=0.1)
    ax.plot([0],[0],'o',color='blue',markersize=1)
    fig.tight_layout()
    plt.show()

def main(filename):
    t,px,py = [],[],[]
    with open(filename,'r') as f:
        for l in f.readlines():
            a,b,c = l.rstrip().split(',')
            t.append(float(a))
            px.append(float(b))
            py.append(float(c))  
    plot_orbit(px,py,t[1]-t[0])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please, use as: "+ sys.argv[0] + " [file.csv]");
        sys.exit()
    main(sys.argv[1])