
with open('data\example7.txt') as text_file:
    numbers = [int(lint) for lint in text_file]
print(numbers)