import numpy as np
import matplotlib.pyplot as plt
import math

N = 100000
y = np.random.rand(N)

s1 = 0.5
y1 = y + np.random.normal(0.0, s1,(N))

s2 = 0.8
y2 = y + np.random.normal(0.0, s2,(N))

alphaOpti1 = s2*s2 / (s1*s1+s2*s2)
alphaOpti2 = s1*s1 / (s1*s1+s2*s2)
sOpti = math.sqrt(s1*s1*s2*s2/
	(s1*s1+s2*s2))
print('Computed', alphaOpti1,
	alphaOpti2, sOpti)

a1 = []
a2 = []
s = []
sO = []
for alpha in range(101):
    alphaX = alpha / 100.0
    yy = alphaX * y1 + (1.0 - alphaX) * y2
    a1.append(alphaX)
    a2.append(1.0-alphaX)
    s.append(math.sqrt(np.sum((yy-y)**2)
    	/(N-1.0)))
    sO.append(sOpti)

pos = np.argmin(s)
print('Simulated', a1[pos], a2[pos], s[pos])

plt.figure(figsize=(10,10))
plt.plot(a1,s,'r')
plt.plot(a1,sO,'g')
plt.plot([alphaOpti1],[sOpti],'bo')
plt.xlabel(r"$\alpha$")
plt.ylabel(r"$\sigma_B^2$")
plt.show()
