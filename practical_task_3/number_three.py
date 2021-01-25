def my_funs(*args):
    args = list(args)
    args.remove(min(args))
    print(sum(args))


my_funs(3, 4, 5)
