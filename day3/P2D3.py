"""
2) Lets create a dictionary named "Capitals" of country and their capitals 
India : New Delhi
USA : Washington DC
Nepal: Kathmandu
Ukraine : Kyiv
Do the following operations on the created dictionary
 (i) Display number of elements in the Capitals collection
 (ii) Add Afghanistan: Kabul  to the Capitals collection 
 (iii) Add "Albania:	Tirana
			Algeria:	Algiers
			Andorra:	Andorra la Vella
			to the Capitals collection 
 (iv) Remove the USA from the collection 
"""


Capitals=[  'India : New Delhi',
            'USA : Washington DC',
            'Nepal: Kathmandu',
            'Ukraine : Kyiv'        ] 

print("---------------------start-------------------------") 
print("i. Display number of elements in the Capitals collection")
print("Capitals collection:",Capitals)

print("----------------------------------------------------") 
print("ii. Add Afghanistan: Kabul  to the Capitals collection ")
new_capital= "Afghanistan: Kabul"
Capitals.append(new_capital)
print("Capitals collection:",Capitals)


print("----------------------------------------------------") 
print("iii.  Add 'Albania:	Tirana', 'Algeria:	Algiers','Andorra:Andorra la Vella'to the Capitals collection ")
new_capital1="Albania:	Tiranav"
new_capital2="Algeria:	Algiers"
new_capital3="Andorra:Andorra la Vella"
Capitals.append(new_capital1)
Capitals.append(new_capital2)
Capitals.append(new_capital3)
print("Capitals collection:",Capitals)

print("--------------------------------------------------")
print("iv. Remove the USA from the collection")
Capitals.remove("USA : Washington DC")
print("Updated members list :", Capitals)
print("----------------------END----------------------")