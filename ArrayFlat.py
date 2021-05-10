import numpy as np

def flatener(offspring1):
    arr=np.ndarray.flatten(offspring1[0])
    for i in range(len(offspring1)-1):
        
        temp1=np.ndarray.flatten(offspring1[i+1])
        
        arr=np.concatenate((arr,temp1))
    return arr
def reshaper(arr):
    list1=[]
    ar1=np.reshape(arr[:169], (13,13))
    list1.append(ar1)
    ar2=np.reshape(arr[169:182], (13,))
    list1.append(ar2)
    ar3=np.reshape(arr[182:221], (13,3))
    list1.append(ar3)
    ar4=np.reshape(arr[221:224], (3,))
    list1.append(ar4)
    return list1
    