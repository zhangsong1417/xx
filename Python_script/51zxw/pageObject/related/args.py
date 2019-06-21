def fun_arg1(args):
    print("args is %s" % args)


def fun_arg2(args1, args2):
    print("args1 is %s args2 is %s"%(args1, args2))


def fun_var_args(*args):
    for value in args:
        print("args:", value)


# fun_arg1("51zxw")
#
# fun_arg2('51zxw', 'Selenium')

fun_var_args("51zxw", "Selenium", "Python")