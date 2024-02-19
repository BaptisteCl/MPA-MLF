from random import *
from math import *
from turtle import *
#import matplotlib.pyplot as plt



def PrintPlan(NewOrAll):#all or new only
    up()
    if NewOrAll=="All":
        goto(300,-300)
        down()
        goto(-300,-300)
        goto(-300,300)
        NbFor=len(Point)
    elif NewOrAll=="New" or NewOrAll=="End"  :
        NbFor=k
        
    else : return("Ereure")
    for i in range(NbFor):
        up()
        goto(Point[i][0]*60-300,Point[i][1]*60-300)
        if len(Point[i][2])!=1:#If the point is  a ref kenel point
            if NewOrAll=="End":
                dot(10,"Black")
            else: 
                dot(10,color[i])
        else:
            dot(5,color[int(Point[i][2][0])])
        down()



def average():
    CountAverage=[]
    for i in range(k):
        CountAverage.append([0,0,0])# sum x by color/K, sum y by color/K, number of points
    for i in range(len(Point)):
        CountAverage[int(Point[i][2][0])][0]+=Point[i][0]# sum X
        CountAverage[int(Point[i][2][0])][1]+=Point[i][1]# sum Y
        CountAverage[int(Point[i][2][0])][2]+=1# add 1 point
    for i in CountAverage:
        i[0]=i[0]/i[2]
        i[1]=i[1]/i[2]

    for i in range (k):
        Point[i][0]=CountAverage[i][0]
        Point[i][1]=CountAverage[i][1]
    return(Point)

    

Point=[] #

color=["Blue","red","green","orange","violet","gray","cyan","pink","yellow"]
k=4
for i in range(50):
    x=random()*10
    y=random()*10
    if i<k:
        Point.append([x,y,str(i)+' MySelf',0])
    else:
        Point.append([x,y,'K_ref','distance'])


for i in range(len(Point)):
    distance_min=10
    K_ref_min="init"
    for j in range(k):
        d=sqrt((Point[i][0]-Point[j][0])**2+(Point[i][1]-Point[j][1])**2)
        K_ref=j

        if distance_min>d:
            distance_min=d
            K_ref_min=j
    if distance_min!=0:
        Point[i][2]=str(K_ref_min)
    Point[i][3]=distance_min
     
print()
PrintPlan("All")
Point=average()
PrintPlan("New")
Point=average()
PrintPlan("New")
Point=average()
PrintPlan("New")
Point=average()
PrintPlan("End")

