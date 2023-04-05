import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

G = 1
m = 1
def f_grav(y, t):
    x1, x2, v1, v2 = y
    r = np.hypot(x1,x2) 
    F = G*m/r**3
    return [v1, v2, -x1*F, -x2*F]

t = np.linspace(0, 100, 1001)
init = [0, 1, 1, 0]
ans = odeint(f_grav, init, t)
print(ans)

x,y,_,_ = ans.T

plt.plot(0,0,"oy",ms=8)
plt.plot(x,y)
plt.axis("equal")
plt.show()

