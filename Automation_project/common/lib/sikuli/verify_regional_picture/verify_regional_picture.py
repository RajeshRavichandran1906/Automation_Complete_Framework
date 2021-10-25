'''
This program will take one parameter: image name.
'''
import sys
image_name=sys.argv[1]
left=sys.argv[2]
top=sys.argv[3]
width=sys.argv[4]
height=sys.argv[5]

######//// Image pattern tollerance /////####
image_tolerance=0.80

######//// Getting the location of image /////####
regional_location=Region(int(left), int(top), int(width), int(height))

######////  Check the image exist inside focus window ######////
if regional_location.exists(Pattern(image_name).similar(image_tolerance)):
    sys.exit(123)
else:
    sys.exit(456)