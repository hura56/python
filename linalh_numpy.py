import numpy.linalg as LA
import numpy as np

a=np.arange(4)
a.shape=(2,2)
print("a=",a)
ainv  = LA.pinv(a)
print("ainv=",ainv)
print("a*ainv=",a.dot(ainv))
print("det(a)=",LA.det(a))
print("det(ainv=", LA.det(ainv))
print("det(a)*det(ainv=", LA.det(a)*LA.det(ainv))
print("eigensystem(a)=", LA.eig(a))