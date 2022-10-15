import matplotlib.pyplot as plt
import numpy as np

def noverk(n,k):
  ret = np.arange(1,2,1,dtype=np.longfloat)
  for i in range(k):
    ret *= (n-i) / (k-i)

  return ret

p = np.arange(500, 600, 1, dtype = np.longfloat) / 1000
print(p)
fig, ax = plt.subplots(figsize=(10,10))

for n in range(5001,15002,5000):
  pppp = p**n
  k = int((n-1)/2)
  for i in range(1, k+1, 1):
    pppp += noverk(n, i) * p**(n-i) * (1-p)**i
  print(n, pppp[0:5])
  ax.plot(p, pppp)

plt.xlabel(r"$p$")
plt.ylabel(r"$P_{correct}$")
plt.show()
