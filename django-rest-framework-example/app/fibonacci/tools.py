def FibonacciSequence(steps):
    if steps < 1:
        return None
    elif steps == 1:
        return [0]
    elif steps == 2:
        return [0, 1]
    fibonacci_sequence = [0, 1]
    a, b = fibonacci_sequence
    for _ in range(steps-2):
        c = a
        a = b
        b = b + c
        fibonacci_sequence.append(b)
    return fibonacci_sequence