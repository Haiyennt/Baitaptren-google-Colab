# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PczCgkGNWahR-sFui3GBR4RX-RuBq0ki
"""

import tensorflow as tf
import numpy as np
# creat a numpy array
array_np = np.arange(10)
print (array_np)
print (array_np.shape)
print('---------------------------------------')
# convert from numpy array to tensor
arr_tf = tf.convert_to_tensor(arr_np)
print(arr_tf)
print(arr_tf.shape)
print('---------------------------------------')
# convert from tensor to numpy array 
arr_numpy_back = arr_tf.numpy()
print (arr_np_back)
print (arr_np_back.shape)

#aivietnam.ai
# tao ndarray tu list
import numpy as np
# tao list
l= list (range (1,4))
# tao ndarray 
data = np.array(l)
print (data)
print (data [0])
print (data [1])

## TAO LIST 1D
#aivietnam.ai
# tao ndarray tu list
import numpy as np
# tao list
list1D =[1,2,3] 
# tao ndarray 
data = np.array(list1D)
print (data)
print (data.shape)

## TAO LIST 2D
#aivietnam.ai
# tao ndarray tu list
import numpy as np
# tao list
list2D =[[1,2],[3,4], [5,6]] 
# tao ndarray 
data = np.array(list2D)
print (data)
print (data.shape)

### TAO LIST 3D
#aivietnam.ai
# tao ndarray tu list
import numpy as np
# tao list
list3D =[[1,6],[2,2], [3,4] 
         [4,7],[5,2], [6,5] 
         [7,7],[8,2], [9,5]] 
# tao ndarray 
data = np.array(list3D)
#print (data)
print (data.shape)


### DTYPE EXAMPLE
#aivietnam.ai
# tao ndarray tu list
import numpy as np

# tao ndarray 
data1 = np.array([1,2,3])
print (data1.dtype)
data2 = np.array([1.,2.,3.])
print (data2.dtype)
data3 = np.array([1,2,3], dtype=np.int64)
print (data3.dtype)


#aivietnam.ai
# thay doi gia tri phan tu
import numpy as np
# tao list
l= list (range (1,4))
# tao ndarray 
data = np.array(l)
print (data)
data[0]=8
print (data )

#aivietnam.ai
# tao 1 numpy array voi tat ca cac phan tu la 0
import numpy as np
# shape: 2 dong, 3 cot
arr = np.zeros((2,3))
print (arr)

#aivietnam.ai
# tao 1 numpy array voi tat ca cac phan tu la 1
import numpy as np
# numpy.one (shape)
# shape: 2 dong, 3 cot
arr = np.ones((2,3))
print (arr)

#aivietnam.ai
# tao 1 numpy array voi tat ca cac phan tu la 1hang so fill value
import numpy as np
# numpy.full (shape, fill_value)
# shape: 2 dong, 3 cot
arr = np.full((2,3),9)
print (arr)


#aivietnam.ai
import numpy as np
#np.arange (start=0, stop, step=1)
arr1 = np.arange(5)
print (arr1)
arr2 = np.arange(0,5,2)
print (arr2)

#aivietnam.ai
# Tao 1 numpy array voi duong cheo la 1, cac vi tri khac la 0
import numpy as np
# numpy.eye (N)
# shape: 3 dong, 3 cot
arr = np.eye(3)
print (arr)


#aivietnam.ai
# Tao 1 numpy array voi gia tri ngau nhien
import numpy as np
# numpy.random.random (size)
# shape: 2 dong, 3 cot voi phan tu co gia tri ngau nhien
arr = np.random.random((2,3))
print (arr)


#aivietnam.ai
import numpy as np
# creat an array
arr=np.arange(5)
print (arr)
# condittion
condittion = arr <3
out = np.where(condittion, arr, arr*2)
print (condittion)
print (out)


#aivietnam.ai
import numpy as np
arr=np.array([[1,2], [3,4]])
out=arr.flatten()
print (arr)
print (out)

#aivietnam.ai
import numpy as np
# tao list
l = [[1,2,3],
     [4,5,6]]
         
# tao ndarray 
data = np.array(1)
print('data\n',data)
print('data shape\n', data.shape)
# reshape
data_rs=np.reshape(data, (3,2))
print('data_rs\n',data_rs)
print('data_rs shape\n', data_rs.shape)

#aivietnam.ai
import numpy as np
# khoi tao numpy a_array
a_arr = np.array ([[1,2,3],
                  [5,6,7]])
         
# su dung silicing de tao mang b_array 
# bang cach lay tat ca cac dong va cot 1,2
b_arr = a_arr[:,   1:3]
print(a_arr)
print(b_arr)


#aivietnam.ai
import numpy as np
# khoi tao numpy a_array
a_arr = np.array ([[1,2,3],
                  [5,6,7]])
print('a_arr\n', a_arr)
# su dung silicing de tao mang b_array 
# bang cach lay tat ca cac dong va cot 1,2
b_arr = a_arr[:,   1:3]
print('b_arr\n', b_arr)
print('before changing\n', a_arr[0,1])
b_arr[0,0] = 99
print('after changing\n', a_arr[0,1])

