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





# a = np.arange(6)
# a2 = a[np.newaxis, :]
# print(a2.shape)


# a = np.array([1, 2, 3, 4, 5, 6])

# # print(type(a.len))

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a)


c= np.zeros(3)
print(c)
