import numpy as np
import matplotlib.pyplot as plt

## cos
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = 2*np.cos(2*x) -1

plt.figure(figsize = (12, 5))
plt.plot(x, np.cos(x), label = "cos(x)")
plt.plot(x, y, label = "2*cos(2*x) -1")
plt.legend()
plt.grid(linestyle = ":")
plt.show()





# def polynomial(x, n):
#     y = x ** n
#     return y 

# x = np.linspace(-4, 4, 100)
# #print(x)
# y = polynomial(x, 1)
# y2 = polynomial(x, 2)
# y3 = polynomial(x, 3)

# plt.plot(x,y, label = "Y = X")
# plt.plot(x, y2, label = "Y = X^2")
# plt.plot(x, y3, label = "Y = X^3")
# plt.plot(x, polynomial(x,4), label = "Y = X^4")


# plt.title("Polynomial curve")
# plt.xlable("X")
# plt.ylabel("f(x)")

# plt.legend()
# plt.ylim(-2,2)
# plt.xlim(-2,2)
# plt.grid(linestyle = ":")
# plt.show()

# 삼각함수 

# print(np.pi)
# X = np.linspace(-2*np.pi, 2*np.pi, 100)
# print(X)

# sin_x = np.sin(X)
# cos_x = np.cos(X)
# tan_x = np.tan(X)


# plt.figure(figsize = (12, 5))
# plt.plot(X, sin_x, label = "sin(x)")
# plt.plot(X, cos_x, label = "cos(x)")
# plt.plot(X, tan_x, label = "tan(x)")

# plt.vlines(0, -1, 1, color ="red")
# plt.hlines(0, -2*np.pi, 2*np.pi, color ="black")
# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], label = ["-2pi", "-pi", "0", "pi", "2pi"])

# plt.ylim(-1, 1)
# plt.xlim(-2*np.pi, 2*np.pi)

# plt.legend() 
# plt.grid(linestyle = ":")
# plt.show()


#########
x = np.linspace(-2*np.pi, 2*np.pi, 100)

sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)

y_list = [sin_x, cos_x, tan_x]
y_label =["sin(x)", "cos(x)", "tan(x)"]
color_list = ['b', 'g', 'r']
fig, ax = plt.subplots(3, 1, figsize = (12, 10))

for i in range(3):
    ax[i].plot(x, y_list[i], label = y_label[i], c = color_list[i])
    ax[i].set_ylim(-1, 1)
    ax[i].grid(linestyle = ":")
    ax[i].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
 

plt.show()

########
# y-b = sin(x-a)의 그래프는 y= sin x의 그래프를 x축으로 a만큼, y축으로 b만큼 평행 이동한 것. 

# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.sin(x)
# y1 = np.sin(x - np.pi) + 1

# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = "sin(x)")
# plt.plot(x, y1, label = "sin(x-pi)")    

# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
# plt.show()

###
# y = -sin x의 그래프는 y = sin x의 그래프를 x축을 중심으로 선대칭이다. 

# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.cos(x)
# y1 = -np.cos(x)

# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = "cos(x)")
# plt.plot(x, y1, label = "-cos(x-pi)", linestyle = ":")    

# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
# plt.show()

# ###
# # y = a*sin x의 그래프는 y = sin x의 함수값을 a 배 한 것이다. 
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.sin(x)
# y1 = 2*np.sin(x)

# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = "sin(x)")
# plt.plot(x, y1, label = "2*sin(x)", linestyle = ":")    

# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
# plt.show()

# # y = sin ax의 그래프는 y = sin x 와 모양은 같고 주기가 2파이 / |a| 인 그래프이다. (절대값a) 
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y = np.sin(x)
# y1 = np.sin(2*x)

# plt.figure(figsize = (12, 5))
# plt.plot(x, y, label = "sin(x)")
# plt.plot(x, y1, label = "sin(2*x)", linestyle = ":")    

# plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
# plt.grid(linestyle = ":")
# plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
# plt.show()

###3.4.4
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x - np.pi/2)
y1 = np.sin(x-np.pi/2) + 1

plt.figure(figsize = (12, 5))
plt.plot(x, y, label = "x - np.pi/2")
plt.plot(x, y1, label = "(x-np.pi/2) + 1", linestyle = ":")    

plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
plt.show()


###3.4.5
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = 2*np.sin(x)
y1 = 2*np.sin(x-np.pi/2) + 1

plt.figure(figsize = (12, 5))
plt.plot(x, y, label = "2*sin(x)")
plt.plot(x, y1, label = "2*sin(x-np.pi/2) + 1", linestyle = ":")    

plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
plt.show()

###3.4.6 
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(2*x)
y1 = np.sin(2*x-np.pi) - 1

plt.figure(figsize = (12, 5))
plt.plot(x, y, label = "sin(2*x)")
plt.plot(x, y1, label = "sin(2*x-pi) - 1", linestyle = ":")    

plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
plt.show()

###3.4.7 
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x-np.pi/2)
y1 = -np.cos(x) + 1
y2 = np.cos(2*x + np.pi)
y3 = np.cos(x)

plt.figure(figsize = (12, 5))
plt.plot(x, y, label = "cos(x-pi/2)")
plt.plot(x, y1, label = "-cos(x) + 1", linestyle = ":")    
plt.plot(x, y2, label = "cos(2*x+pi)", linestyle = "-.")   
plt.plot(x, y3, label = "cos(x)", color='magenta')


plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], labels = ["-2pi", "-pi", "0", "pi", "2pi"])
plt.grid(linestyle = ":")
plt.legend() #sin(x) 를 호출. 얘가 호출되려면 label 지정해줘야함 
plt.show()