#!/usr/bin/env python
# coding: utf-8

# In[11]:


input_value = input("값을 입력해주세요 : ")
input_temp = input_value.split()
num = int(input_temp[0])
value = list(map(int,input_temp[1:]))
sum_value = 0
for i in range(num):
    sum_value += (i+1) * (max(value))
    value.remove(max(value))
print("최솟값 : ", sum_value)

