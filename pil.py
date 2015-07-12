#!/usr/bin/env python
#					#
#	Author: Edson Silva		#
#	Site: http://edsonlead.com 	#
#					#
#########################################
import Image
import ImageDraw

img = "image.jpg"
new_img = "1m4g3.jpg"
img = Image.open(img)
width = 140
height = 140
size = width,height
angle = 45
posV = 200
posH = 200
position = posV,posH
phrase = "Example" 

def info_image(img):
	print (img.size,img.mode)

def to_thumbnail(new_img,(size)):
	img.thumbnail((size))
	img.save(new_img)

def to_antialias((size)):
	img.thumbnail((size),Image.ANTIALIAS)
	new_name = "antialias-%s.jpg" %(img)
	img.save(new_name)

def to_rotate(angle):
	imgRotate = img.rotate(angle)
	new_name = "%s-rotate-%s.jpg" %(img,angle)
	imgRotate.save(new_name)

def to_write(position,phrase):
	draw = ImageDraw.Draw(img)
	draw.text(position,phrase)
	new_name = "%s-write.jpg" %(img)
	img.save(new_name)

info_image(img)
to_thumbnail(new_img,(size))
to_antialias((size))
to_rotate(angle)
to_write(position,phrase)

