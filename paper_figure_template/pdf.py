import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
from scipy.interpolate import make_interp_spline

x = np.array(["1","2","3","4-5","6-8","9-12","13+"])
y = np.array([0.1,0.14,0.13,0.07,0.08,0.03,0.07,])
fig = plt.figure(figsize=(8.8,6))
axes1 = fig.add_axes([0.14, 0.14, 0.82, 0.8])
axes2 = fig.add_axes([0.5, 0.6, 0.4, 0.3])
axes1.bar(x, y, width = 0.5)
# axes1.yticks(fontsize=28)
# plt.xticks(fontsize=28)
axes1.grid(ls='--',axis='y')
axes1.set_xlabel('Burst Loss',fontsize=28)
axes1.set_ylabel('PDF',fontsize=30)
axes1.set_yticklabels(axes1.get_yticklabels(), fontsize=20)
axes1.set_xticklabels(axes1.get_xticklabels(), fontsize=20)
y_major_locator=MultipleLocator(0.1)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
axes1.set_ylim(0,0.4)

# replace file name
x_cdf = np.loadtxt('./filename.csv', usecols=0, delimiter=',', dtype='int')
y_cdf = np.loadtxt('./filename.csv', usecols=3, delimiter=',', dtype='float')
X_Y_spline = make_interp_spline(x_cdf, y_cdf)
X_ = np.linspace(x_cdf.min(), x_cdf.max(), 5000)
Y_ = X_Y_spline(X_)
axes2.step(X_, Y_)
axes2.set_xlim(0, 300)
axes2.set_xlabel('Loss',fontsize=28)
axes2.set_ylabel('CDF',fontsize=30)
plt.yticks(size=20)
plt.xticks(size=20)

plt.savefig('loss.pdf', bbox_inches='tight')
plt.show()
