import numpy as np
import matplotlib.pyplot as plt
import math

N = 100000
y = np.random.rand(N)

s1 = 0.65
y1 = y + np.random.normal(0.0, s1,(N))

s2 = 0.8
y2 = y + np.random.normal(0.0, s2,(N))

s3 = 1.1
y3 = y + np.random.normal(0.0, s3,(N))

alphaOpti1 = s2*s2*s3*s3 / (s1*s1*s2*s2+s1*s1*s3*s3+s3*s3*s2*s2)
alphaOpti2 = s1*s1*s3*s3 / (s1*s1*s2*s2+s1*s1*s3*s3+s3*s3*s2*s2)
alphaOpti3 = s1*s1*s2*s2 / (s1*s1*s2*s2+s1*s1*s3*s3+s3*s3*s2*s2)

sOpti = math.sqrt(s1*s1*s2*s2*s3*s3/ (s1*s1*s2*s2+s1*s1*s3*s3+s3*s3*s2*s2))
print('Computed:', alphaOpti1, alphaOpti2, alphaOpti3, sOpti)

a1 = []
a2 = []
a3 = []
s = []
sO = []
for alpha1 in range(101):
    alpha1X = alpha1 / 100.0
    for alpha2 in range(101):
        alpha2X = alpha2 / 100.0

        alpha3X = 1.0 - alpha1X - alpha2X
        if alpha3X >= 0:
            yy = alpha1X * y1 + alpha2X * y2 + alpha3X * y3

            a1.append(alpha1X)
            a2.append(alpha2X)
            a3.append(alpha3X)
            s.append(math.sqrt(
            	np.sum((yy-y)**2)/(N-1.0)))
            sO.append(sOpti)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

pos = np.argmin(s)
print('Simulated:', a1[pos], a2[pos],
	a3[pos], s[pos])

ax.scatter(a1,a2,s,c='r',alpha=0.1)
ax.scatter(a1,a2,sO,c='g',alpha=0.1)
ax.scatter([alphaOpti1],[alphaOpti2],
	[sOpti],c='b')
ax.set_xlabel(r"$\alpha_1$")
ax.set_ylabel(r"$\alpha_2$")
ax.set_zlabel(r"$\sigma_B^2$")
plt.show()
