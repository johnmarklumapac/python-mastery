data = [1, 2, 3, 4, 5, 15]

for i in range(len(data)):
    data.pop()
    data_sum = sum(data[i:])
    data.append(data_sum)

    print(data[i:])

    
