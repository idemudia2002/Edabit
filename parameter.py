def first_arg(*args):
    if args: return args[0]

def last_arg(*args):
    if args: return args[-1]

print(first_arg(2,3,4))
print(last_arg(2,4,5,6))