import sys
import os 
from PIL import Image

#grab first and second argument in the command line using sys.argv
try:
    image_folder = sys.argv[1]
    output_folder = sys.argv[2]

    #use os.path module to check is new/exists, if not use makedirs to create new
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #loop through Pokedex using os listdir module
    #convert image to png using Image module, clean/exclude file extension .jpg
    #save .png to the new folder
    for filename in os.listdir(image_folder):
        image = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        image.save(f'{output_folder}{clean_name}.png', 'png')
    print('All set and done!')

except IndexError as err:
    print(f"Please enter a working and destinated folder begins with a '/' {err}")

