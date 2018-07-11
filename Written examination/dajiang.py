def maxpooling(inputArray,k):
    length = len(inputArray)
    if length<k:
        return
    p = length-k+1
    ans = []
    for i in range(p):
        maxt = max(inputArray[i:i+k])
        ans.append(maxt)
    return ans

print(maxpooling([1,4,3,4,5],1))