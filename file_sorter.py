# folder-sorter
#This is a python program to sort the files in my computer /file manager according to the extension the file has*
import os,shutil
path=r"<link-the-folder/files-to-be-sorted>"
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

