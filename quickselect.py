def quickselect(a,k):
  k=k-1
  s=0
  e=len(a)-1
  if k>e:
    return "not found"
  while True:
    pivot= partition(a,s,e) #lomuto partioning
    if pivot==k:
      return a[pivot]
    elif pivot>k:
      e=pivot-1
    elif pivot<k:
      s=pivot+1


def partition(a,s,e):
  pivot=a[e]
  index=s-1
  for j in range (s,e+1):
    if a[j]<pivot:
      index+=1
      a[index],a[j]=a[j],a[index]
  index+=1
  a[index],a[e] = a[e],a[index]
  print(a)
  return index


a=[2,5,8,3,1,7]
print("the kth element:",quickselect(a,4))