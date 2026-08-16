def is_valid(s):
  mapping = {
    "]" : "[",
    "}" : "{",
    ")" : "("
  }

  stack = []

  for char in s:
    if char in mapping.values():
      stack.append(char)

    else:
      if not stack:
        return False
      if stack[-1] != mapping.values():
        return False
      stack.pop()


    