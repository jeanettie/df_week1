# print hello world
# print hello world
print("hello world")

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print("The average is: " + str(result))
