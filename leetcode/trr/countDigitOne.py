def countDigitOne(n):
    count, k = 0, 0
    tip, tip1 = 1, 0
    n1 = n
    while n:
        x = n % 10
        k += 1
        if x > 1:
            count += tip + x * tip1 
        if x == 1:
            count += (n1%tip+1) + tip1
        tip, tip1 = tip * 10, k * tip
        n = n // 10
    return count

n = 121
print(countDigitOne(n))