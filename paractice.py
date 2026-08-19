# # #Functions
# # add=lambda a,b: a+b
# # print("addition : ",add(10,5))

# # def ad(a,b):
# #     return a+b
# # print(ad(10,5))

# # def addd(a,b=10):
# #     return a+b
# # print(addd(10))


# # def largest(*ss):
# #     return max(ss)
# # print(largest(1,2,3,4))

# # #lists tuples sets and dictionaries

# # list1=[1,2,3,4,5]
# # print(list1[1:4:2])

# # list1.append(6)
# # print(list1)

# # t=(1,2,3)
# # print(t)

# # set1={1,3,4,5}
# # set2={3,5,6,7}

# # print(set1|set2)
# # print(set1 & set2)
# # print(set1-set2)
# # #compherensions

# # evens=[x for x in range(20) if x%2==0]
# # print(evens)

# # word_len={w: len(w) for w in ["cat","elephant","dog"]}
# # print(word_len)

# #NUMPY FUNDAMENTALS
import numpy as np
# list=[1,2,3,4,5]
# np.array(list)

# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr.ndim)
# print(arr.dtype)

# arr=np.random.rand(5)
# print(arr)

# arr=np.random.randint(996,1000,size=5)
# print(arr)

# #indexing slicing reshaping

# arr=np.array([[1,2,3],[4,5,6]])
# print(arr[1,2])

# #columns sum
# m=np.array([[1,2,3],[4,5,6]])
# print(m.sum(axis=0))

# print(m[m>2])

# #paractice tasks

# arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# m=np.array(arr)
# print(m.shape)
# print(m.size)
# print(m.dtype)


# arr=np.random.randint(10,50,size=(5,5))
# print(arr)
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))

# import numpy as np
# arr = np.array([1, 2, 3, 4, 
#                    5, 6, 7, 8, 9,
#                    10,11, 12, 13, 14, 
#                    15, 16, 17, 18, 19, 20])

# # new_arr=arr.reshape(4,5)
# print(arr)

# print(new_arr[:,1:3])
# mean=sum(arr)/len(arr)
# print("mean",mean)
# print("values above mean",arr[arr>mean])

#using boolean masking
# arr = np.array([1, 2, 3, 4, 
#                  -5, 6, 7, -8, 9,
#                  10,11, -12, -13, 14, 
#                  15, -16, -17, 18, 19, 20])

# # arr[arr>0]=1
# # arr[arr<0]=0

# # print(arr)
# arr = np.where(arr < 0, 0, 1)
# print(arr)




#PANDAS
import pandas as pd
