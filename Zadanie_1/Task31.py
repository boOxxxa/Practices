def writef(filename: str, data: list) -> None:
    f=open(filename, "a", encoding="utf-8")
    for i in data:
        f.write(f"{i[0]}\t{i[1]}\n")

writef("1.txt",[(1, 20),(2, 30),(3, 40),(4, 35),(5, 22),(6, 10)])