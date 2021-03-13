import smartcrop
from PIL import Image


def scrop(image_location, width=100, height=100):

    image = Image.open(image_location)

    sc = smartcrop.SmartCrop()
    result = sc.crop(image, width, height)

    box = (result['top_crop']['x'],
           result['top_crop']['y'],
           result['top_crop']['width'] + result['top_crop']['x'],
           result['top_crop']['height'] + result['top_crop']['y'])

    image_debug = sc.debug_crop(image, result['top_crop'])
    image_debug.save(image_location.rsplit('/', 1)[0] + '/debug_output.jpg')

    # Here the image "im" is cropped and assigned to new variable im_crop
    im_crop = image.crop(box)
    im_crop.save(image_location.rsplit('/', 1)[0] + '/output.jpg')
