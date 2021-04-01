import matplotlib.pyplot as plt
import numpy as np
a = np.zeros([100,100,3],dtype = 'uint8')
a[0:50,0:50]  = [[[255,255,255]]]
a[50:100,50:100]  = [[[255,255,255]]]
plt.imshow(a)
