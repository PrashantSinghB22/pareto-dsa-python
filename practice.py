def group_anagrams_frequency(strs):
  groups = {}
  for word in strs:
    count = [0] * 26
    for char in word:
      index = ord(char) - ord('a')
      count[index] += 1

    key = tuple(count)

    if key not in groups:
      groups[key] = [word]
    else:
      groups[key].append(word)

  return list(groups.values())

