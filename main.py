# Reverse a String
# i want the first letter of my_word to be the last letter (spelt backwards)

my_word = 'Hello'

# Example
my_word_backwards = my_word[len(my_word) - 1]

for index in range(len(my_word) -1, -1, -1):
    print(my_word[index])

# This is my version

# the [::-1] is a slice statement it starts at position -1 (o) and ends at pisition 0 (H)

def my_word_backwards(my_word):
    word = my_word[::-1]
    return word

example = my_word_backwards('Hello')
print(example)

# Capitalize Letter

phrase = input('Please enter a random sentence: ')
print(phrase.title())


