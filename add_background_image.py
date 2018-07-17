import  PIL
from PIL import Image
import os 


## use this script to add a background image behind transparent globe image


# path of image you want to use as your background
backgroundimage = 'Path'

# Function to merge background image and globe images from path
def make_im(path):
    for filename in os.listdir(path):
        if filename.startswith('DWF'): # use these for specfic start name or filename.endswith for specfic ext. ending
            background = Image.open(backgroundimage) # open the background image
            foreground = Image.open(path + filename) # open each globe image
	
            background.paste(foreground, (-1, -1), foreground) # pastes the globe image on the background
            background.save('/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/globe_final/MOD_all_label_' + filename) # save the mergered image to chosen dir with your chosen name

#-------------- Run the function for your choosen path --------------------------- #
make_im('/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/globe_final/')

