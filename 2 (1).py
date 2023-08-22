satr = int(input("satr: "))
sotun = int(input("sotun: "))
jadval_zarb = []
for i in range(1,satr+1):
    jadval_zarb.append([])
    
    for j in range(1,sotun+1):
        jadval_zarb[i-1].append([i*j])
        

for row in jadval_zarb:
    print(row)
    