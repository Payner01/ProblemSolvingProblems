
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




#print(phrase.capitalize())
#print(phrase.title())

# above capitalizes the first letter in the phrase
# i want the first letter in each part of phrase to be capitalized
# make a function that takes the phrase and looks at the string

phrase = 'hello world'

def first_letter_capitalize():
    processed_string = ""
    previous_letter = " "
    for x in phrase:
        if previous_letter  == " ":
            letter = x.upper()
            processed_string += letter
            previous_letter = x
        # make an elif to handle the logic for the very virst letter 
        # elif x == phrase[0]:
        #   run some code
        else:
            processed_string += x
            previous_letter = x
    print(processed_string)
            

final = first_letter_capitalize()
print(final)


# PROBLEM 3
# previouse_letter = phrase[0]
# variables we will need. previous_letter, current_counter, processed_string
# for loop is easiest to understand 
# if and else just like above 
# need to track the previous letter to determine if we should contiune counting or start over counting 
# if x == previous letter 
#   current_counter += 1
# else:
#   processed_string += str(current_count) + previous_letter
#   current_count = 0
#   prevouse_letter = x
#print(processsed_string)

phrase = 'aaaabbbccd'

def compressed_string(phrase):
    processed_phrase = ''
    count = 1
    for x in range(len(phrase)-1):
        if phrase[x] == phrase[x + 1]:
            count = count + 1
        else:
            processed_phrase = processed_phrase + phrase[x] + str(count)
            count = 1
    processed_phrase = processed_phrase + phrase[x + 1] + str(count)
    print(processed_phrase)

final = compressed_string(phrase)
print(final)
