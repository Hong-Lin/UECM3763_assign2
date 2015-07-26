import pylab as p
import numpy as np

n_path = 1000
n = n_partitions = 1000
t = 1.0
alpha = 1
theta = 0.064
sigma = 0.27
R0 = 3

dt=t/n 
t = p.linspace (0,1,n+1)[:-1]
dB = p.randn(n_path,n+1)*p.sqrt(dt)
dB[:,0] = 0
B = dB.cumsum(axis=1)
R = p.zeros_like(B)

R[:,0] = R0
col = 0
for col in range (n):
    R[:,col+1]=R[:,col]+(theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]
        
R5 = R[0:5:,:-1]
p.plot(t,R5.transpose())
p.xlabel('Time,$t$')
p.ylabel('R(t)')
p.title('5 realizations of the mean reversal process')
p.show()

R1 = R[:,-1]
print ('Expectation value of R(1) =', np.mean(R1))
a = R1>2
b= sum(a)/len(a)
print ('P[R(1)>2]=',b)
