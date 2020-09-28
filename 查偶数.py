list_1 = eval(input('请输入列表lst：'))
def f_even_num(x):
    num = 0
    for i in x:
        if i%2==0:
            num = num + 1
    return num
pp = f_even_num(list_1)
print(pp)
