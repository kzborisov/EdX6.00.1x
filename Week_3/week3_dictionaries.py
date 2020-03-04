# ## DICTIONARIES ###
# Dictionaries are not ordered!!!
# Example, How to store student infor:
# 	def get_grade(student, name_list, grade_list, course_list):
# 		i = name_list.index(studet)
# 		grade = grade_list[i]
# 		course = course_list[i]
# 		return (course, grade)

# The above example is messy if ahve a lot of different info to keep track of
# Must maintain may lists and pass them as arguments
# Must always index using integers
# must remember to change multiple lists



# A beeter and cleaner way is to use
# 			DICTIONARIES
# They store pairs of data: a key and a value!

# 	my_dict = {}
# 	grades = {'Ana':'B','John': 'A+','Denise':'A'}
# 	grades['John'] => 'A+'
# 	grades['Ana']  => 'B'
# 	grades['sylvan'] => key error
# 	grades['sylvan'] = 'A'
# 	grades['sylvan'] => 'A'
# 	'John' in grades:
# 		True
# 	del(grades['Ana'])
# 	grades => {'John': 'A+','Denise':'A','sylvan':'A'}

# Look up the set of keys:
# 	Get an itterable that acts like a tuple of all keys/values!
# 	grades.keys() 	=> dict_keys(['John',..........])
# 	grades.values() => dict_values(['A','A+',......])

# Values: they can be anything!!!!!!
# Keys: must be unique, immutable(int,float,string,tuple,bool(hashable objects))!!!!!
# No order to key or values!!!!!

# Example 3: Function to analyze song lyrics:
# 1. Create a frequency dictionary mapping str:int
# 2. find words athat occurs the most and how many times
# 3. find the words that occur at least X times.
#
# Creating a dictionary:
# def lyrics_to_frequencies(lyrics):
#		myDict = {}
#		for word in lyrics:
#			if word in myDict:
#				myDict[word] += 1
#			else:
#				myDict[word] = 1
#		return myDict
#
# def most_common_words(freqs):
#	values = freqs.values()
#	best = max(values)
#	words = []
#	for k in freqs:
#		if freqs[k] == best:
#			words.append(k)
#	return (word,best)
#
# def words_often(freqs, minTimes):
#	result = []
#	done = False
#	while not done:
#		temp = most_common_words(freqs)
#		if temp[1] >= minTimes:
#			result.append(temp)
#			for w in temp[0]:
#				def(freqs[w]) # remove word from dictionary
#		else:
#			done = True
#	return result
# 
# EXERCISE - HOW MANY TIMES:
# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#     returns: int, how many values are in the dictionary.
#     '''
#     # Your Code Here
#     sum = 0
#     for i in aDict.values():
#         sum += len(i)
#     return sum
#
# EXERCISE - BIGGETS:
#
# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#     returns: The key with the largest number of values associated with it
#     '''
#     # Your Code Here
#     counter = 0
#     result = None
#     if aDict == {}:
#         return result
#     else:
#         for i in aDict.keys():
#             if len(aDict[i]) > counter:
#                 result = i
#     return result
#
#
# # # FIBONACCI RECURSIVE CODE # # #
# def fib_efficient(n,d):  
# 	if n in d:
#		return d[n]
# 	else:
#		ans = fib_efficient(n-1,d) + fib_efficient(n-2,d) # Method called memoization!!!
#		d[n] = ans
#		return ans
#
# Global Variables:
# 	can be dangerous to use as they break the scope of variables by function call
#	and allow for side effects of changing variable values in ways that affect other computations
#
#