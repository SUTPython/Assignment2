dna=input()
k=int(input())
f={}
for i in range(len(dna)-k+1):
  s=dna[i:i+k]
  if s in f:
    f[s]+=1
  else:
    f[s]=1
most=None
max_count=-1
for s in f:
  if f[s]>max_count:
    most=s
    max_count=f[s]     
print(most) 