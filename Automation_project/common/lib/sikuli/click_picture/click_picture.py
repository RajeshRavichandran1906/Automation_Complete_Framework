import sys,os
image_name=sys.argv[1]
xoffset=sys.argv[2]
yoffset=sys.argv[3]
click_type=sys.argv[4]
m=find(image_name)
x=m.getX()
y=m.getY()
m.click(Location(x+int(xoffset),y+int(yoffset)))
