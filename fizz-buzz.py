#fizz-buzz problem
import time
for i in range(1,15):
    if i % 5 == 0 and i % 3 == 0:
        
        print(i,' fizz-buzz')
        
    else:
        if i % 5 == 0:
           
            print(i," buzz")
           
        else:
            if i % 3 == 0:
                
                print(i," fizz")
              
            else:
                print(i)
                
