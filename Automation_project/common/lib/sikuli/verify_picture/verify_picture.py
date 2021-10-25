'''
This program will image with tolerance.
'''
import sys
image_name=sys.argv[1]
tolerance=sys.argv[2]

if exists(Pattern(image_name).similar(float(tolerance))):
    sys.exit(123)
else:
    sys.exit(456)