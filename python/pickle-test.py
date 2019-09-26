import pickle
lst = ['a','b','c']
f = open("pickle-list.txt","wb")
pickle.dump(lst, f)
f.close()
