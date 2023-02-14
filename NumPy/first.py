import numpy as np

l = [1, 2, 3, 4]
a = np.array([1, 2, 3, 4])


# # ------basic operaions------
#
# l = l + [4]  # is same as   l.append(4)
# # l = l + 4    is not possible as we can't add the integer value to a list
# a = a + 4  # is same as a = a + np.array([4])
#
# l = l * 2  # it duplicates the times
# a = a * 2  # it multiply the times
# print(l, a)
#
# # maths operations
# print(np.sqrt(a))
# print(np.log(a))
#
# # the below are used to get information about the array
# print(a.shape)  # gives the number of rows and coloum
# print(a.dtype)
# print(a.ndim)
# print(len(a))
#
# # ------- end of basic operations----





# # -----dot product-----
#
#
# # using list
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# dot = 0
# for i in range(len(l1)):
#     dot += l1[i] * l2[i]
# print(dot)
#
#
# # using np-array
# a1 = np.array([1, 2, 3])
# a2 = np.array([4, 5, 6])
#
# #direct method
# dot = np.dot(a1, a2)
# print(dot)
#
# # long approch
# pro = a1*a2
# dot = np.sum(pro)
# print(dot)
#
# #shorthand
# dot = a1 @ a2
# print(dot)
# # ---end-of-dot product---



# # --- multi dimensional  array---
#
#
# ma = np.array([[1,2,3],[4,5,6]])
# print(ma.shape)
# print(ma.dtype)
# print(ma.ndim)
# print(len(ma))

# [row , coloum]
# ma[r, c]    #specific element
# ma[r, :]    #specific row
# ma[:, c]    #specific colomn

# print(ma.T)                     #transpose
# # np.linalg.inv(square-array)   #used to inverse a matrix
# # np.linalg.det(square-array)   #used to find thd determinate of matrix
# print(np.diag(ma))              # makes a list of diagonal element
#
#
# # --- end-of-multi dimensional  array---



# #---- reorganising array-----
# before =np.array([[1,2,3,4],[5,6,7,8]])
# # print(before)
#
# after = before.reshape(1,8)
# # print(after)
#
# # stacking vectors
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
# print(np.vstack([v1,v2,v1]))# vertical stacking
# print(np.hstack([v1,v2,v1]))# horizontal stacking
#
#
# h1 =np.ones((4,2))
# print(h1)
# h2 = np.zeros((4,2))
# print(h2)
# print("------------------------")
# print(np.vstack([h1,h2]))
# print("------------------------")
# print(np.hstack([h1,h2]))
#
#
# #---- end-of- reorganising array-----


# # -----miscellaneous----
#
# #loading the data from file
# filedata = np.genfromtxt('data.txt', delimiter=',')# it is used to get the data from the txt file
#
# filedata.astype('int32')# this does not mack changes to the original file , which means that it is the copyof filedata with the int32
# filedata = filedata.astype('int32')
#
# #Boolean masking and advanced indexing
# # with the above eg
# filedata>50 # upon printing this, there is a array of boolean value
# filedata[filedata>50]#this gives the array of numbers grater than 50
#
# np.any(filedata>50,axis=0)
#
#
#
#
# ex = np.array([00,10,20,30,40,50,60,70,80,90])
# print(ex<50)
# print(ex[ex<50])
#
# # ---- end-of miscellaneous


# a = np.arange(6)
# a2 = a[np.newaxis, :]
# print(a2.shape)


# a = np.array([1, 2, 3, 4, 5, 6])

# # print(type(a.len))

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a)


# c= np.zeros(3)
# print(c)
# print("------------------------")


