# Program to print files in a directory recursively

import os
import sys
dirt=sys.argv[1]
print dirt
a='|--'
b='|   '
i=0
def dirttree(dirt,i):
        filenames=os.listdir(dirt)
        for filename in filenames:
                if not os.path.isdir(os.path.abspath(dirt+'/'+filename)):
                        if filename==filenames[-1]:
                                print b*i+'\--',filename
                        else:
                                print b*i+'|--',filename

                else:
                        print b*i+'|--',filename
                        dirt=dirt+'/'+filename
                        dirttree(dirt,i+1)

dirttree(dirt,i)

