import os
import glob
from PIL import Image

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

screenshots = glob.glob(desktop+'/'+'Screenshot*.png')
print(screenshots)
screenshots.sort()
print(screenshots)

images = []
for f in screenshots:
    img = Image.open(f)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    images.append(img)

pdf_path = desktop + '/' + 'p.pdf'

images[0].save(
    pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)