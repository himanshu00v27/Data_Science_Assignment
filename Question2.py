def mid(a):
    return a[len(a)//2]

def check(a, s):

    m = mid(a)
    i = len(a)//2

    if s > m:
        return set(a[:i])

    elif s == m:
        return {i: m}

    else:
        return tuple(a[i+1:])

a = list(map(int, input("Enter list: ").split()))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Sum
s = x + y

# Output
print(check(a, s))
