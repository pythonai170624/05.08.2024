"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array.
  Otherwise, return false.
Example 1:
  Input: arr = [2,6,4,1]
  Output: false
  Explanation: There are no three consecutive odds.
Example 2:
  Input: arr = [1,2,34,3,4,5,7,23,12]
  Output: true
  Explanation: [5,7,23] are three consecutive odds.
"""

def triple_odds(list1: list[int]) -> bool:
    count = 0
    for number in list1:
        if number % 2 != 0:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

def triple_odds_no_count_minus(list1: list[int]) -> bool:
    for i in range(2, len(list1)):
        if list1[i] % 2 != 0 and list1[i - 1] % 2 != 0 and list1[i - 2] % 2 != 0:
            return True
    return False

def triple_odds_no_count_plus(list1: list[int]) -> bool:
    if len(list1) < 2:
        return False
    for i in range(0, len(list1) - 2):
        if list1[i] % 2 != 0 and list1[i + 1] % 2 != 0 and list1[i + 2] % 2 != 0:
            return True
    return False

print(triple_odds([1,2,34,3,4,5,7,23,12]))  # True
print(triple_odds([34,3,4,5]))  # False

print(triple_odds_no_count_minus([1,2,34,3,4,5,7,23,12]))  # True
print(triple_odds_no_count_minus([34,3,4,5]))  # False

print(triple_odds_no_count_plus([1,2,34,3,4,5,7,23,12]))  # True
print(triple_odds_no_count_plus([34,3,4,5]))  # False

