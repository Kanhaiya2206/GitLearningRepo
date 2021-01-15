def replace0with5(num):
    num += caladdedvalue(num)
    return num
    
def caladdedvalue(num):
    result=0
    decimalplace=1 
    if(num==0):
        result+=(5*decimalplace)
    while(num>0):
        if(num%10==0):
            result+=(5*decimalplace)
        num//=10
        decimalplace*=10
    return result
    
print(replace0with5(1020))    
    
