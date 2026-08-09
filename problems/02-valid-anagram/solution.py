# def valid_anagram(s, t):

#   if len(s) != len(t):
#     return False
#   s_count = {}
#   t_count = {}

#   for char in s:
#     if char not in s_count:
#       s_count[char] = 1
#     else :
#       s_count[char] += 1

#   for char in t:
#     if char not in t_count:
#       t_count[char] = 1
#     else:
#       t_count[char] += 1

#   return s_count == t_count
    





# def valid_anagram_sorting(s, t):
#   if len(s) != len(t):
#     return False

#   sorted_s = ''.join(sorted(s))   
#   sorted_t = ''.join(sorted(t))  

#   return sorted_s == sorted_t

# def valid_anagram_fixed_array(s, t):
#   if len(s) != len(t):
#     return False

#   count = [0] * 26






# print(valid_anagram_sorting("anagram", "nagaram"))
# print(valid_anagram_sorting("rat", "car"))
# print(valid_anagram_sorting("aab", "abb"))
# print(valid_anagram_sorting("abc", "abc"))
# print(valid_anagram_sorting("a", "a"))
# print(valid_anagram_sorting("a", "b"))
    
      



def contains_duplicate_hashset(nums):
  my_list = set()
  for num in nums:
    if num in my_list:
      return True
    else:
      my_list.add(num)
    
  return False


print(contains_duplicate_hashset([1, 2, 3, 4, 6, 7, 7, 2]))
print(contains_duplicate_hashset([1, 2, 3, 4]))
    
