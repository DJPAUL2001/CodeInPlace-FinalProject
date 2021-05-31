'''
Created on May 22, 2021

@author: Dhruba Jyoti Paul
'''
from simpleimage import SimpleImage
import random

def main():
    print("Input nothing for default values\n")
    
    PATCH_NAME = 'images/simba-sq.jpg'
    imgAddr = input("Provide Image Address (relative): ")
    if imgAddr != "":
        PATCH_NAME = imgAddr
    
    try:
        image = SimpleImage(PATCH_NAME)
    except:
        input("Image not found...")
        return

    while True:
        userInput = input("\nChoose an action: \n[c] - create color collage\n[m] - create mirror image\n[q] - quit program\n")
        if userInput == "c" or userInput == "C":
            image = createColorCollage(image)
        elif userInput == "m" or userInput == "M":
            image = mirror(image)
        elif userInput == "q" or userInput =="Q":
            break
        else:
            continue
    
    # print("\nARE YOU REALLY QUITTING ON ME? ;-;\nFINE! BE THAT WAY! I don't really care anyway.")
    # print(" ╭╭━━━━━━╮╮┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫\n┈┈┈▏┏┳━━━━▏┏┳━━╯\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈\n\n")
    # input("Byeeeeeeeeee\nThank you for using this program. :-) \nPress enter to exit\n")
    input("Byeeeeeeeeee\nThank you for using this program. :-) \nPress enter to exit\n")
def mirror(image):
    
    while True:
        userInput = input("\t[r] - mirror right\n\t[d] - mirror down\n")
        
        if userInput == "r" or userInput == "R":
            return mirrorRight(image)
            break
        elif userInput == "d" or userInput == "D":
            return mirrorDown(image)
            break
        else:
            print("\tInvalid input. Try again")
            continue
    
def mirrorDown(image):
    print("\tCreating mirror image")

    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width, height * 2)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, (height * 2) - (y + 1), pixel)
    
    print("\tMirror Image Created!")
    mirror.show()
    return mirror

def mirrorRight(image):
    """
    Reads image from file specified by filename. 
    Returns a new image that includes the original image 
    and its mirror reflection.   
    """
    print("\tCreating mirror image")
    width = image.width
    height = image.height 
    
    # Create new image to contain mirror reflection
    mirror = SimpleImage.blank(width * 2, height)

    for y in range(height):
        for x in range(width): 
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel((width * 2) - (x + 1), y, pixel)
           
    print("\tMirror Image Created!") 
    mirror.show()
    return mirror
    
def createColorCollage(image):
    # DEFAULT VARIABLES FOR COLLAGE
    N_ROWS = 2
    N_COLS = 3
    
    #Gathering information from the user! :D
    print("\n\tInput nothing for default values\n")

    rows = input("\tProvide Number of Rows (non-zero positive integer): ")
    if rows != "":
        N_ROWS = int(rows)
        
    cols = input("\tProvide Number of Columns (non-zero positive integer): ")
    if cols != "":
        N_COLS = int(cols)
    
    WIDTH = N_COLS * image.width
    HEIGHT = N_ROWS * image.height
    
    # Staring Collage Creation
    print("\n\tCreating ColorCollage!")
    
    # Creating a blank canvas and drawing on it
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
        
    for i in range(N_ROWS):
        for j in range(N_COLS):
            colorPatch(image, final_image, i, j)
            print("\t(Row: " + str(i + 1) + ", Col: " + str(j + 1) + ") Done!")
    
    # Displaying the image
    print("\tColorCollage created! :D")
    final_image.show()
    
    return final_image
    
def colorPatch(origImg, final_image, row, col):
    
    # Creating new image copy for filter
    image = SimpleImage.blank(origImg.width, origImg.height)
    
    for x in range(origImg.width):
        for y in range(origImg.height):
            image.set_pixel(x, y, origImg.get_pixel(x,y))
        
    
    patchImage = make_recolored_patch(image, random.uniform(0.8, 2.0), random.uniform(0.8, 2.0), random.uniform(0.8, 2.0))
    
    addY = row * patchImage.height # as y in range of patch_height
    addX = col * patchImage.width # as x in range of patch_width
    
    for x in range(patchImage.width):
        for y in range(patchImage.height):
            px = patchImage.get_pixel(x, y)
            final_image.set_pixel(addX + x, addY + y, px)
    
    return final_image

def make_recolored_patch(image, red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    for px in image:
        px.red = px.red * red_scale
        px.green = px.green * green_scale
        px.blue = px.blue * blue_scale
    return image

if __name__ == '__main__':
    main()
