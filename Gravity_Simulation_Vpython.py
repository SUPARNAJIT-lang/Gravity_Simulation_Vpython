import math
from vpython import *
import sympy as sp

global G
G=6.67430*(10**-3)

p_1=input("Enter position vec of m1 (x,y,z):")
p_2=input("Enter position vec of m2 (x,y,z):")

x1,y1,z1=map(float, p_1.split(','))
x2,y2,z2=map(float,p_2.split(','))

global p1 , p2

p1=vec(x1,y1,z1)
p2=vec(x2,y2,z2)



plnt=sphere(pos=p1, radius=1, color=color.red,make_trail=True)

star=sphere(pos=p2, radius=2, color=color.yellow)

plnt.velocity=vector(0,0,0)

a=float(input("m1"))
b=float(input("m2"))


def com(m1,m2):
    p_com=(m1*p1+m2*p2)/(m1+m2)
    print(p_com)
    return p_com

p_com=com(a,b)

def gravity(p1,p2,m1,m2):
    r_vec=p1-p2
    r_mag=mag(r_vec)
    F_vec=-((G*(m1*m2))/(r_mag**2))*norm(r_vec)
    print(F_vec)
    


dt=1

while True:
    rate(100)
    
    plnt.pos=plnt.pos+plnt.velocity*dt
    F_vec=gravity(plnt.pos,star.pos,a,b)
    acc=(F_vec)*(a**-1)
    plnt.velocity=plnt.velocity+(acc)*dt
