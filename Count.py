# Python program to count the number of occurrence 
# of a word in the given string given string 

def countOccurences(str, word): 
	
	# split the string by spaces in a 
	a = str.split(" ") 

	# search for pattern in a 
	count = 0
	for i in range(0, len(a)): 
		
		# if match found increase count 
		if (word == a[i]): 
		count = count + 1
			
	return count	 

# Driver code 
str ="Python is most trending programming language"
word ="portal"
print(countOccurences(str, word)) 
