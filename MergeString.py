# This is Famous leetcode problem solution along with example
#Merge String is famous problem 
from io import StringIO

def merge_alternately(word1, word2):
    merged_string = StringIO()

    i = 0
    j = 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged_string.write(word1[i])
            i += 1

        if j < len(word2):
            merged_string.write(word2[j])
            j += 1

    return merged_string.getvalue()

# Example usage
word1 = "Hello"
word2 = "World"
merged_string = merge_alternately(word1, word2)
print(merged_string)
