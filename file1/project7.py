import numpy as np
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

a=np.mat([
    [9,53,381],
    [53,381,3017],
    [381,3017,25317]
])

b=np.transpose(np.mat([32,147,1025]))

x=np.linalg.solve(a,b)
#print(x)

y=[]
for i in x.tolist():
    y.append(float(i[0]))

for i in y:
    print(i)
    #print(fractions.Fraction(i).limit_denominator())



