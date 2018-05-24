
def execute(aList):
    
    for number in range(len(aList)-1,0,-1):
        
        for index in range(number):
            
            if aList[index] > aList[index+1]:
                
                value = aList[index]    
                aList[index] = aList[index+1]
                aList[index+1] = value