"""
4) Create two sets as follows 
A = 1,2,3,4,5
B = 18,19,20,21
Perform following operations on these :
a) Union
b) Intersection 
c) A-B
d) B-A
Display if 20 is a member of set B 
Do the following operations on the created set A	 
 (i) Display number of elements in the set A
 (ii) Add 365 to the set
 (iii) Add 12,13,14  to set B
 (iv) Remove 12 from set B
"""


A={1,2,3,4,5}
B ={18,19,20,21}
print(A,B) 
#Perform following operations on these :
#a) Union
print("A U B:", A.union(B))
#b) Intersection 
print("A Intersection B:", A.intersection(B))
#c) A-B
print("A difference B:",A.difference(B))
#d) B-A
print("A difference B:",B.difference(A))