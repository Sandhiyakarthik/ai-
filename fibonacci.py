def generate_fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two numbers

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence

    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

# Change the value of 'n' to generate a different number of Fibonacci numbers
n = 10
fib_numbers = generate_fibonacci(n)
print(f"Fibonacci sequence of the first {n} numbers: {fib_numbers}")
