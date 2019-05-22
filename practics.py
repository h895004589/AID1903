
def sum(num):
    if num > 0:
        return num +sum(num-1)
    else:
        return 0

print(sum(100))

list01 = [1,2,3,[225,15,[225],[225,12,53,[225]]]]
all_value = []
def fun01(target_list):
    for i in target_list:
        if isinstance(i,list):
            fun01(i)
        else:
            all_value.append(i)
    return all_value

f = fun01(list01)
print(f)



