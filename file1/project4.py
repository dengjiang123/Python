x=[5,8,13,21,30,50,100]
y=[2,4,10,29,70]
z=[]
m=len(x)
n=len(y)
i,j=0,0
while (i<m or j<n):
    if j<n and x[i]<y[j]:
        z.append(x[i])
        if i<m:
            i+=1
    elif j<n and x[i]>=y[j]:
        z.append(y[j])
        if j<n:
            j+=1
    elif j<n:
        z.extend(y[j:n])
        j=n
    else:
        z.extend(x[i:m])
        i=m

print(z)