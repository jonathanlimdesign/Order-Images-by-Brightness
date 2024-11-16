#PURPOSE: Sort images by their brightness value and rename them with a desired naming convention
#DATE: 05/13/2024
#AUTHOR: JONATHAN JAE JUN LIM


# import modules
import os   
# make sure to "pip install opencv-python" in cmd
import cv2
# make sure to "pip install numpy" in powershell
import numpy as np

# Definition for getting monochromatic value of an image
def getMonoValue(texture):
    # Uncomment below to see where the script is clogging up
    #print(texture)
    img = cv2.imread(r'{}'.format(texture))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    avg = np.mean(hsv[:, 2])
    per = (avg/255)*100
    return per

# Definition for extracting file extension from a file
def getExt(image):
    extension = ''
    #Extract file name from variable "image"
    imageFile = image [0]
    #Flip image name (the file name, so that the extension are the beginning characters)
    imageFile = imageFile [::-1]

    #Add extension characters to variable "ext" and break loop after a "." is encountered
    for letter in imageFile:
        if letter == ".":
            break
        else:
            extension += letter
    #Reverse backwards-spelt variable "ext" so that it is normal again
    extension = extension [::-1]

    return extension


def main():
    # Get the path of script folder
    dirPath = input("What is the file location for organization: ")

    # Get files in selected folder
    files = os.listdir(dirPath)

    # Make dictionary for files
    fileDict = {}

    # Get target file name
    target = input("What is the name of this material?: ")
    #target = "Wood"

    # List of potential image file names
    extList = (".jpg", ".png", ".jpeg", ".webp", "jfif")

    # Get image files
    for name in files:
        for fileExt in extList:
            if fileExt in name:
                OGfile = dirPath + "/" + name
                #Get monochromatic value of image
                value = getMonoValue(OGfile)
                #Add image to dictionary
                fileDict["{}".format(name)] = value
            else:
                None

    #Order dictionary
    sortedDict = sorted(fileDict.items(), key=lambda x:x[1])

    #Setup number padding
    imageNum = 0
    numPad = '0'

    #Update image number padding
    for image in sortedDict:
        imageNum = int(imageNum) + 1
        imageNum = str(imageNum)

        #Get extension
        ext = getExt(image)

        #Check number padding
        if int(imageNum) >= 10:
            numPad = ''
        else:
            None

        #Create new file name
        newName = target + '_' + numPad + imageNum + '.' + ext



        # #Execute rename function
        OGfile = dirPath + '/' + image[0]
        newDest = dirPath + '/' + newName
        
        os.rename(OGfile, newDest)

if __name__ == '__main__':
    main()