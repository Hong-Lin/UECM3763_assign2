import pylab as p
import numpy as np

mu = 0.1
sigma = 0.26
S0 = 39
n_path = 1000
n = n_partitions = 1000

t = p.linspace(0, 3, n+1)
dB = p.randn(n_path, n+1)/p.sqrt(n)
dB[:,0] = 0
B = dB.cumsum(axis=1)

nu = mu - sigma*sigma/2.0
S = p.zeros_like(B)
S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])

S5= S[0:5]                                # plotting 5 realizations of GBM
p.plot(t,S5.transpose())
p.xlabel('Time,$t$')
p.ylabel('Stock prices')
p.title('5 realizations of the GBM')
p.show()

S3 = p.array(S[:,-1])

print ('Expectation value of S(3) =', np.mean(S3))
print ('Variance of S(3) =',np.var(S3))

a = S3>39.0
b= sum(a)/len(a)
print ('P[S(3)>39]=',b)
c = S3*a
d = sum(c)/sum(a)
print ('E[S(3)|S(3)>39]=',d)


