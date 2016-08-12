# skeleton code for obamicon from PIL import Image
from PIL import Image
Unicorn = Image.open("Unicorn..jpg")
pixel_list = list(Unicorn.getdata())
# =============================================================== # define colors as variables so we can recall them later: #
dark_blue=(0, 51, 76) 
red=(217, 26, 33)
light_blue=(112, 150, 158) 
yellow=(252, 227, 166) 

colors_list=[]
 
# =============================================================== # define a function that obama-fies the image. # this function will take your images' pixel list as a parameter. # for each pixel in your image's pixel list, "obama-fy" it by # creating a new RGB value (dark blue, red, light blue, or yellow) # based on the intensity of that pixel. return a pixel list # containing the RGB values of the obamafied picture. # ===============================================================
 
# Alexia=Image.open("Unicorn..jpg")
def obamafy(pixel_list):


	 # tuple = (1,2,3) # list = [1,2,3] # tuple[0] # give me 1
# Change the values so the pixel color changes # - Based on the rules below, change that pixel color from the original color to either dark blue, red, light blue, or yellow
# If the intensity < 182, then it's dark blue # If the intensity is between 182 and 364, then it's red # If the intensity is between 364 and 546, then it's light blue # all other intensity values, it is yellow
	# colors_list.append("dark_blue, red, light_blue, yellow")

# if intensity is < 182 then add dark blue to the new list 
# 	elif intensity is >= 182 and < 364 then add red to the new list
# 	elif intensity is >= 364 and < 546 then add light blue to the new list 
# 	else add yellow to the new list

	for item in pixel_list:
		intensity = item[0] + item[1] + item[2]
		if intensity <= 182:
			colors_list.append(dark_blue) #should change inten. color..
		elif intensity >= 182 and intensity < 364:
			colors_list.append(red)
		elif intensity >= 364 and intensity < 546:
			colors_list.append(light_blue)
		else:
			colors_list.append(yellow)

# return the pixel list i was given that i edited to contain the RGB values of the obamafied picture.
	return colors_list

obamafy(pixel_list)
Unicorn.putdata(colors_list)
Unicorn.show()
