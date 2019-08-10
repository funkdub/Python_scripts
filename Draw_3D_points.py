#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


f = open('/Users/tony/Desktop/1.1.10.txt')

x= []
y =[]
z = []


for line in f:
    t1 = float(line.split('  ')[0].split(' ')[1])
    t2 = float(line.split('  ')[1])
    t3 = float(line.split('  ')[2].split('/')[0])

    if t1>3000 or t1<-2000:
        continue
    if t2>3000 or t2<-2000:
        continue
    if t3>3000 or t3<-2000:
        continue
    
    x.append(t1)
    y.append(t2)
    z.append(t3)

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x[100::],y[100::], z[100::])

plt.show()


# In[1]:


get_ipython().system('pwd')


# In[5]:


from PIL import Image
img = Image.open('Desktop/1.jpg')


# In[ ]:




