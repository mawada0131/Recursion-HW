def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return Fibonacci(n-1)+ Fibonacci(n-2)

def find_subsets(lst):
    if len(lst) == 0:
        return [[]]
    new_subset = find_subsets(lst[1:])
    current_result = []
    for sub in new_subset:
        current_result.append([lst[0]] + sub  )
    return current_result + new_subset
print(find_subsets([1,2]))
    
    