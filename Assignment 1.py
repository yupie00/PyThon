#!/usr/bin/env python
# coding: utf-8

# ## Task 1

# #### 1. Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[61]:


1+1


# #### 2.Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in acomma-separated sequence on a single line

# In[54]:


for i in range(2000,3201):
    if(i%7 == 0 and i%5 != 0):
        #print(type(i)) --> integer
        print(i, end = ",")
###But type of data here is NoneType


# #### Another Method

# In[55]:


num = []
for i in range(2000,3201):
    if(i%7 == 0 and i%5 !=0):
        num.append(str(i))
print(','.join(num))


# In[ ]:





# ####  3.Write a Python program to accept the user's first and last name and then getting them printed inthe the reverse order with a space between first name and last name

# In[4]:


fname = input("provide first name ")
lname = input("provide last name ")

print("The name in reverse order is :", lname, " " , fname )


# In[ ]:





# #### 4.Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r3

# In[50]:


d = 12
vol = (4/3) * (22/7) * (d/2)**3
print("The volume of the sphere is : ", vol)


# In[ ]:





# ## Task 2

# #### 1.Write a program which accepts a sequence of comma-separated numbers from console andgenerate a list.

# In[23]:


input("Please provide a list of comma seperated numbers of your choice : ").split(",")


# In[ ]:





# #### 2.Create the below pattern using nested for loop in Python.

# In[36]:


n = int(input("Enter the no of lines "))
for i in range(n):
    print("* " *(i+1))
for i in range(n-1):
    print("* "*(n-1 -i))
    


# In[ ]:





# #### 3.Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:Input word: AcadGildOutput: dilGdacA

# In[12]:


word = input()
list_word = list(reversed(word))
print("".join(list_word))


# In[ ]:





# #### 4.Write a Python Program to print the given string in the format specified in the ​sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into aSOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to allits citizens

# In[16]:


print("WE, THE PEOPLE OF INDIA, \n \t having solemnly resolved to constitute India into aSOVEREIGN, \n \t \t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n \t \t  and to secure to all its citizens")


# In[ ]:




