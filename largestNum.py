inputNumb = [3, 41, 12, 74, 50]
largest = inputNumb[0]  # Assign any number in the list to a temporary variable
for x in inputNumb:
    if x > largest:
        largest = x
print(f"The largest number among {inputNumb} is {largest}")
