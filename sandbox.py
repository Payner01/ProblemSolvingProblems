
phrase = 'this is a test'
#print(phrase.capitalize())
print(phrase.title())

# above capitalizes the first letter in the phrase
# i want the first letter in each part of phrase to be capitalized
# make a function that takes the phrase and looks at the string


def first_letter_capitalize():
    for x in range(0,len(phrase)):
        if phrase[x] == ' ':
            first_letter = phrase[x+1]
            print(first_letter.capitalize())
        

final = first_letter_capitalize()
print(final)



