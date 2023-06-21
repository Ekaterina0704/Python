def same_by(characteristic,object):
    return len(set(map(characteristic,object)))==1 or object=[]
# return len(list(filter(characteristic,object)))==0



values=[0,2,10,6,7]
if same_by(lambda x: x%2,values):
    print("same")
else:
    print("different")
