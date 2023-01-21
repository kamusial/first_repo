import os
#from os import *

print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop\\nn')
print(os.getcwd())
os.mkdir('new_folder')
os.rename('new_folder', 'new_folder2')
os.rmdir('new_folder2')