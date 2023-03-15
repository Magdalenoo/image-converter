import sys
import os
from PIL import Image

# Taking first argument, path of source folder with pictures
source = sys.argv[1]

# Second argument, directory to which new pictures will be saved
final = sys.arg[2]

if not os.path.exists(final):
    os.makedirs(final)

for filename in os.listdir(source):
    img = Image.open(f'{source}{filename}')
    clean = os.path.splitext(filename)[0]
    img.save(f'{final}{clean}.png', 'png')