"""
1) Lets create a student list named "members" with following names in it
Pratiksha,Kevin,Sachin,Yuvraj,Sania
Do the following operations on the created list 
 (i) Display number of elements in the members list
 (ii) Add "Ross" to the members collection 
 (iii) Add "David","Bret","Sanju"  to the members collection 
 (iv) Remove the third member from the collection 
 (v) Remove the last member from the collection 
 ( vi)  Display third, fourth and fifth element from the collection 
 """


members=['Pratiksha','Kevin','Sachin','Yuvraj','Sania'] 
print("---------------------start-------------------------") 
print("i. Display number of elements in the members list")
print("Members:",members)

print("--------------------------------------------------")
print("ii. Add 'Ross' to the members collection")
new_members= "Ross"
members.append(new_members)
print("Updated members list :", members)

print("--------------------------------------------------")
print("iii. Add 'David','Bret','Sanju' to the members collection ")
new_members1="David"
new_members2="Bret"
new_members3="Sanju"
members.append(new_members1)
members.append(new_members2)
members.append(new_members3)
print("Updated members list :", members)

print("--------------------------------------------------")
print("iv. Remove the third member from the collection")
members.remove("Sachin")
print("Updated members list :", members)

print("--------------------------------------------------")
print("v. Remove the last member from the collection")
members.remove("Sanju")
print("Updated members list :", members)

print("--------------------------------------------------")
print("vi. Display third, fourth and fifth element from the collection")
print("Display third ,fourth and fifth element from collection: ",members[2],members[3],members[4] )
print("------------------------end---------------------")