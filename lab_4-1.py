# Ryan Lugo: 12/3/21

total = 0

while True:
    numbers_input = int(input("Give number: "))

    if numbers_input == -1:
        break
    total += numbers_input
print("Heres the total amount of numbers: ",total)