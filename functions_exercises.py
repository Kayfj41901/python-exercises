#!/usr/bin/env python
# coding: utf-8

# In[22]:


#1
def is_two(betty):
    if betty == 2 or betty == "2":
        return True
    else:
        return False
print(is_two(5))


# In[27]:


#2
def is_vowel(charlie):
    if charlie in ('aeiouAEIOU'):
        return True 
    else:
        return False
print(is_vowel('f'))


# In[66]:


def is_consonant2(abbba):
    if is_vowel(abbba):
        return False
    else: 
        return True
print(is_consonant2('m'))


# In[29]:


#3
david = "v"
def is_consonant(david):
    if david not in ('aeiouAEIOU'):
        return True 
    else:
        return False
print(is_consonant('a'))


# In[33]:


#4
def cap(ella):
    if is_consonant(ella[0]):
        return ella.capitalize()
print(cap("max"))


# In[67]:


#5
def calculate_tip(tip_percentage, bill_total): 
    return bill_total * tip_percentage

print(calculate_tip( .22, 100))


# In[35]:


#6
def apply_discount(original_price, discount_percentage):
    return original_price * (1 - discount_percentage)
print(apply_discount(100, .38))


# In[46]:


#7
def handle_commas(foxtrot):
    foxtrot = foxtrot.replace(',','')
    return foxtrot


print(handle_commas('1,000,000'))


# In[52]:


#8
grade = 95
def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "c"
    elif grade >= 60 and grade <= 69:
        return "D"
    else: 
        return "F"
print(get_letter_grade(62))


# In[53]:


#9
def remove_vowels(x):
  for i in "aeiouAEIOU":
    x = x.replace(i,"")
  return x
print(remove_vowels('Harrison'))


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# In[55]:


#10
bad_words = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonl]ocal", "not"]
#x[0] = not int or float
# possibly x = x.str.replace([{bad_words}, "    ")
###can't only contain digits 
#just need to change to lowercase and order the code properly 
def normalize_name(x):
    x = x.replace({bad_words}, '    ')
    strip(x)
    x = x.replace('  ', '__')
    for i in x:
        if i in "!@#$%^&*":
            x.replace(char, " ")
            return x
            
print(normalize_name('%#&$%none KayBay'))


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[2]:


#11
def cumulative_sum(r):
    total = 0 
    result = []
    for i in r:
        total += i
        result.append(total)
    return result 

cumulative_sum(10)
#giving error message 'int' object is not iterable 


# In[ ]:




