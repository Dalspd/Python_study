# Welcome
print("welcome to this repo.")

# A test for pycharm[x.print==>print(x)]
x = 3
print(x)  # x.print

# 换行符
one = 1
two = 2
three = 3
total = one + \
        two \
        + three

fruits = ['apple', 'banana',
          'orange']  # [],{},()不需要换行符

# 从键盘输入
# insth = input("input sth pls\n")
# print(insth)

"""
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
"""
print('aaaaaa', sep='1', end='3', flush=True)

f = list(range(10))
print(f)
