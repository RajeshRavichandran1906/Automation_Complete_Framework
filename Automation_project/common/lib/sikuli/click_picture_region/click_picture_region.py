import sys,os

image_name=sys.argv[1]
xoffset=sys.argv[2]
yoffset=sys.argv[3]
click_type=sys.argv[4]
screen_area=sys.argv[5]
if screen_area=="right":
    regional_location=Region(int(1000), int(150), int(900), int(900))
elif screen_area=="bottom":
    regional_location=Region(int(0), int(800), int(1900), int(450))
m=regional_location.find(image_name)
x=m.getX()
y=m.getY()
m.click(Location(x+int(xoffset),y+int(yoffset)))
