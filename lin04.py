import matplotlib.pyplot as plt
import numpy as np

def noverk(n,k):
  ret = 1
  for i in range(k):
    ret *= (n-i) / (k-i)

  return ret

p = np.arange(0.0, 1.01, 0.01)
print(p)
fig, ax = plt.subplots(figsize=(10,10))

for n in range(1,105,2):
  pppp = p**n
  k = int((n-1)/2)
  for i in range(1, k+1, 1):
    pppp += noverk(n, i) * p**(n-i) * (1-p)**i
  ax.plot(p, pppp)

plt.xlabel(r"$p$")
plt.ylabel(r"$P_{correct}$")
plt.show()
