# Ryan Lugo: RJL 12/2/21

def sum_to(n):
    total = 0
    counter = 0
    while counter <= n:
        total += counter
        counter += 1
    return total


number = int(input("Enter a number: "))
print(sum_to(number))