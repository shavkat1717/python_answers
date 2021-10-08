from random import  sample
from math import sqrt
x = list(range(0,1001))
y = sample(x,k=10)
print(y)
ildizlar = list(map(lambda n:sqrt(n),y))
print(ildizlar)
toq_sonlar = list(filter(lambda n:n%2,y))
print(toq_sonlar)