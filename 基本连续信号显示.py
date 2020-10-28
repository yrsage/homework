import matplotlib.pyplot as plt
import numpy as np 

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(-1, 10, 50)
y = np.exp(x)
plt.subplot(1,4,1)
plt.title(r'实指数信号$f(x)=e^x$') 
plt.plot(x, y)
#plt.show()

x1 = [t*0.375*np.pi+np.pi/2 for t in x]
y1 = np.sin(x1)
plt.subplot(1,4,2)
plt.title(r'正弦信号$f(x)=sin(\omega x+\pi/2), \omega = \frac{3}{8} \pi$')
plt.plot(x1, y1)

def u(x):
    y = x > 0
    return y

x2 = np.linspace(-5, 5, 50)
y2= u(x2)
plt.subplot(1,4,3)
plt.title(r'单位阶跃信号$u(t)$')
plt.plot(x2, y2)

def t(x):
    y = x == 0 
    return y

x3 = np.linspace(-5, 5, 50)
y3= t(x3)
plt.subplot(1,4,4)
plt.title(r'冲激信号$u(t)$')
plt.plot(x3, y3)

plt.show()