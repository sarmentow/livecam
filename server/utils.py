import glob
from PIL import Image

# filepaths
fp_in = "static/images/*.jpeg"
fp_out = "static/images/result.gif"

def make_gif():
    print("MAKING GIF")
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
    img = next(imgs)  # extract first image from iterator
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)


