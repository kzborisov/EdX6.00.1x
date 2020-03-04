s = 'azcbobobegghakl'
vowels_list = ['a', 'e', 'i', 'o', 'u']

counter = 0

for vowel in vowels_list:
    print('looking for ' + vowel)
    for char in s:
    	if vowel == char:
    		counter += 1

print(counter)
