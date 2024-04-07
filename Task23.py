arr=[45,7,4,7,38,3,5,2]
def mult(arr: list)->str:
    s=''
    for i in arr:
        s+=str(i*10)+ " "
    return s
print(mult(arr))