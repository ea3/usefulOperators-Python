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

d = {'mykey': 345}
print(345 in d.values())

mylist = [10,20,30,40,50,60]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist5 = [3,6,1,8,5,9,0]
shuffle(mylist5)
print(mylist5)
shuffle(mylist5)
print(mylist5)


from random import randint

print(randint(0,100))


result = input('Enter a number here: ')

print(type(result))


mystring = 'hello'
mylist = []
for letter in mystring:
	mylist.append(letter)

print(mylist)



mylist = [x for x in 'word']
print(mylist)



## LIST COMPREHENSION

mylist = [x**2 for x in range(0,11) if x % 2 == 0]
print (mylist)

# Fahrenheit conversion

celcius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(fahrenheit)

fahrenheit = []
for temp in celcius : 
	fahrenheit.append(((9/5)*temp + 32) )
print(fahrenheit)

mylist = []
for x in [2,4,6]:
	for y in [100,200,300]:
		mylist.append(x*y)

print(mylist)

st = "Print only the words that start with s in this sentence"
stSplit = st.split()
print(stSplit)

for word in stSplit:
	if word[0] == 's':
		print(word)

## print even number from 0 to 10 using range. 
print(range(0,11,2))



print([x for x in range(1,51) if x % 3 == 0])




##fizz BUZZ!!

for num in range(1,101):
	if (num % 3 == 0) and (num % 5 == 0) :
		print('FizzBuzz')
	elif (num % 3 == 0):
		print('Fizz')
	elif (num % 3 == 0):
		print('Buzz')
	else:
		print(num)










