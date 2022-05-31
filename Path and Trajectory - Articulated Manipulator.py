import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH,ERobot, ELink, ETS
import numpy as np

# link lengths in mm
a1 = float(input("a1 = ")) 
a2 = float(input("a2 = ")) 
a3 = float(input("a3 = ")) 

# link converted to meters
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m
 
a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

# link limits converted to meters
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)

# Create Links
# [robot variable]=DHRobot([RevoluteDH(d,r/a,alpha,offset)])
Arti_Elbow = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a2,0,0,qlim=[(-20/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a3,0,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
], name= 'Arti_Elbow')

print(Arti_Elbow)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi

# q Paths
# for ARTICULATED joint variables = ([T1,T2,T3])
q_init = np.array([0,0,0]) # origin

q_pick = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))]) # 1st path

q2 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))]) # 2nd path

q3 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))]) # 3rd path

# Trajectory commands
traj1 = rtb.jtraj(q_init,q_pick,30) #time vector or steps
print(traj1)
print(traj1.q)
traj2 = rtb.jtraj(q_pick,q2,30)
print(traj2)
print(traj2.q)
traj3 = rtb.jtraj(q2,q3,30)
print(traj3)
print(traj3.q)

#plot scale
x1 = -1.0
x2 = 1.0
y1 = -1.0
y2 = 1.0
z1 = -1.0
z2 = 1.0

#plot command
# for joint variable vs Time(s) table
rtb.qplot(traj1.q)
rtb.qplot(traj2.q)
rtb.qplot(traj3.q)

# plot of trajectory
Arti_Elbow.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2],movie='Arti_Elbow_1.gif')
Arti_Elbow.plot(traj2.q,limits=[x1,x2,y1,y2,z1,z2],movie='Arti_Elbow_2.gif')
Arti_Elbow.plot(traj3.q,limits=[x1,x2,y1,y2,z1,z2],movie='Arti_Elbow_3.gif')

#Arti_Elbow.teach(jointlabels=1)
