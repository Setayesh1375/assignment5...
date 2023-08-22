array = []
def chess(satr,sotun):
    for j in range(satr):
        array.append([])
        for i in range(sotun):
            if i % 2 != 0:
                array[j].append("#")
            else:
                array[j].append("*")
chess(int(input("tedad satr : ")), int(input("tedad sotun: ")))
for row in array:
     print(row )