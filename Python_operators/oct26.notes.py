
# coding: utf-8

# In[ ]:




# In[2]:

n = 15
print(n)
print(type(n))


# In[5]:

print(0xf)
print(0b1111)
print(0o17)


# In[6]:

n = 15
print(bin(n))
print(hex(n))
print(oct(n))


# In[7]:

print(int('f', 16))
print(int('1111', 2))
print(int('17', 8))


# In[9]:

# float
print(0.003)
print(3e-3)
print(3E-3)


# In[14]:

# complex number 
n = 3+4j
print(n)
print(type(n))
print(n.real)
print(n.imag)
print(n.conjugate())
print(n ** n)


# In[18]:

print(5.8 / 2)
print(5.8 // 2)  # floor division 
print(5.8 // 2 + 1)  # ceil division 


# In[21]:

n = 5.6

print(n >= 3 and n <= 7)
print(not 3 <= n <= 7)


# In[22]:

5 & 2


# In[24]:

"""
if else conditional operator
=====================
syntax :-

true-part if test-condition else false-part 
"""

n = 14
result = n ** 2 if n > 5 else n ** 3
print(result)


# In[27]:

a, b, c = 12, 3, 23.21

result = a if a > b and a > c else (b if b > c and b > a else c) 
print(result)


# In[29]:

r = range(10)
print(r)
print(type(r))
print(list(r))


# In[30]:

r = range(10)
print(list(r))
print()
r = range(1, 10)
print(list(r))
print()
r = range(1, 10, 2)
print(list(r))
print()


# In[31]:

r = range(10, 1, -2)
print(list(r))
print()


# In[35]:

# immutable object
s = 'python'
# s[2] = 'T'
print(s)


# In[36]:

# regular vs raw string

file_path = 'c:\templates\neo\rules\blames\temp.txt'
print(file_path)


# In[37]:

file_path = r'c:\templates\neo\rules\blames\temp.txt'  # raw string
print(file_path)


# In[42]:

# doc string, multiline formatted content

s = '''
   {}
  2 2
 3 {} 3
  4 4
   {}
'''
data = 'x'
print(s.format(data, .3, 'z'))


# In[43]:

# indexing 

s = 'perl'
print(s[0])
print(s[1])
print(s[2])
print(s[3])


# In[46]:

s = 'perl'  # -ve indexing
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])


# In[65]:

s = 'perl\'andpython'
print(s[:4])
print(s[3:7])
print(s[-6:])
print(s[:])
print(s[1:-1])
print(s[-6])


# In[76]:

# name[start-index:ex-of-end-index:frequency]

s = 'perlandpython'
print(s[::1])
print(s[::-1]) 
print()
print(s[::2])
print(s[1::2])


# In[69]:

s = 'perlandpython'
print(list(s))
items = [1.1, 'pam', 'eva', 3.4]
print(items)
print(items[1:-1])


# In[77]:

print(ord('A'))


# In[78]:

print(chr(65))


# In[79]:

s = 'this is a sample string in python'
print('sam' in s)


# In[89]:

s = 'this is a sample string in python'
items = s.split()
print(items)
print('is' in items)  # contains 

for item in items:
    if 'sam' in item or 'str' in item:
    #if ['str', 'sam'] in item:
        print(item)


# In[93]:

items = list(range(1, 153))
print(items)
print()
print(1113 in items)


# In[95]:

for item in range(5):
    print(item)


# In[96]:

bool('peter')


# In[97]:

bool('')


# In[98]:

bool(-123.21)


# In[99]:

bool(1)


# In[105]:

print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool(0+0j))
print(bool([]))  # list
print(bool({}))  # dict
print(bool(()))  # tuple
print(bool(set()))  # set
print(bool(None))
print(type(None))


# In[ ]:



