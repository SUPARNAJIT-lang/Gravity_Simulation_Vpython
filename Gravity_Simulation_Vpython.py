from vpython import *
from matplotlib import pyplot as plt

G=6.67430*(10**-2)

planet_position = []
star_position = []

p_1=input("Enter position vec of m1 (x,y,z):")
p_2=input("Enter position vec of m2 (x,y,z):")

vel1=input("Enter velocity vec of m1 (x,y,z):")
vel2=input("Enter velocity vec of m2 (x,y,z):")

# Parsing input velocities
vel1_x, vel1_y, vel1_z = map(float, vel1.split(','))
vel2_x, vel2_y, vel2_z = map(float, vel2.split(','))

# Parsing input positions
x1,y1,z1=map(float, p_1.split(','))
x2,y2,z2=map(float,p_2.split(','))


p1=vec(x1,y1,z1)
p2=vec(x2,y2,z2)



planet=sphere(pos=p1, radius=4, color=color.red, make_trail=True,retain=1000,trail_radius=0.5)

star=sphere(pos=p2, radius=10, color=color.orange,emissive=False, make_trail=True,retain=1000,trail_radius=0.5)

planet.velocity=vector(vel1_x, vel1_y, vel1_z)
star.velocity=vector(vel2_x, vel2_y, vel2_z)


a=float(input("m1"))
b=float(input("m2"))


def energy(m1,m2, p111, p222, v1, v2):
    r_vec = p111 - p222
    r_mag = mag(r_vec)

    kinetic_energy = 0.5 * m1 * mag(v1)**2 + 0.5 * m2 * mag(v2)**2
    potential_energy = - (G * m1 * m2) / r_mag

    total_energy = kinetic_energy + potential_energy
    print(f"Total energy: {total_energy}")
    if total_energy < 0:
        print("Elliptical (Bound)")
    elif total_energy == 0:
        print("Parabolic (Barely Escape)")
    else:
        print("Hyperbolic (Escape)")

    return total_energy


def geta(p, p0, m1, m2):
    r_vec = p - p0
    r_mag = mag(r_vec)
    
    f_vec = -((G * m1 * m2) / (r_mag ** 2)) * norm(r_vec)
    a_vec = f_vec / m1
    return a_vec

#Implimenting RK4:
h=0.001
def rk4(vn,pn,sn,m1,m2):
    k1=h*vn
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

# Instructions
print("\nSimulation running... (Click on VPython window and press 'q' to stop)")

# Initial energy calculation
energy(a, b, planet.pos, star.pos, planet.velocity, star.velocity)

# Key to stop simulation
scene.bind('keydown', lambda evt: setattr(scene, 'paused', True) if evt.key == 'q' else None)
scene.paused = False

while not scene.paused:
    rate(100)
    
    dp1,dv1=rk4(planet.velocity,planet.pos,star.pos,a,b)
    dp2,dv2=rk4(star.velocity,star.pos,planet.pos,b,a)
    
    planet.pos+=dp1
    planet.velocity+=dv1
    
    star.pos+=dp2
    star.velocity+=dv2



    planet_position.append((planet.pos.x, planet.pos.y, planet.pos.z))
    star_position.append((star.pos.x, star.pos.y, star.pos.z))


ax=plt.axes(projection='3d')
x11,y11,z11=zip(*planet_position)
x22,y22,z22=zip(*star_position)

plt.plot(x11,y11,z11,color='brown')
plt.plot(x22,y22,z22,color='orange')

plt.show()





        
    
    
    






    







    
