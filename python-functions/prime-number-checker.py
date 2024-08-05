number_input = int(input("please enter a number:  "))
is_prime = True

for i in range(2, int(number_input ** 0.5) + 1):
    if number_input % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"Your number: {number_input}, is A PRIME number!")
else:
    print(f"Your number: {number_input}, is NOT a prime number!")
