def func(n):
    my_list = [i for i in range(n)]
    my_list = sorted(my_list, key=int, reverse=True)
    print(my_list)
    return [i for i in my_list if i % 3 == 0]


n = int(input("number: "))
print(func(n))
