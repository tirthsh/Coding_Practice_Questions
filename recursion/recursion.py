def palindrome(s):
  if len(s) == 1:
    return True

  first_index = 0
  last_index = len(s)-1

  while first_index <= last_index:
    if s[first_index] != s[last_index]:
      return False 
    first_index += 1
    last_index -= 1

  return True

def palindrome_recursion(s):
  if len(s) <= 1:
    return True
  else:
    return s[0] == s[-1] and palindrome_recursion(s[1:-1])

  
  
s = "anna"
print(palindrome(s))
print(palindrome_recursion(s))