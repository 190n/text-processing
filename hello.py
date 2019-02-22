from functools import reduce

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib_seq = [0, 1]

def fast_fibonacci(n):
    if n < len(fib_seq):
        return fib_seq[n]
    else:
        [a, b] = fib_seq[-2:]
        while len(fib_seq) < n:
            b += a
            a = b - a
            fib_seq.append(b)
        return b

def weave_strings(a, b):
    return reduce(str.__add__, [a[i] + b[i] for i in range(len(a))])

def weave_many_strings(*args):
    return reduce(str.__add__, [reduce(str.__add__, [s[i] for s in args]) for i in range(len(args[0]))])

# if __name__ == '__main__':
#     print(fast_fibonacci(100000))
