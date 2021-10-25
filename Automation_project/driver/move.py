import os, shutil, sys

file_type=sys.argv[1]
source=sys.argv[2]
target=sys.argv[3]

root=os.getcwd()

if file_type == 'folder':
#     if os.path.isdir(target):
#         os.system('rm -r '+target)
    shutil.move(root+'/' + source+'/', root+'/'+target+'/')