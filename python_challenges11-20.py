def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase. >>> flip_case('Aaaahhh', 'a') 'aAAAhhh'  >>> flip_case('Aaaahhh', 'A') 'aAAAhhh'
 >>> flip_case('Aaaahhh', 'h') 'AaaaHHH'    """
    new_string=""
    compare = to_swap.upper()
    
    for char in phrase:
        if char.upper() == compare:
            char = char.swapcase()
        new_string += char
    print(new_string)
    
def multiply_even_numbers(nums):
    """Multiply the even numbers. >>> multiply_even_numbers([2, 3, 4, 5, 6]) 48 >>> multiply_even_numbers([3, 4, 5]) 4 
    If there are no even numbers, return 1. >>> multiply_even_numbers([1, 3, 5]) 1 """
    total = 1
    for num in nums:
        if num % 2 == 0:
            total = total * num

    return total

def capitalize(phrase):
 """Capitalize first letter of first word of phrase. >>> capitalize('python') 'Python' >>> capitalize('only first word') 'Only first word' """
    x = phrase.capitalize()
    print(x)
    
def compact(lst):
    """Return a copy of lst with non-true elements removed.
 >>> compact([0, 1, 2, '', [], False, (), None, 'All done']) [1, 2, 'All done']
    """
    newlist = []

    for x in lst:
        if bool(x) is not False:  #is not runs faster than == or != 
            newlist.append(x)

    print(newlist)
    
    
def intersection(l1, l2):
    """Return intersection of two lists as a new list::  >>> intersection([1, 2, 3], [2, 3, 4]) [2, 3] >>> intersection([1, 2, 3], [1, 2, 3, 4])
 [1, 2, 3] >>> intersection([1, 2, 3], [3, 4])[3]  >>> intersection([1, 2, 3], [4, 5, 6]) []"""
    z = set(l1).intersection(set(l2))
    return z

    
def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    
def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.
    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')
    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"
        >>> calculate('add', 2.5, 4)
        'The result is 6.5'
        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'
        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'
        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'
    If a valid operation isn't provided, return None.
        >>> calculate('foo', 2, 3)
    """
    
    def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    
    def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """

    
