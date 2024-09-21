
def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

result = facto(4)
print(result)  # Output: 24
