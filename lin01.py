import matplotlib.pyplot as plt
import numpy as np
import random

p = np.arange(0.5, 1.0, 0.01)
p_3 = p * p * p + 3 * p * p * (1-p)
p_3_3 = p_3 * p_3 * p_3 + 3 * p_3 * p_3 * (1-p_3)

p_9 = p**9 + 9 * p**8 * (1-p) + 36 * p**7 * (1-p)**2 + 84 * p**6 * (1-p)**3 + 126 * p**5 * (1-p)**4

sp_3_3 = []
for i in range(len(p)):
    sp = p[i]
    
    cor = 0
    for j in range(30000):
        cc = 0
        for l in range(3):
            c = 0
            for k in range(3):
                if random.random() <= sp:
                    c +=1
            if c >= 2:
                cc += 1
        if cc >= 2:
            cor += 1
    sp_3_3.append(cor/30000.0)

sp_9 = []
for i in range(len(p)):
    sp = p[i]
    
    cor = 0
    for j in range(30000):
        c = 0
        for k in range(9):
            if random.random() <= sp:
                c +=1
        if c >= 5:
            cor += 1
    sp_9.append(cor/30000.0)

plt.figure(num='', figsize = (15,12))

plt.plot(p, p_3_3, 'r')
plt.plot(p, sp_3_3, '--', color='r')
plt.plot(p, p_9, 'b')
plt.plot(p, sp_9, '--', color='b')
plt.xlabel('p')
plt.ylabel('Combined probability')
plt.show()

