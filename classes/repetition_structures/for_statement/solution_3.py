NUMBER_OF_REPETITIONS = range(1, 11)
ANOTHER_NUMBER_OF_REPETITIONS = range(11)
for index in NUMBER_OF_REPETITIONS:
    print(f"Let's print out the multiply table for {index}")
    for index_2 in ANOTHER_NUMBER_OF_REPETITIONS:
        print(f"{index} x {index_2} = {index * index_2}")
