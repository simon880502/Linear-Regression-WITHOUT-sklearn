# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:53:58 2019

@author: simon880502
"""
import numpy as np
import matplotlib.pyplot as plt

def Predict(X=[]):
    X.insert(0,1)
    print('when X = ',X,', y_bar = ',np.inner(w,X))
def PLT():
    plt.xlabel('Epoch')
    plt.ylabel('Mean Absolute Error')
    plt.title('Data 2 Error Function')
    plt.scatter(epoch_list[10::1000],MAE_list[10::1000])

#READ TXT
X=np.loadtxt('data2.txt',delimiter='\t')
y=np.array(X[::,-1::],dtype=float)
w=np.random.random((1,X.shape[1]))
X=X[::,0:-1:]
One=np.full((X.shape[0],1),1)
X=np.hstack((One,X))
del One 

#VARIABLE SET UP
LR=0.00002
epoch=0
epochBound=99999
MAE=100
tolerance_error=0.7
epoch_list=[]
MAE_list=[]

#COMPUTE W,MSE
while(epoch<=epochBound):
    if (MAE<tolerance_error):
        break
    error=0
    error_sum=0
    for i in range(X.shape[0]):
        y_bar=np.inner(w,X[i])
        w=w+((LR*(y[i]-y_bar))*X[i])
        square_error=abs(y[i]-np.inner(w,X[i]))
        error_sum=error_sum+square_error
    epoch+=1
    MAE=error_sum/X.shape[0]
    epoch_list.append(epoch)
    MAE_list.append(MAE)
    print('EPOCH:',epoch,', Mean Absolute Error',MAE[0])
print('Training End')

#PRINT RESULT
print('\nMean Absolute Error : ',MAE[0],'\n\n')
PLT()
#ANS
print('\nAns:\nweight : ',w)
Predict([6.8, 210, 0.402, 0.739])
Predict([6.1,  180, 0.415, 0.713])