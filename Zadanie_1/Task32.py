def filter(path: str, lim: int) -> list:
    arr=[]
    with open(path,"r", encoding="utf-8") as f:
        s=f.read().split("\n")
        for i in s:
            if float(i)<=lim:
                arr.append(float(i))
    return arr

file='freqs.txt'
threshold = float(input())
print(filter(file,threshold))