###  THIS IS THE CODE I PERSONALLY CREATED TO SORT THE FILES IN MY CHROMEBOOK


import os,shutil                       #These are the modules that are used----OS(OPERATING SYSTEM)
path=r"/home/revantharepalli/ex/"
k=os.listdir(path)                     #GIVES LIST OF FILES IN THE GIVEN PATH
l=list()         
for i in k:                            #IT CREATES FOLDERS WITH THE NAMES WHICH ARE AVAILABLE AS FILE EXTENSIONS & ALSO AVOIDS DUPLICATION
   j=i.split('.')  
   if not os.path.exists(path+j[-1]):  # HELPS TO AVOID DUPLICATION
      os.makedirs(path+j[-1])
      l.append(j[-1])                  #LIST OF CREATED FOLDERS
for i in k:                            #LOOP TO MOVE FILES INTO FOLDERS ACCORDING TO THEIR EXTENSIONS
   for j in l:
      if '.'+j in i and not os.path.exists(path+j+'/'+i):   # HELPS TO AVOID DUPLICATION
            shutil.move(path+i,path+j+'/'+i)
