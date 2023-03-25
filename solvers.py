
def solver_one(values):
    max_sum = -10000000000
    s,e = 0,0
    l = len(values)
    for start in range(l):
        for end in range(start,l):
            tmp_sum = sum(values[start:end])
            if max_sum < tmp_sum:
                max_sum = tmp_sum
                s = start
                e = end
    return (s,e,max_sum)
            
test = [1,2,-1,4,-2,6,8,-1,4,6,-4,-5,3,1]
print("valori: ", test, " len = ", len(test))
print(solver_one(test))
