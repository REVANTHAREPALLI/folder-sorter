import os,shutil
path=r"/home/revantharepalli10/ex/"
k=os.listdir(path)
l=list()
for i in k:
   j=i.split('.')
   if not os.path.exists(path+j[-1]):
      os.makedirs(path+j[-1])
      l.append(j[-1])
for i in k:
   for j in l:
      if '.'+j in i and not os.path.exists(path+j+'/'+i):
            shutil.move(path+i,path+j+'/'+i)
