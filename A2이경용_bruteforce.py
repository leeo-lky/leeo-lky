#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_value = input("값을 입력해주세요: ")
input_temp = input_value.split()
num = list(map(int,input_temp[:2]))
value = list(map(int,input_temp[2:]))
sum_result = 0
for i in range(num[0]):
    for j in range(i+1,num[0]):
        for k in range(j+1,num[0]):
            sum_temp = value[i] + value[j]+ value[k]
            if  (sum_temp <= num[1]) and (sum_temp > sum_result):
                sum_result = sum_temp
print("최대 가까운 값: ", sum_result)
            


# In[ ]:




