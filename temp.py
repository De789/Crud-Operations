# def merge_array(x,y):
#     res=[]
#     i,j=0,0
#     while i <len(x) and j <len(y):
#         if x[i]<y[j]:         
#             res.append(x[i])
#             i+=1
#         else:
#             res.append(y[j])
#             j+=1
#     res.extend(x[i:])
#     res.extend(y[j:]) 
#     return  res
# print(merge_array([1,2,9],[3,0,7]))

# remove duplicates in a list:
# x=["a", "b", "a", "c", "c"]
# print(list(dict.fromkeys(x)))
# keys = ['a', 'b', 'c']
# print(dict.fromkeys(keys,values=[1,2,3]))


# def reverse_str(str):
#     if len(str)==1:
#         return str
#     else:
#         return str[-1]+reverse_str(str[:-1])
# print(reverse_str("Mahesh"))
 

# def free_item(n):
#     free=n//9
#     paid=n-free
#     return free 
# n = int(input("Enter the total items: "))
# print("The free items after buying", n, "are", free_item(n))
# nums = [1, 5.3, 321, 0, 1, 2]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

# words = ('morello', 'irk', 'fuliginous', 'crusado', 'seam')
# print(sorted(words,key=len,reverse=False))

import numpy as np
import pandas as pd

x=np.array([1,2,3])
y=np.array([2,3,4])
z=x+y
print(z)
# print(z.shape)
print(z.ndim)