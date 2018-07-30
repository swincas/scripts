import imageio 
import os
from PIL import Image
imageio.plugins.ffmpeg.download()


#---=== choose path of images you want to merged together into a video --- 
path = '/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/globe_final/'


# --- create array of all files you want to merger from path ----- 
filelist = []
files = []

for filename in os.listdir(path):
	if filename.startswith('MOD_all_label_'): # or use .endswith to choose ext. type 
		files.append(filename) # add filename to the array 
		
files.sort() # sort the files into accessending order 

writer = imageio.get_writer('/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/DWF_World_15fps.mp4', fps = 15) #make path and name of video you want to create and choose frames per second with fps. 

# --- Create the video 
for im in files:
	writer.append_data(imageio.imread(path + im)) 
writer.close() 

