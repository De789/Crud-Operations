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

# import numpy as np
# import pandas as pd

# x=np.array([1,2,3])
# y=np.array([2,3,4])
# z=x+y
# print(z)
# print(z.shape)
# print(z.ndim)

# chars = tuple('hello')
# print(chars)
# print(chars[0:3])

# details = ('2024-10-25', 'car', 2346)
# purchase_date,brand,price=details
# print(f"Purchase date :{purchase_date}")
# print(f"Purchase model:{brand}")
# print(f"Price :{price}")

# values = ('first', 6.2, -3, 500, 'last')
# x,*y=values
# print(x)
# print(y)
# x,*y,z=values
# print(x)
# print(y)
# print(z)

# nums=(1,2,3)
# for i in nums:
#     print(f"The square of the number is:{i**2}")
# for t in enumerate(nums):
#     print(f"T is {t}")

# odd=(1,2,3)
# even=(4,5,6)
# for i,j in zip(odd,even):
#     print(i+j)
# x=(1,1,2,3,3,4,5,5,55,65,6)
# print(x.__len__())


# marks = {'Rahul': 86, 'Ravi': 92, 'Rohit': 75, 'Rajan': 79}
# print(marks.get("Rahul"))
# print(marks.get("Sam",8))
# marks.update({"name":"Mahesh"})
# print(marks)
# # for k in marks:
# #     print(k,":",marks[k])


# name="Mahesh anant Patil"
# parts=name.split()
# print(parts)

# def reverse_str(x):
#     parts=x.strip.split()
#     if len(parts)==2:
#         parts[0],parts[1]=parts[1],parts[0]
#     return "".join(parts)
# print(reverse_str(x))



# def flatten_filter(l):
#     result=[]
#     for item in l:
#         if isinstance(item,list):
#             result.extend(flatten_filter(item))
#         elif isinstance(item,str):
#             result.append(item)
#     return result

# data = [1, [2, 'a', [3, [4, 'b'], 5], 'c'], 6, ['d', [7, 8]], 9]
# print(flatten_filter(data))
# output :['a', 'b', 'c', 'd']            

# books=[]
# books.insert(1,"baluta")
# print(books)
# books.extend(["name","dame"])
# print(books)
# books.append("Sagar")
# print(books)


# import random
# items = ['car', 20, 3, 'jeep', -3.14, 'hi']
# random.shuffle(items)
# print(items)

# def get_even(i):
#     new=[]
#     for item in i:
#         if item %2==0:
#             new.append(item)
#     return new
# print(get_even([11,2,32,33,4]))
