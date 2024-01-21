def calculate_sum(numbers):
   
    total = 0
    for num in numbers:
        total += num
    return total


numbers_list = [1, 2, 3, 4, 5]
result = calculate_sum(numbers_list)
print(f"The sum of {numbers_list} is: {result}")
