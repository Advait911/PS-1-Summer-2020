#Creating a Tuple 
#with Mixed Datatype 
Tuple1 = (5, 'Welcome', 7, 'Advait') 
print("\nTuple with Mixed Datatypes: ") 
print(Tuple1) 

#Creating a Tuple 
#with nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'Advait') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 

#Creating a Tuple 
#with repetition 
Tuple1 = ('Advait',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 

#Creating a Tuple 
#with the use of loop 
Tuple1 = ('Advait') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
	Tuple1 = (Tuple1,) 
	print(Tuple1) 
