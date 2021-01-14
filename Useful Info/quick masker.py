import cv2
import os

def createPatchMask():
    '''Method that will create a mask file for the desired squadron patch.'''

    for root, dirs, files in os.walk(".", topdown=False):
       for name in files:
        fileName = (os.path.join(root, name)).replace('.\\', "")
        print fileName

        if "_mask" not in fileName and ".py" not in fileName and "fallback" not in fileName:
            # Load image with alpha channel.
            img = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)
            # Get mask from alpha channel.
            mask = img[:, :, 3]
            # Save the mask.
            fileName = fileName.replace(".png","_mask.png")
            cv2.imwrite(fileName, mask)
    #--------------------------------------------------------------------------------------------------------------------------------------------#

createPatchMask()




