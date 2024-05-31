from rembg import remove #pip install rembg (if it's not working then you install) pip install rembg==2.0.28
from PIL import Image  #pip install pillow
input_path = '11.jpg'
output_path = "ironman.png"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)