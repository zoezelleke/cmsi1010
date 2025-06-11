def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n 

# Here are some sample calls to the blocks function just for fun
print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(995))


def sum_of_digits(n):
    return 0 if n == 0 else n % 10 + sum_of_digits(n // 10)


def is_palindrome(s):
    return True if s ==s[::-1] else False
    

def print_count_down(n): 
    if n==0:
        print("BOOM") 
    else:
        print(n)
        print_count_down(n -1)


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)