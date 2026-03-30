# Exercise 1: Calculate Cosine Similarity
from scipy.spatial import distance

vector1= [1,2]
vector2= [2,4]

result=distance.cosine(vector1,vector2)

print(result)