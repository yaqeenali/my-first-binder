#this code ensures that we can navigate the WiMSE repo across multiple systems
import subprocess
import os
#get top directory path of the current git repository, under the presumption that 
#the notebook was launched from within the repo directory
gitRepoPath=subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('ascii').strip()

#move to the top of the directory
os.chdir(gitRepoPath)

#file name of standard map of the world
firstMapName='Earthmap1000x500.jpg'

#file name of grayscale map of the world
grayscaleMapName='World_map_blank_without_borders.svg.png'

#file name of world map with "graticule" (lines)
#see https://en.wikipedia.org/wiki/Geographic_coordinate_system for more info
linedMapName='Equirectangular_projection_SW.jpg'

#file name of political world map
politicalMapName='2000px-Dünya.svg.png'

#loading image processing and manipulation package Pillow
# https://pillow.readthedocs.io/en/stable/
import PIL
from PIL import Image
import os
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np

firstMapPath=os.path.join(gitRepoPath,'images',firstMapName) 
firstMap= Image.open(firstMapPath)

#in order to display in jupyter, some trickery is necessary
%matplotlib inline
imshow(np.asarray(firstMap))
fig = plt.gcf()
fig.set_size_inches(15, 30)
