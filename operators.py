# range key word. . 
mylist = [1,2,3]

for num in range(0,10,2):
	print(num)


print(mylist)

#print(range(0,11,2))

#index_count = 0
#word = 'abcde'


#for letter in word:
#	print(word[index_count])
	#index_count += 1

###################################  ENUMERATE key word. 
word = 'abcde'

for index, letter in enumerate(word):
	print(index)
	print(letter)


mylist1 = [1,2,3,4]
mylist2 = ['a', 'b', 'c', 'd']
print(zip(mylist1, mylist2))
for item in zip(mylist1, mylist2) : 
	print(item)


x = 3
print(x in [1,2,3])


print('z' in 'there is a party in my tummy')

print('mykey' in {'mykey':234})






