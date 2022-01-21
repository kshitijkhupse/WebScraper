# put your python code here
three_digit_number = int(input())
last_digit = three_digit_number % 10
three_digit_number = three_digit_number // 10
second_digit = three_digit_number % 10
three_digit_number = three_digit_number // 10
first_digit = three_digit_number % 10
print(first_digit + second_digit + last_digit)
