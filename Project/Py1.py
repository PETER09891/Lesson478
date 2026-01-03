# Program to check if a number is an Armstrong number

num = int(input("Enter a number: "))
original = num
digits = len(str(num))
sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** digits
    num //= 10

if sum_of_powers == original:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")