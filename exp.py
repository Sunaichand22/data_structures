def power(base,exp):
               if(exp==1):
                              return(base)
               if(exp!=1):
                              return(base*power(base,exp-1))
base=int(input("Enter Base:"))
exp=int(input("Enter Exp:"))
print("Result :",power(base,exp))
