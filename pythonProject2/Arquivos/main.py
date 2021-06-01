""" Open Read and Change things into files
with open('abc.txt','w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print(file.read())"""

# 'R' is just to Read archives into the files
#with open('abc.txt','r') as file:
#    print(file.read())
"""" "a+" Is just to add lines into the file
with open('abc.txt','a+') as file:
    file.write( 'other line\n' )
    file.seek(0)
    print(file.read())"""

""" if you want to remove files into your project you may use 
import os and use os.remove('name_of_the_file')
"""