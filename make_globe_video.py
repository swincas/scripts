import imageio 
import os
from PIL import Image
imageio.plugins.ffmpeg.download()

#field = 'Antlia'
#cand = 100

path = '/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/globe_final/'

filelist = []
files = []
for filename in os.listdir(path):
	if filename.startswith('MOD_all_label_'):
		files.append(filename)
		
files.sort()
#print(files)

writer = imageio.get_writer('/Users/swebb/Documents/DWF/sky_plots/DWF_world_plot/images/DWF_World_15fps.mp4', fps = 15)

for im in files:
	test = path + im
	print(test)
	writer.append_data(imageio.imread(path + im))
writer.close() 

