import numpy as np
A=np.mat([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,-1,0,-1],[-1,0,-1,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
D=np.mat(np.diag(np.diag(A)))
L=np.mat(np.tril(A,-1))
U=np.mat(np.triu(A,1))

b=np.mat([0,5,-2,5,-2,6])
b=np.transpose(b)

B1=np.linalg.inv(D)*(L+U)
B2=np.linalg.inv(D-L)*U
w1=1.334
w2=1.95
w3=0.95
B31=np.linalg.inv(D-w1*L)*((1-w1)*D+w1*U)
B32=np.linalg.inv(D-w2*L)*((1-w2)*D+w2*U)
B33=np.linalg.inv(D-w3*L)*((1-w3)*D+w3*U)

print(max(map(abs,(np.linalg.eig(B1)[0]))))
print(max(map(abs,(np.linalg.eig(B2)[0]))))
print(max(map(abs,(np.linalg.eig(B31)[0]))))
print(max(map(abs,(np.linalg.eig(B32)[0]))))
print(max(map(abs,(np.linalg.eig(B33)[0]))))