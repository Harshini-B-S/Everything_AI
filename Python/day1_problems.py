# Reverse a string O(n)
def reverse_string(s):
    return s[::-1]

# Example usage
print(reverse_string("abcdefg"))

'''
#not very optimal O(n)
def reverse_string(s):
    return ''.join(reversed(s))

# O(n^2)
def reverse_string(s):
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str

    return reversed_str
'''

#check palindrome
def is_palindrome(s):
    p = s.lower().replace(" ", "")
    return p == p[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("Nurses run"))    # True

#largest number in a list O(n)
def find_largest(nums):
    if not nums:
        return None  # Handle empty list case

    largest = nums[0]

    for num in nums[1:]:
        if num > largest:
            largest = num

    return largest

# Example usage
print(find_largest([3, 1, 4, 1, 5, 9]))  # 9
print(find_largest([]))  # None

#fibonacci series
def fibonacci(n):
    if n == 0 or n == 1:
        return n 
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(5))

#fibonacci iterative
def fibonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])

    return fib

print(fibonacci(5))

#fibonacci optimal
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
print(fibonacci(5))

#prime
def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(n ** 0.5) + 1,2):
        if n % i == 0:
            return False
        
    return True
    
print("1",isPrime(1))

#n primes

def n_primes(n):
    primes = [2]
    if n <= 0:
        return [] 
    num = 3
    while len(primes) < n:
        if isPrime(num):
            primes.append(num)
        num += 2
    return primes

print(n_primes(10))

#remove duplicates

def remove_dup (nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique

def remove_dup_better(nums):
    seen = set()
    i = 0

    while i < len(nums):
        if nums[i] in seen:
            nums.pop(i)
        else:
            seen.add(nums[i])
            i += 1

    return nums
nums = [1, 2, 2, 3, 1, 4]
nums = ['a','a','c','b','d','c','b']
print(remove_dup(nums))
print(remove_dup_better(nums))

#char counter
def count(s):
    l = len(s)
    dic = {}
    for i in range(l):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    return dic

print(count("abcdefghijklmnopabcdefghijnn"))