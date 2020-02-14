#script for parameter optimisation
#Run for find optimal threshold values
combination=[]
ma = []
for j in range(0,254):
    for k in range(j+1,255):
      ma.append(SegmentTest("data/train/image", "data/train/label",j,k))
      combination.append([j, k])
      print(j, k)
index = ma.index(max(ma))
print('best low threshold is%d'%combination[index][0])
print('best high threshold is%d'%combination[index][1])
print('PA is %f'%max(ma))










