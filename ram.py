def rem(x,a):
    if x==a:
        return 0
    elif x<a:
        return x
    else:
        return rem(x-a,a)

print(rem(2,5))
print(rem(5,5))
print(rem(7,5))