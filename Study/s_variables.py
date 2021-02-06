# python允许连续赋值，分配到相同的内存空间上
a = b = c = 1

d, e, f = 1, 2, "ccc"

# python有6个标准数据类型:numbers，string，list，tuple，set，dictionary

# int,float,bool,complex
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
