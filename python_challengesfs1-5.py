def is_odd_string(word):
    """Is the sum of the character-positions odd?
    Word is a simple word of uppercase/lowercase letters without punctuation.
    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.
    For example, these sum to 1, which is odd:
        >>> is_odd_string('a') True
        >>> is_odd_string('A') True
    These sum to 4, which is not odd:
        >>> is_odd_string('aaaa') False
        >>> is_odd_string('AAaa') False
    Longer example:
        >>> is_odd_string('amazing') True """
    total = 0
    for char in word.lower():
        total += ord(char) % 2
    if total % 2 == 1:
        return True
    else:
        return False

    # Hint: you may find the ord() function useful here
def valid_parentheses(parens):
    """Are the parentheses validly balanced?
        >>> valid_parentheses("()") True
        >>> valid_parentheses("()()") True
        >>> valid_parentheses("(()())" True
        >>> valid_parentheses(")()") False
        >>> valid_parentheses("())") False
        >>> valid_parentheses("((())") False
        >>> valid_parentheses(")()(") False """
    print(len(parens) % 2 == 0)
    
def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"
        >>> three_odd_numbers([1, 2, 3, 4, 5]) True
        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]) True
        >>> three_odd_numbers([5, 2, 1]) False
        >>> three_odd_numbers([1, 2, 3, 3, 2]) False """
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

    return False
    
    
def reverse_vowels(s):
    """Reverse vowels in a string.
    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.
    >>> reverse_vowels("Hello!") 'Holle!'
    >>> reverse_vowels("Tomatoes") 'Temotaos'
    >>> reverse_vowels("Reverse Vowels In A String") 'RivArsI Vewols en e Streng'
    reverse_vowels("aeiou") 'uoiea'
    reverse_vowels("why try, shy fly?") 'why try, shy fly?''
    """
        vowels = 'aeiou'
    
    new_string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if new_string[i].lower() not in vowels:
            i += 1
        elif new_string[j].lower() not in vowels:
            j -= 1
        else:
            new_string[i], new_string[j] = new_string[j], new_string[i]
            i += 1
            j -= 1
    print("".join(new_string))
    return "".join(new_string)

def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.
    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle
    This should work:
       >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle
    It will raise an error if the file cannot be found.
        >>>> read_file_list("cats")
        - Auden
        - Ezra
        - Fluffy
        - Meowsley"""
    
    with open(filename) as fp:
        for lines in fp:
            lines = lines.strip
            print(f"- {lines}")

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
