from PIL import Image#import the pillow library for python
import statistics#statistics help when finding the median
pic1=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/1.png")
pic2=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/2.png")
pic3=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/3.png")
pic4=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/4.png")
pic5=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/5.png")
pic6=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/6.png")
pic7=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/7.png")
pic8=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/8.png")
pic9=Image.open("/Users/danieljauregui/Desktop/CST205Proj1/9.png")
imagelist=[pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9]
print("The size of all the images is: ", pic1.size)#gets the size of original image
width=495
height=557
redPixelList=[]
greenPixelList=[]
bluePixelList=[]
redmpixel=0
bluempixel=0
greenmpixel=0
newImage=Image.new("RGB",(495,557))#Creates new image with the intended height and width
for x in range(0,width):#nested loop to control pixel manipulation and to find median
	for y in range(0,height):
		for Image in imagelist:
			myred,myblue,mygreen=Image.getpixel((x,y))
			redPixelList.append(myred)
			greenPixelList.append(mygreen)
			bluePixelList.append(myblue)
		redmpixel=statistics.median(redPixelList)
		greenmpixel=statistics.median(greenPixelList)
		bluempixel=statistics.median(bluePixelList)
		bluePixelList=[]#clears the lists
		greenPixelList=[]
		redPixelList=[]
		newImage.putpixel((x,y),(redmpixel,greenmpixel,bluempixel))#Puts pixels in new image


newImage.show()
