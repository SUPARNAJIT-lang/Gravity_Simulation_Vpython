from vpython import *



global G
G=6.67430*(10**-2)
p_1=input("Enter position vec of m1 (x,y,z):")
p_2=input("Enter position vec of m2 (x,y,z):")

x1,y1,z1=map(float, p_1.split(','))
x2,y2,z2=map(float,p_2.split(','))

global p1 , p2

p1=vec(x1,y1,z1)
p2=vec(x2,y2,z2)



planet=sphere(pos=p1, radius=4, color=color.red, make_trail=True,retain=500,trail_radius=0.2)

star=sphere(pos=p2, radius=10, color=color.orange,emissive=False, make_trail=True,retain=500,trail_radius=0.2)

planet.velocity=vector(0,1,0)
star.velocity=vector(0,0,0)


a=float(input("m1"))
b=float(input("m2"))


def geta(p1, p2, m1, m2):
    r_vec = p1 - p2
    r_mag = mag(r_vec)
    
    F_vec = -((G * m1 * m2) / (r_mag ** 2)) * norm(r_vec)
    a_vec = F_vec / m1
    return a_vec

#Implimenting RK4:
h=0.09
def rk4(vn,pn,sn,m1,m2):
    k1=h*(vn)
    l1=h*(geta(pn,sn,m1,m2))

    k2=h*(vn+l1/2)
    l2=h*(geta(pn+k1/2,sn,m1,m2))

    k3=h*(vn+l2/2)
    l3=h*(geta(pn+k2/2,sn,m1,m2))

    k4=h*(vn+l3)
    l4=h*(geta(pn+k3,sn,m1,m2))

    k=(k1+2*k2+2*k3+k4)/6
    l=(l1+2*l2+2*l3+l4)/6

    pn1=k
    vn1=l

    return pn1,vn1

while True:
    rate(100)
    
    dp1,dv1=rk4(planet.velocity,planet.pos,star.pos,a,b)
    dp2,dv2=rk4(star.velocity,star.pos,planet.pos,b,a)
    
    planet.pos+=dp1
    planet.velocity+=dv1
    
    star.pos+=dp2
    star.velocity+=dv2

    print(planet.pos)




        
    
    
    






    







    
