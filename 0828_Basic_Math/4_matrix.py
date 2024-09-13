import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 3, 4],
              [10, 20, 30]])

B = np.array([[2, 3, 4],
              [10, 20, 30]], dtype = np.float32)
#모든 matrix 는 float 으로 잡음. 계산된 결과가 정수이기가 힘들기 때문에
#값이 저장이 안됨. 

print("Matrix A = \n", A)
print("Shape of A = ", A.shape)
print("Dtype of A = ", A.dtype)

print("Matrix B = \n", B)
print("Shape of B = ", B.shape)
print("Dtype of B = ", B.dtype)

print(np.__version__)


# Diagonal Matrix

a = np.array([1,2,3,4,5])
D_1 = np.diag(a)
print("D_1 = \n", D_1)

b = np.random.randint(1,10,5)
D_2 = np.diag(b)
print("D_2 = \n", D_2)

# Identitiy 단위행렬

I_3 = np.eye(3)
print("3 x 3 Identity = \n", I_3)


I_5 = np.eye(5)
print("5 x 5 Identity = \n", I_5)


##전치 행렬, Matrix Transpose 
A = np.array([[1,2,3,4],
              [5,6,7,8]], dtype = np.int64)

print("A = \n", A)
print("transpose A = \n", A.T) 

## Matrix Product 

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[1, 1],
              [1, 2]])

print("A*B = \n", A*B) #이거 답이 오ㅐ .. ? 
print("A X B = \n", np.matmul(A, B))






