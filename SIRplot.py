from pylab import plot, show

t = 0
S = 45400.0
I = 2100.0
R = 2500.0

tList = [t] 
sList = [S] 
iList = [I] 
rList = [R]

deltat = 0.1

for k in range(300):
    Sprime = -.00001*S*I 
    Iprime = .00001*S*I -I/14 
    Rprime = I/14
    
    deltaS = Sprime*deltat 
    deltaI = Iprime*deltat 
    deltaR = Rprime*deltat
    
    t += deltat 
    S += deltaS 
    I += deltaI 
    R += deltaR
    
    tList.append(t) 
    sList.append(S) 
    iList.append(I) 
    rList.append(R)
    

plot(tList,sList) 
plot(tList,iList) 
plot(tList,rList) 
show()