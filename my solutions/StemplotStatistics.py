def read_plot():
    floor = int(input("floor of the number on the left of the line"))
    cieling = int(input("ceiling of the number on the right of the line"))
    datas = []
    for i in range(floor, cieling+1):
        inputs = input(i, "| ").split()
        for x in inputs:
            datas.append(int(str(i)+str(x)))
            
    datas.sort()
    return datas

def read_numbers():
    datas = []
    while 1:
        _=input()
        if _=="":
            break
        datas.append(int(_))
    datas.sort()
    return datas
        
datas = read_numbers()
mean = sum(datas) / len(datas)

def get_median(dataset):
    if len(dataset) % 2:
        return dataset[len(dataset) // 2 + 1]
    
    median = dataset[len(dataset)//2-1]
    median += dataset[len(dataset)//2]
    median /= 2
    return median

median = get_median(datas)
left_half = datas[0:len(datas)//2]
right_half = datas[len(datas)//2+1:len(datas)]
q1 = get_median(left_half)
q3 = get_median(right_half)
IQR = q3-q1

variance = 0
for i in datas:
    variance += (i-mean) ** 2
    
variance /= len(datas)-1
standard_deviation = variance ** 0.5

outlier_range = (q1-IQR*1.5, q3+IQR*1.5)
left_outliers = []
right_outliers = []
for i in datas:
    if i < outlier_range[0]:
        left_outliers.append(i)
    if i > outlier_range[1]:
        right_outliers.append(i)


print("mean:", mean)
print("median:", median)
print("variance:", variance)
print("standard deviation:", standard_deviation)
print("range:", datas[-1] - datas[0])
print("five number summary:", (datas[0], q1, median, q3, datas[-1]))
print("IQR:", q3-q1)
print("Q1-1.5IQR:", outlier_range[0])
print("Q3+1.5IQR:", outlier_range[1])
print("outliers:", left_half, "(left)", right_half, "(right)")

while True:
    x = int(input("x>>"))
    i = 0
    for i in range(len(datas)):
        if datas[i] > x:
            break
    
    print("percentile", i/len(datas))
    print("z-score", (x-mean) / standard_deviation)