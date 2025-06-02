def sum_odds(n):
    if n < 1 :
        print('Input must be greater than 1')
        return 0
    total = 0
    for i in range(1, n+1):
        print(f'i at {i}th iteration : {i}')
        if i % 2 != 0:
            print(i)
            total += i
    return total

# Test the function
print(sum_odds(10))  # Expected: 1 + 3 + 5 + 7 + 9 = 25
