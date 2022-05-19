x=30
if x > 30:
    print("Yes")
else:
    print("No")


def slength1(s):
    if len(s) > 10:
        ans = 'very long'
    else:
        ans = 'normal'

    return ans

print(slength1("Hello"))

print(slength1("HelloHello"))

print(slength1("Hello again"))

def slength2(s):
    if len(s) == 0:
        ans = 'empty'
    elif len(s) > 10:
        ans = 'very long'
    elif len(s) > 7:
        ans = 'normal'
    else:
        ans = 'short'
    return ans

print(slength2("siema"))
print(slength2("siema siema witam"))
print(slength2("Hello Hi"))
print(slength2(""))
