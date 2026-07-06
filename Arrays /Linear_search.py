arr = [12, 7, 25, 18, 5]
key = 18
found = False 
for i in range(len(arr)):
    if  (arr[i] == key):
        found = True
        print("Found at index", i)
        break
            
if found == False:
    print("Not found")
        
        
  
    
