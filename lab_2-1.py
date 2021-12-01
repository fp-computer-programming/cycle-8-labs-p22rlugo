# Ryan Lugo: RJL 12/1/21

number_input = int(input("What number?: "))

def adding(number):
    total = 0

    for e in range(number + 1):
        total += e
    return total

final = adding(number_input)
print("Here's the final sum of the numbers!:",final)
