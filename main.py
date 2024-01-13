#Ahmed0or1
import glob
import PIL.Image
image_file = []
for image in glob.glob("*.png"):
    print('\n')
    try:
        image_name=image.split(".")[0]
        icon = PIL.Image.open(image)
        width, height = icon.size
        crop = width if width <= height else height
        icon = icon.crop(((width - crop) // 2, (height - crop) // 2, (width + crop) // 2, (height + crop) // 2)).resize((256,256))
        icon.save('./{}.ico'.format(image_name), format = 'ICO', sizes=[(256,256)], quality=95)
        print(image,'==>  Done! {}.icon'.format(image_name))
    except:
        print(image,'==>  Error!')
