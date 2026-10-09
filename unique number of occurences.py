nums=list(map(int,input().split()))
freq={}
count=0
for i in nums:
  freq[i]=freq.get(i,0)+1
for key,value in freq.items():
  if(value>2):
    count+=1
if(count>=1):
  print("true")
else:
  print("false")