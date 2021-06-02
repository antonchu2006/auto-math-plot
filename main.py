import matplotlib.pyplot as plt
import numpy as np

## Cambiar los valores al gusto

a = 1
b = -4
c = 7

def f(x, a, b, c):
    return a*x*x+b*x+c
def vx(a, b):
    return -b / a**2
def vy(a, b, c):
    return a*vx(a,b)**2+b*vx(a,b)+c

## Cambiar el -10 y el 10 para los valores máximos y mínimos del dominio. En este caso es [-10, 10]
dom = np.linspace(-10, 10,num=1000)
ylist = f(dom,a,b,c)

Vx = vx(a, b)
Vy = vy(a, b, c)

print("Vértice: (" + str(Vx) + "," + str(Vy) + ")")

plt.figure(num=0,dpi=120)
plt.plot(dom,ylist)
plt.show()
