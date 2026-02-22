def function(n):
    nums = [i+1 for i in range(n)]

    total = 1
    for i in range(n):
        total *= i+1

    results = []
    
    def backtrack(start):
        if start == n:
            results.append(nums[:])
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            
    backtrack(0)
  
    return total, results
