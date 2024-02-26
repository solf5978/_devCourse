list_of_fib [0, 1]

def append_and_print_fib(i):
    fib_num = list_of_fib[i - 1] + list_of_fib[i - 2]
    list_of_fib.append(fib_num)

for i in range(2, 1000):
    append_and_print_fib(i)


