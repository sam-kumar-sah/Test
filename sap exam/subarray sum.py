def SubArraySum(arr, n):
  temp,result = 0,0
  for i in range(0, n):
    temp=0;
    for j in range(i, n):
      temp+=arr[j]
      result += temp
  return result


n=int(input())
arr = list(map(int,input().split()))
print (SubArraySum(arr, n))
