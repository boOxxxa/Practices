def ocs(s:str) -> bool:
    for i in s:
        if i != 'O' and not i.isdigit():
            return True
    return False
melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
for i in melt:
    if "O" in i and ocs(i):
        print(melt[i])