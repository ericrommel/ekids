input_numbers = [45, 3, 5, 12, 1, 40]

def sort_des(numbers):
    array_length = len(numbers)
    for pass_index in range(array_length):
        for element_index in range(0, array_length-1):
            if numbers[element_index] > numbers[element_index+1]:
                temp_number = numbers[element_index]
                numbers[element_index] = numbers[element_index + 1]
                numbers[element_index + 1] = temp_number
    return numbers


print(sort_des(input_numbers))