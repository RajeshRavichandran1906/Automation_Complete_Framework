'''
This program will take one parameter: image name.
'''
import sys,os
image_name=sys.argv[1]

if exists(image_name.exact()):
    sys.exit(123)
else:
    sys.exit(456)