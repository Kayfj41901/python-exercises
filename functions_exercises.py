#!/usr/bin/env python
# coding: utf-8

# In[22]:


#1
def is_two(betty):
    if betty == 2 or betty == "2":
        return True
    else:
        return False



# In[27]:


#2
def is_vowel(charlie):
    if charlie in ('aeiouAEIOU'):
        return True 
    else:
        return False



# In[66]:


def is_consonant2(abbba):
    if is_vowel(abbba):
        return False
    else: 
        return True



# In[29]:


#3
david = "v"
def is_consonant(david):
    if david not in ('aeiouAEIOU'):
        return True 
    else:
        return False



# In[33]:


#4
def cap(ella):
    if is_consonant(ella[0]):
        return ella.capitalize()



# In[67]:


#5
def calculate_tip(tip_percentage, bill_total): 
    return bill_total * tip_percentage




# In[35]:


#6
def apply_discount(original_price, discount_percentage):
    return original_price * (1 - discount_percentage)



# In[46]:


#7
def handle_commas(foxtrot):
    foxtrot = foxtrot.replace(',','')
    return foxtrot




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


# In[53]:


#9
def remove_vowels(x):
  for i in "aeiouAEIOU":
    x = x.replace(i,"")
  return x


# In[55]:


#10
bad_words = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonl]ocal", "not"]
#x[0] = not int or float
# possibly x = x.str.replace([{bad_words}, "    ")
###can't only contain digits 
def normalize_name(x):
    x = x.replace({bad_words}, '    ')
    strip(x)
    x = x.replace('  ', '__')
    for i in x:
        if i in "!@#$%^&*":
            x.replace(char, " ")
            return x
            


# In[68]:


#11
def cumulative_sum(ada):
    total = 0 
    result = []
    for i in ada:
        total += ada
        result.append(total)
    return result 


