# write a program to generate fibonacci series n as parameter into function and take user input for n
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series   
n=int(input("Enter the number of terms in the Fibonacci series: "))
print(fibonacci_series(n))
#write a program to reverse the list using the function and take user input for the list elements using slicing or loop
def reverse_list(lst):
    return lst[::-1] 
user_input = input("Enter the list elements separated by spaces: ")
lst = user_input.split()    
reversed_lst = reverse_list(lst)
print("Reversed list:", reversed_lst)
#write a program to check if string starts with a capital letter and ends with a period output true or false 
def check_string(s):    
    return s[0].isupper() and s.endswith('.')
user_string = input("Enter a string: ")
result = check_string(user_string)
print("String starts with a capital letter and ends with a period:", result)
#write a  function to add the numbers up to 10
def add_numbers_up_to_10():
    return sum(range(1, 11))
#take user inout for n 
n = int(input("Enter a number to add up to 10: "))
# call the function and print the result
result = add_numbers_up_to_10()
print("Sum of numbers from 1 to 10 is:", result)
#write a program to add numbers up to 10 and print output
def add_numbers_up_to_10():
    total = 0
    for i in range(1, 11):
        total += i
    return total
result = add_numbers_up_to_10()
print("Sum of numbers from 1 to 10 is:", result)
#write a program in 2 different prompts styles to generate a function that returns the sum of digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

num = int(input("Enter a number to calculate the sum of its digits: "))
result = sum_of_digits(num)
print("Sum of digits:", result)
def sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum
num = int(input("Enter a number to calculate the sum of its digits: "))
result = sum_of_digits(num)
print("Sum of digits:", result)

