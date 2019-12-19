def triandular_number_generator(n):
    return [i * (i + 1) // 2 for i in range(n)]


n = int(input("Enter your number: "))
print(triandular_number_generator(n))
