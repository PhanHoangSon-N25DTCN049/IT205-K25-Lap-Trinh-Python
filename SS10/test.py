numbers = [45, 12, 87, 34, 91, 56, 23, 78, 11, 69, 4, 38, 95, 27, 62, 15, 83, 50, 7, 41]
for i in range(1,len(numbers)):
    for j in range(i, 0, -1):
        if numbers[j] >= numbers[j - 1]: break;
        temp = numbers[j];
        numbers[j] = numbers[j - 1];
        numbers[j - 1] = temp;
print(numbers)
            
            
            
            
