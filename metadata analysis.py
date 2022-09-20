import PIL.Image

img = PIL.Image.open("resim1.jpg")

print(img._getexif())

import PIL.ExifTags

exif = {PIL.ExifTags.TAGS[key]: value for key, value in img._getexif().items() if key in PIL.ExifTags.TAGS}

exif

resim2 = PIL.Image.open("e_resim1.jpg")

exif2 = {PIL.ExifTags.TAGS[key]: value for key, value in img._getexif().items() if key in PIL.ExifTags.TAGS}

exif2

import piexif

exif_dict = piexif.load("e_resim1.jpg")

exif_dict