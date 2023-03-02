#Febonacci Numbers
#1 1 2 3 5 8 13 21 34 ......
# xi = xi-1 + xi-2

# create a function feb that returns nth 
# febo number and takes n as an input argumjent

# first, second = 1, 1

# i = 0
# while i < n - 2:
#     temp = second 
#     second += first
#     first = temp   

#     i += 1

# print(second)



#Febonacci Numbers
#1 1 2 3 5 8 13 21 34 ......
# xi = xi-1 + xi-2



# create a function feb that returns nth 
# febo number and takes n as an input argumjent


mem = {}

def feb(n):
    if n <=2: return 1
    else:
        if mem[n] is None:
            mem[n] = feb(n - 1) + feb(n - 2)
        
        return mem[n]
        



print(feb(6))



