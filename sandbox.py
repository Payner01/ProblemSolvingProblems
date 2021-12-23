

#need to get the digits in a number alone 

#digits = [int(a) for a in str(number)]
#print(digits)

#sum = digits[0] * digits[0] + digits[1] * digits[1]
#print(sum)

number = input("enter number")

def happy_numbers(number):
    counter = 0
    new_number = number
    while counter <= 1000:#says what run you are on
        digits = list(str(new_number))#splits number
        counter += 1
        if new_number != 1:
            new_number = 0 
            for x in digits:#for each number in list you are ittirating over it
                new_number += int(x) * int(x)
        else:
            print(f'{number} is a happy number')
            break
    else:
        print(f'{number} is not happy after 1000 runs')       
            
happy_numbers(number)

        
    



