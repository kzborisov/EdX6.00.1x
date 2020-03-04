# # # TESTING AND DEBUGING # # #
'''
1. We aim for high quality!
	- Testing
		Comparing input and outputs
		How can I break my program?
	- Defensive Programming (defining what I expect to come in):
		Write specifications for functions (add docstrings and check the expected input/output)
		Write modular programs
		Check the conditions for thos input/outputs
	- Eliminate source of bugs - debugging!

2. Set yourself up for easy testing and debugging:
	- Break program into modules that can be tested and debuged individually
	- Document constraint on modules:
		What do you expect the input and output to be?
	- Document assumptions - thinking process etc.

	!"Motherhood and apple pie" approach : something that cannot be questioned because it appeals to
	universally-held wholesome values!

3. When are you ready to test?:
	- Ensure code runs:
		Remove syntax errors
		Remove static semantic errors
		Python interpreter can usually find these for you
	- Have a set of expected results:
		An input set
		For each input, the expected output

3. Clases of Tests:
	- Unit testing:
		Validate each piece of program
		Testing each function separately
	- Regression testing (testing again after each fix):
		Add test for bugs as you find them in a function
		Catch reintroduced errors that were previously fixed
	- Integration testing:
		Each of the piece is handing off information correctly
		Does overall program work?
		Tend to rush to do this

4. Testing Approaches:
	- Intuition about natural boudaries to the problem.
	- If no natural partions, might do random testing.
		Probability that code is corret increases with more tests
	- Black Box Testing:
		Explore paths through specification;
		Design without looking at the code;
		Can be done by somebody other than the implementer to avoid some biases;
		Testing can be reused if implementation changes
		Paths through specification: 
			Build test cases in different natural space partitions;
			Also consider boundary conditions (empty lists, singleton list, large numbers, small numbers);

	-Glass Box Testing:
		Explore all paths through the code itself.
		Use code directly to guid the design of test case;
		Caled path0complete if every potention path through the code is tested at least once;
		What are some drawbacks of this type of testing?
			Can go through loops arbitrarily many times;
			Missing paths
		Guidelines:
			Branches    - exercise all parts of a conditional
			For loops   - loop not entered;
					    - body of loop executed exactly once;
					    - body of loop executed mroe than once;
			While loops - sam as for loops, cases that catch all ways to exit loop;

5. Bugs:
	- Isolate the bugs;
	- Eradicate the bugs;
	- Retest until code runs correctly

	HISTORY :):
		September 0th 1947 - one of the earliest compiters was build at Harvard called 
		'Mark II Aiken Relay'. It was a vacuum tubes and electronic relays and other very large-scale
		electronic components. 
		Some of the functions were not working and as they open up one of the vacuum tubes that was in the computer
		and inside they found that a moth had flown into it and had shortened out the connection.

	- Overt vs Covert Bugs:
		Overt  - has an obviuos manifestation - code crashes or runs forever;
		Covert - has no obvious manifestation - code return a value, which may be incorrect but hard to determine;

	- Persistent vs Intermittent:
		Persistent   - occurs every time the code is run;
		Intermittent - only occurs some times, even if run on the same input(external factors -time, web, etc);

	- Categories of Bugs:
		Overt and Persistent:
			Obvious to detect;
			Good programmers use defensive programming to try to ensure that if error is made, bug will fall into this category;
		Overt and Intermittent:
			More frustrating, can be harder to debug, but if conditons that prompt bug can be reproduced;
		Covert:
			Highly dangerous, as users may not realise answers are incorect until code has been run for long time;

6. Debugging:
	- Steap learning curve
	- Goal is to have a bug-free program
	- Tools:
		Build in to IDE and Anaconda
		Python Tutor
		print statement - when we enter a function, result, halfway through the code, expected values, etc
		use your brain, be systematic in your hunt
	- Logic Errors:
		Think before start writing new code;
		Draw pictures, take a break;
		Explain the code - a rubber ducky;
	- Study program code:
		Ask how did I get tge unexpected result;
		Don't ask what is wrong;
		Is it part of a family;
	- Scientific method:
		Study available data;
		Form hypothesis as to what may be cause the particular error;
		Repeatable experiments to test the hypothesis;
		Pick simplest input to test with;

	DO NOT:
		- write the entire program-> test entrire program -> debug entire program!!!
		- Change the code, remember where the bug was; test the code, forget where the bug was or what change you made!
	DO:
		- Write Fucntion -> Test the function, debug it -> write a function -> test and debug it -> Do the integration testing!
		- Backup Code; Change code; write down potential bug in a comment; test code; comapre new version with old version!

7. Debuggung Example:
	- Debugging skills;
		treat as a search problem: looking fo explanation for incorrect behavior
		 	Study available data - both correct test cases and incorrect ones;
			Form and hypothesis consistent with the data;
			Design and run a repeatable experiment with potential to refute the hypothesis
			Keep record of experiments performed: use narrow range of hypothesis;
	- Debuggind as Search:
		Want to narrow down space of possible sources of error;
		Design experiments that expose intermediate stages of computation (use print statements!),
		and use results to further narrow search!
		Binary search is a powerfull tool for this!!!
			-> Insert a print statement in the middle of the code;
			-> This way you can find out where exactly is the bug in your code - before or after the print statement, if it is before,
			   you can move the print above and vice verse and so on.
	
	- SOME PRAGMATIC HINTS:
		Look for the ussual suspects;
		Ask why the code is doing what it is, not why it is not doing what you want;
		The bug is probably not where you think it is - eliminate locations;
		Explain the problem to someone else;
		Don't believe the documentation;
		Take a break and come abck to the bug after;

=====================================================================================================================================

+++ EXERCISES +++ 

Exercise 1:

def size(aSet):
   """
   aSet is a collection of objects, which might be empty.
   Objects are assumed to be of the same type.
   """

	Test for:
		Empty set;
		Set of size 1;
		Set of size greater than 1;

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 2:

def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   
   Test for:
		set1 is an empty set; set2 is an empty set;
		set1 is an empty set; set2 is of size greater than or equal to 1;
		set1 is of size greater than or equal to 1; set2 is an empty set;
		set1 and set2 are both nonempty sets which do not contain any objects in common;
		set1 and set2 are both nonempty sets which contain any objects in common;

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 3:

def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger
	
	Test for:
		maxOfThree(2, -10, 100), maxOfThree(7, 9, 10), maxOfThree(6, 1, 5), maxOfThree(0, 40, 20)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 4:

def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)

	Test for:
		union('','abc'), union('a','abc'), union('ab','abc'), union('d','abc')
		len(set1) == 0 - matched by the test union('', 'abc')
		set1[0] in set2 - matched by the test union('a', 'abc')
		set1[0] not in set2 (this is the else: of the conditional) - matched by the test union('d', 'abc')
		In addition, because union is a recursive function, we should make sure our test set considers a recursion depth of 0, 1, 
		and many. In this case, recursion depth is covered by some of the tests we've already chosen:

		Recursion depth = 0 - matched by the test union('', 'abc')
		Recursion depth = 1 - matched by the tests union('a', 'abc'), union('d', 'abc')
		Recursion depth > 1 - matched by the test union('ab', 'abc')

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 5:

def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count	

	Test for:
		In glass box testing, we try to sample as many paths through the code as we can. In the case of loops, we want to sample three general cases:
			Not executing the loop at all.
			Executing the loop exactly once.
			Executing the loop multiple times.

			foo(10, 3), foo(1, 4), foo(10, 6)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 6:

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count

When we call:
print(integerDivision(5, 3))

We get the following error:
File "temp.py", line 9, in integerDivision
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
Your task is to modify the code for integerDivision so that this error does not occur.

Solution:
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
  ->count = 0 
    while x >= a:
        count += 1
        x = x - a
    return count

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 6:

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)

When we call:
	rem(2,5)
the shell returns 2. 
When we call
	rem(5, 5)
the shell returns 0. 
But when we call
	rem(7, 5)
the shell does not return anything!


Solution:
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
  ->   return rem(x-a, a)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Exercise 7:

def f(n):
   """
   n: integer, 
   n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

When we call f(3) we expect the result 6, but we get 0.
When we call f(1) we expect the result 1, but we get 0.
When we call f(0) we expect the result 1, but we get 0.

Solution:
def f(n):
   """
   n: integer, 
   n >= 0.
   """
   if n == 0:
 ->   return 1 # 
   else:
      return n * f(n-1)
Explanation:
This is a function known as factorial - the product of all the numbers from 1 through n.
The base case of factorial is 0! = 1, but the original code was written with the base case 0! = 0
Before:
f(3)=3∗f(2)
	=3∗(2∗f(1))
	=3∗(2∗(1∗f(0)))
	=3∗(2∗(1∗(0)))
	=3∗(2∗(0))
	=3∗(0)0 
The fixed version of the code puts the line return 1, instead of return n, when n == 0. We can see that this modified version of the code fixes the factorial function by again writing out the recursive expansion of f(3):
After:
f(3)=3∗f(2)
	=3∗(2∗f(1))
	=3∗(2∗(1∗f(0)))
	=3∗(2∗(1∗(1)))
	=3∗(2∗(1))
	=3∗(2)6
'''