'''
# Worksheet 1

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

# Bonus Problem

my_word = 'level'

def my_word_backwards(my_word):
    word = my_word[::-1]
    return word

word_backwards = my_word_backwards(my_word)


def palindrome_string():
    if word_backwards != my_word:
        print(f'{my_word} is not a palindrome')
    else:
        print(f'{my_word} is a palindrome')

final = palindrome_string()
print(final)


# Worksheet 2

# Happy Numbers




# Prime Numbers

my_number = 3

def determine_if_prime():
    if my_number > 1:
        for x in range(2,my_number):
            if (my_number % x) == 0:
                print(f'{my_number} is a prime number')
                break
        else:
            print(f'{my_number} is a prime number')
    else:
        print(f'{my_number} is not a prime number')

final = determine_if_prime()

# Fibonacci Numbers
'''
user_input = int(input('Please enter the number of itterations you want: '))
itterations = user_input

#how many times they want to run
#counter
#store in a list 

def fibonacci_sequence():
    counter = 1
    v1 = 1
    v2 = 2
    print(v1)
    if itterations <= 1:
        print('Enter number greater than 0')
    elif itterations == 2:
        print(v1)
    else:
        while counter < itterations:
            print(v1)
            n_itterations = v1 + v2
            v1 = v2
            v2 = n_itterations
            counter += 1

output = fibonacci_sequence()
