#!/usr/bin/env python
#					#
#	Author: Edson Silva		#
#	Site: http://edsonlead.com 	#
#					#
#########################################
import Image
import ImageDraw

nameImg = "image.jpg"
newImg = "1m4g3.jpg"
img = Image.open(nameImg)
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

def to_thumbnail(newImg,(size)):
	imgThumb = img
	imgThumb.thumbnail((size))
	imgThumb.save(newImg)

def to_antialias((size)):
	newImg = img
	newImg.thumbnail((size),Image.ANTIALIAS)
	newName = "antialias-%s" %(nameImg)
	newImg.save(newName)

def to_rotate(angle):
	imgRotate = img.rotate(angle)
	newName = "%s-rotate-%d.jpg" %(nameImg[:-4],angle)
	imgRotate.save(newName)

def to_write(position,phrase):
	draw = ImageDraw.Draw(img)
	draw.text(position,phrase)
	newName = "%s-write.jpg" %(nameImg[:-4])
	img.save(newName)

info_image(img)
to_thumbnail(newImg,(size))
to_antialias((size))
to_rotate(angle)
to_write(position,phrase)

