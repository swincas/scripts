import  PIL
from PIL import Image
import os 


backgroundimage = '/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/stars_all_labels.png'

def make_im(path):
	for filename in os.listdir(path):
		if filename.startswith('DWF'):
			background = Image.open(backgroundimage)
			foreground = Image.open(path + filename)
	
			background.paste(foreground, (-1, -1), foreground)
			background.save('/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/globe_final/MOD_all_label_' + filename)

testing = make_im('/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/globe_final/')

