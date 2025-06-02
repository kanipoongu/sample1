import pdb

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True  # ❌ Bug: Wrong indentation

def analyze_numbers(nums):
    odds = []
    evens = []
    odd_sum = 0
    even_sum = 0

    for num in nums:
        pdb.set_trace()  # Debug here
        if num % 2 == 0:
            evens.append(num)
            even_sum += num
        else:
            odds.append(num)
            odd_sum += num
        
        # Bug in prime logic will affect this
        if is_prime(num):
            print(f"{num} is a Prime number")
        else:
            print(f"{num} is not a Prime number")
    
    print(f"Odd Numbers: {odds} | Sum = {odd_sum}")
    print(f"Even Numbers: {evens} | Sum = {even_sum}")

# Run it
analyze_numbers([2, 3, 4, 5, 6, 7, 8, 9])
