def truncate(phrase, n):
    """Return truncated-at-n-chars version of phrase. If the phrase is longer than, or the same size as, n make sure it ends with '...'
    and is no longer than n. >>> truncate("Hello World", 6)
'Hel...' >>> truncate("Problem solving is the best!", 10)
'Problem...' >>> truncate("Yo", 100) 'Yo' 
 The smallest legal value of n is 3; if less, return a message:
>>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.' >>> truncate("Woah", 4) 'W...' >>> truncate("Woah", 3)'...'"""
    if n < 3:
        return "Truncation must be at least 3 characters."
    if n > len(phrase) + 2:
        return phrase

    return phrase[:n - 3] + "..."
    
def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those. >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
 {'x': 9, 'y': 8, 'z': 7} If there are fewer values than keys, remaining keys should have value of None:
 >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) {'a': 1, 'b': 2, 'c': 3, 'd': None}
 If there are fewer keys, ignore remaining values: >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
 {'a': 1, 'b': 2, 'c': 3}"""
    new_dict = {}
    for index, value in enumerate(keys):
        new_dict[value] = values[index] if index < len(values) else None
    print(new_dict)
    return new_dict
    
def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.
    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)
        >>> nums = [1, 2, 3, 4] >>> sum_range(nums) 10
        >>> sum_range(nums, 1) 9
        >>> sum_range(nums, end=2) 6
        >>> sum_range(nums, 1, 3) 9
    If end is after end of list, just go to end of list:
        >>> sum_range(nums, 1, 99) 9"""
    if end is None:
        end = len(nums)

    return sum(nums[start:end + 1])
    
    
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
        >>> same_frequency(551122, 221515) True
        >>> same_frequency(321142, 3212215) False
        >>> same_frequency(1212, 2211) True """
    string1 = str(num1)
    string2 = str(num2)
    new_dict = {}
    new_dict2 = {}
    for i in string1:
        new_dict[i] = new_dict.get(i, 0) + 1
    for j in string2:
        new_dict2[j] = new_dict2.get(j, 0) + 1
    print(new_dict == new_dict2)
    
def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..
        >>> two_oldest_ages([1, 2, 10, 8]) (8, 10)
        >>> two_oldest_ages([6, 1, 9, 10, 4]) (9, 10)
    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages: >>> two_oldest_ages([1, 5, 5, 2]) (2, 5)"""
    age = set(ages)
    x = max(age)
    age.remove(x)
    y = max(age) 
    print(x, y)
    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.
def find_the_duplicate(nums):
    """Find duplicate number in nums.
    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None >>> find_the_duplicate([1, 2, 1, 4, 3, 12]) 1
     >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9]) 9 >>> find_the_duplicate([2, 1, 3, 4]) is None True """
    seen = {}
    dupes = []
    for num in nums:
        if num not in seen:
            seen[num] = 1
        else:
            if seen[num] == 1:
                dupes.append(num)
            seen[num] += 1
    if len(dupes) > 0:
        print(dupes)
    else:
        print("None")
    
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.
    Sum of TL-to-BR diagonal along with BL-to-TR diagonal: >>> 
    m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73
        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]
    print(total)
    
    
def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.
        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}) (1, 10) Works with any kind of key that can be compared,
        like strings: >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}) ('apple', 'cherry') """
    key_list = list(d.keys())
    this_tuple = (min(key_list), max(key_list))
    
    print(this_tuple)
    
def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.
    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3
    Examples:
        >>> find_greater_numbers([1, 2, 3])3
        >>> find_greater_numbers([6, 1, 2, 7]) 4
        >>> find_greater_numbers([5, 4, 3, 2, 1]) 0
        >>> find_greater_numbers([]) 0 """
    count = 0

    for num in range(len(nums)):
        for i in range(num + 1, len(nums)):
            if nums[i] > nums[num]:
                count += 1
    return count
