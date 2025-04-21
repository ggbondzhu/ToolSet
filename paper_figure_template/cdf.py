# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

y1 = [0.3,0.1,0.2,0.05,0.07,0.02,0.0022,0.005,0.004,0.001,0.002]
y = [0.44,0.7,0.8,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.999999999]
x=[0,1,2,3,4,5,6,7,8,9,10]                    #虚假的x值，用来等间距分割
x_index=['0','1','2','3','4','5', '6','7','8','9','   10+']

# x = np.arange(20, 350)
# l1 = plt.plot(x, y, 'bo-')
plt.plot(x, y, c='#4b74b2',linewidth=2,marker='o')
# plt.title('The Lasers in Three Conditions')
plt.xlabel('Times',fontsize=24)
plt.ylabel('CDF',fontsize=24)
# plt.legend(fontsize=20)
plt.yticks(fontsize=24)
plt.grid(ls='--')
_ = plt.xticks(x,x_index,fontsize=24)
plt.rc('font',family='Times New Roman')
plt.savefig('cdf2.pdf', bbox_inches = 'tight')
plt.show()
