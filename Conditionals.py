Conditionals 

conditionals: allow us to execute code conditionally 
loops: allow us to execute code repeatedly 

The if statement is a condition that evaluates to a boolean value followed by a colon (:), the body of the statement indented by 4 spaces 

D=[[12,10,13,14,13,-2,17,20,19,14],[9,-5,11,20,10,16,13,22,15,12]]

for i in D: 
    for j in range(len(i)):
        if i[j] < 0:
            i[j]=0

for i in data_science_students: 
    for j in i:
        print(sum(j)) 


import math 
