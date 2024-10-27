import random

def generate_random_list(n):
    return random.sample(range(-10, 11), n)


def calculate_sum_between_max_min(numbers):
    if not numbers:  
        return 0

    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))

    start_index, end_index = sorted([max_index, min_index])

    return sum(numbers[start_index:end_index + 1])

n = int(input("Введіть кількість елементів : "))
random_list = generate_random_list(n)

print("Згенерований список:", random_list)

result_sum = calculate_sum_between_max_min(random_list)
print("Сума чисел між максимальним і мінімальним значенням:", result_sum)
