# # # EXCEPTIONS AND ASSERTIONS # # #
'''
1. Exceptions:
    - What happens when procedure execution has unexpected condition?
        Get an exception... to what was expected:
		Trying to access beyond list limits             -> IndexError
		Trying to convert an inappropriate type         -> TypeError
		Referencing a non-existing variable		-> NameError
		Mixing data types without coercion		-> TypeError
		Python can't parse types			-> SyntaxError
		Local or global name not found			-> NameError
		Attribute reference fails			-> AttributeError
		Operand doesn't have correct type 		-> TypeError
		Operand type okay. but value is illegal         -> ValueError
		IO system reports malfunction
					(e.g file not found)	-> IOError

    - What to do with exceptions:
        - Fail silentrly - the user gets no warning BAD BAD BAD!!!
        - Return and "error" value - what value to choose, complicates the code having to cxheck for a special value
        - Stop executing, raise an exception:
            - raise Exception("describtiove string")

    - Dealing with exceptions:
         try:
            # Some code
        except:
            print("Bug found (descriptive)")
        print('Outside')

    - Handling specifix exceptions:
        try:
            # some code
        except ValueError:
            print("Could not convert to a number")
        except ZeroDivisionError:
            print("Cannot devide by zero>")
        except:
            print("Someting went very wrong!!!")

    - Other exception:
        - else:
            Body of this is executed when execution of assotiated
            try body completes with no exceptions;
        - finaly:
            Body of this is always executed after try, else and except clauses even if they raise another error
            or executed a break, continue or return;
            It is useful for clean-up code that should be run no matter what else happened (e.g close a file)

2. Exceptions as Control Flow:
    - We could decide when to reain an Exception
        raise <exceptionName>(<arguments>) -> when unable to produce a consisten result
            
3. Assertions:
    Good Defensive Programming!!!
    - use and assert statement to raise an AssertionError exceptin if assumptions are not met!

    def avg(grades):

        assert not len(grades) == 0 'no grades data' -> raises and AssertionError if it is given an empty list for grades

        return sum(grades)/len(grades)

    - Asserttion don't allow a programmer to control response to unexpected conditions;
    - Ensure that execution halts whenever an expected condition is not met;
    - Used to check input
    - Can be used to check outputs
    - Check for violations of constaints on procedure (e.g. no duplicates in a list)

    - Where to use assertions:
        use as a suplement to testing;
        raise exceptions if users suplies bad data input;
        check type of arguments or values
        check that invariants on data structures are met;
        check constaints on return values;
        check for violations of constaints on procedure;



=====================================================================================================================================

+++ EXERCISES +++ 

Exercise 1:
    '1' / '2'               -> TypeError
    '1' / 2                 -> TypeError
    int('1') / 2.0          -> No error
    mylist = [10, 20, 30]
    mylist.index(11)        -> ValueError
    A=2
    3*a                     -> NameError

Exercise 3:
def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

Exercise 4:
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers

normalize([0, 0, 0]) -> Assertion error: Cannot divide by 0
'''
