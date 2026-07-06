arr = [12, 7, 25, 18, 5]
largest = arr[0]
second = float (' -inf')
for i in range (5):
    if ( arr[i] > largest ):
        second = largest
        largest = arr[i]
    elif ( arr[i] > second and arr[i] < largest):
        second = arr[i]
print(second)
        
        
