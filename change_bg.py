# UTF-8
# By lizhaofu
from PIL import Image
from removebg import RemoveBg
import os


def change_background(path, color="red",
                      key="cLL287gL9uoGA8P3L1mgwcXU"):
    rmbg = RemoveBg(key, "error.log")
    for pic in os.listdir(path):
        if "_no_bg.png" not in pic:
            # print(pic)
            rmbg.remove_background_from_img_file(os.path.join(path, pic))
            # print("ok")
    for pic in os.listdir(path):
        if "_no_bg.png" in pic:
            im = Image.open(os.path.join(path, pic))
            x, y = im.size
            # print(x, y)
            try:
                p = Image.new('RGB', im.size, color)
                p.paste(im, (0, 0, x, y), im)
                p.save(os.path.join(path, pic) + color + '1.jpg')
            except:
                pass


path = 'picture2'
change_background(path)










