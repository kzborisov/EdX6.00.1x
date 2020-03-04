### TUPLES ###
# aTup = ('I', 'am', 'a', 'test', 'tuple')
# def oddTuples(aTup):
#     '''
#     aTup: a tuple
    
#     returns: tuple, every other element of aTup. 
#     '''

#     new_tup = ()
#     for t in range(len(aTup)):
#     	if t % 2 == 0:
#     		new_tup = new_tup + (aTup[t],)
#     return new_tup

### LISTS & LIST OPERATIONS ###
#
# 1. ADDITION:
#	- append() -> Mutates the list!!!
#		What is the dot?:
#			-Everything in Python is and object(including lists)
#			- objects have data;
#			- objects also have methods and functions
#			- access this information by object_name.do_something();
#
# 2. Concatenate:
#	- list1 + list2 = list3(contains both list2 and list3)
#		by concatenation list1 and list2 are not changed
#
# 3. Remove:
#	- del(list1[3]) : deletes the 3th elemth of the list
#	- .pop() -> removes element at the end of the list and returns it
#	- .remove(3) -> removes first occurance of 3m if not in the list returns and error
#
# 4. Split:
#	- .split() -> split a string on a character parameter, splits on spaces if called without parameter
# 		s = 'I love Python'
#		s.plit() -> ['I','love','Python']
#	- .join() -> turns a lsit of characters into a string:
#		L = ['a','b','c']
#		_.join(L) -> "a_b_c"
#
# 5. Sorting:
#	- sorted()   -> special function, returns sorted list, DOES NOT MUTATE IT!!!
#	- .sort()    -> mutates the list!
#	- .reverse() -> mutates the list!
#
#### MUTATION,ALIASING AND CLONING ###
#
# 1. Lists are an object in memory.
# 2. ALIASES:
# 	- warm = ['red','yellow','orange']
#	- hot  = warm
#	- hot.append('pink') -> also changes hot as well as warm!!!
#	-!!! cool = ['blue','green','grey']
#	-!!! chil = ['blue','green','grey'] -> cool and chill are the same but are pointing to seperated location in memory
#
# 3. Cloning a list:
#	- cool  = ['blue','green','grey']
#	- chill = cool[:] -> chill is exact copy of cool! Again pointing to different memory location
#
# 4. SIDE EFFECTS:
#    LIST OF LIST O
#	- warm = ['yellow','orange']
#	- hot = ['red']
#	- brightcolors = [warm]
#	- brightcolors => [['yellow','orange']]
#	- brightcolors.append(hot) => [['yellow','orange'], ['red']]
#	- hot.append('pink')
#	- hot 			=> ['red',pink]
#	- brigthcolors  => [['yellow','orange'], ['red',pink]]
#	
# 5. MUTATION AND ITERATION:
#	AVOID MUTATING A LIST WHILE ITERATING IT!!!
#	- def remove_dups(L1,L2):
#		for e in L1:
#			if e in L2:
#				L1.remove(e)
#		=> Python uses itnernal counter to keep track of index it is in the loop
#		Mutating changes the list length but Python doesn't update the counter;
#
#	The above could be done by cloning the list:
#	- def remove_dups(L1,L2):
#		L1_copy = L1[:]
#		for e in L1_copy:
#			if e in L2:
#				L1.remove(e)
#
### FUNCTIONS AS OBJECTS, DICTIONARIES ###
# 1. FUNCTIONS:
#	Functions are first class objecst:
#		- it has a type
#		- can be element of data structure like lists
#		- can appear in expressions(assignments)
#
#	example:
#	- def applyToEach(L,f):
#	- '''Assuming that L is a list
#	- 	and f in a function
#	- '''
#	-	for i in range(len(L)):
#	-		L[i] = f(L[i])
#	- L = [1,-2,3.4]
#	- applyToEach(L,abs) => [1,2,3.4]
#	- applyToEach(L,int) => [1,2,3]
#	- applyToEach(L,fact)=> [1,2,4]
#	- applyToEach(L,fib) => [1,2,13]
#
#	The other way aroung:
#	- def applyFunc(L,x):
#	- '''Assuming that L is a list
#	- 	of functions to x(number)
#	- '''
#	-	for f in L:
#	-		print(f(x))
#
#	applyFunc([abs,int,fact,fib],3)
#
# 2.GENERALIZATION OF HOPS (Higher order procedure) => map
#	map(abs,[1,-2,3,-4]) => gives back a structure (iterable) that needs to be walked down
#							to get the results. 
#	=> for elt in map(abs,[1,-2,3,-4]):
#			print(elt)
#		[1,2,3,4]
#
#	General form - any n-ary function and n collections of arguments:
#	- L1 = [1,28,36]
#	- L2 = [2,57,9]
#	- for elt in map(min,L1,L2):
#			print(elt)
#		=> [1,28,9]
# 


# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])

# Assume that
# testList = [1, -4, 8, -9]

# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList
# has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated
# value. You may need to write a simple procedure in each question to help with this process.
#

# Your Code Here
def absolute(a):
    return abs(a)

applyToEach(testList, absolute)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
print(applyEachTo([inc, square, halve, abs], -3))