  
import sample_4
p1 = sample_4.Point(2, 3)
p2 = sample_4.Point(4, 5)
print(p1)
print(p2)
print(sample_4.distance(p1, p2))
del p1
del p2
print('Done')