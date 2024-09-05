import numpy as np
import matplotlib.pyplot as plt

'''
v = np.array([1,1])
w = np.array([-2,-1])

plt.quiver(0, 0, v[0], v[1], angles = "xy", scale_units = "xy", scale = 1, color = 'r')
plt.quiver(0, 0, w[0], w[1], angles = "xy", scale_units = "xy", scale = 1, color = 'b')

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(linestyle = ":")
plt.show()


v = np.array([[1, 1],
              [-2, 2],
              [4, -7]])

origin = np.array([[0,0,0],
                   [0,0,0]])

# print(origin)
# print(*origin)

plt.quiver(*origin, v[:, 0] , v[:, 1], angles = "xy", scale_units = "xy", scale = 1, 
           color = ['r', 'b', 'c'])
#v[:, 0] = ':' 모든 행을 뽑고, 0번째 열을 뽑아
##v[:, 1] = ':' 모든 행을 뽑고, 1번째 열을 뽑아

plt.grid(linestyle = ":")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

# print("v = |n", v)
# print("Shape of v = ", v.shape)
# print("Dtype of v = ", v.dtype)

'''


# Projection vector

def projection_vec(base_vec, target_vec):
    scale = np.inner(base_vec, target_vec)/np.linalg.norm(base_vec)**2 
    #절대값처럼 생긴 벡터 길이 |a| 이거 이름이 norm 제곱이면 norm**2 
    proj_vec = scale*base_vec 
    
    plt.quiver(0,0,base_vec[0], base_vec[1], angles = "xy", scale_units = "xy", 
               color = 'r', scale = 1, label = 'Base vector')
    plt.quiver(0,0,target_vec[0], target_vec[1], angles = "xy", scale_units = "xy", 
                color = 'g', scale = 1, label = 'Target vector')
    plt.quiver(0,0,proj_vec[0], proj_vec[1], angles = "xy", scale_units = "xy", 
                color = 'b', scale = 1, label = 'Projected vector')
    
    plt.xlim(-8, 8)
    plt.ylim(-5, 5)
    plt.grid(linestyle = ":")
    plt.legend()
    plt.show()


projection_vec(np.array([-2, 1]), np.array([-6, 4]))