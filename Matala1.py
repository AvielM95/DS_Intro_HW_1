         

#%%
def my_func(x1,x2,x3):
    
      
        if x1+x2+x3 == 0 :
              return("Not a number-denominator is zero")
                
        elif  type(x1)!=float :  
              return "ERROR:parameters should be float"
              
        elif  type(x2)!=float:  
              return"ERROR:parameters should be float"
        
        elif  type(x3)!=float :  
              return"ERROR:parameters should be float"
        
        else :
             return((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)

                                       
print(my_func(1.0,1.0,-3))



#%%


def convert(hours=0,minute=0):
    
    if hours < 0 or minute < 0 :
       return("Input error!")
     
    else:
       return(hours*3600+minute*60)


print(convert(1,3.0))




















