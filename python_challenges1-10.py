def product(a, b):
    """Return product of a and b.        >>> product(2, 2)       4        >>> product(2, -2)        -4    """
     return a * b
    
def weekday_name(day_of_week):
"""Return name of weekday.     >>> weekday_name(1)  'Sunday'   >>> weekday_name(7) 'Saturday'   For days not between 1 and 7, return None >>> 
weekday_name(9) >>> weekday_name(0)    """
    weekdays = {
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",
        7:"Saturday"
    }
    
    return weekdays.get(day_of_week)


def last_element(lst):
    """Return last item in list (None if list is empty.   >>> last_element([1, 2, 3])    3   >>> last_element([]) is None   True"""
    return lst[-1]
    
def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a    >>> number_compare(1, 1) 'Numbers are equal' >>> number_compare(-1, 1) 'Second is greater' 
    >>> number_compare(1, -2) 'First is greater'"""
    if a > b:
        print("First is greater")
    elif b > a:
        print("Second is greater")
    elif b == a:
        print("numbers are equal")

    
def reverse_string(phrase):   """Reverse string, >>> reverse_string('awesome')'emosewa'>>> reverse_string('sauce')'ecuas'    """
    new_string =  phrase[::-1]
    print(new_string)
    
def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)  >>> single_letter_count('Hello World', 'h') 1 >>> single_letter_count('Hello World', 'z')0
  >>> single_letter_count("Hello World", 'l') 3  """
    counter = word.upper().count(letter.upper())
    print(counter)
    
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase. >>> multiple_letter_count('yay') {'y': 2, 'a': 1}>>> multiple_letter_count('Yay') {'Y': 1, 'a': 1, 'y': 1} """
    from collections import Counter
    output = Counter(phrase)
    return output
    
    
def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end. 
    - lst: list of values 
    - command: command, either "remove" or "add" 
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add
remove: remove item at beginning or end, and return item removed
  >>> lst = [1, 2, 3]>>> list_manipulation(lst, 'remove', 'end') 3
  >>> list_manipulation(lst, 'remove', 'beginning') 1>>> lst [2]

add: add item at beginning/end, and return list
        >>> lst = [1, 2, 3]>>> list_manipulation(lst, 'add', 'beginning', 20) [20, 1, 2, 3]
        >>> list_manipulation(lst, 'add', 'end', 30) [20, 1, 2, 3, 30] >>> lst [20, 1, 2, 3, 30]
Invalid commands or locations should return None:
        >>> list_manipulation(lst, 'foo', 'end') is None True>>> list_manipulation(lst, 'add', 'dunno') is NoneTrue """
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

        elif command == "add":
            if location == "beginning":
                lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst

def is_palindrome(phrase):
    """Is phrase a palindrome?Return True/False if phrase is a palindrome (same read backwards andforwards).
        >>> is_palindrome('tacocat') True >>> is_palindrome('noon')True >>> is_palindrome('robert') False
    Should ignore capitalization/spaces when deciding: >>> is_palindrome('taco cat')True>>> is_palindrome('Noon')True"""
    new_string = phrase.lower().replace(' ', '')
    if new_string == new_string[::-1]:
        return True
    else:
        return False

def frequency(lst, search_term):
    """Return frequency of term in lst >>> frequency([1, 4, 3, 4, 4], 4)3 >>> frequency([1, 4, 3], 7) 0 """
    output = lst.count(search_term)
    return output
