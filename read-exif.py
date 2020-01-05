#!/usr/local/bin/python3

import sys
from PIL import Image, ExifTags

##カメラ機種：Model
##レンズ種別：Lens
##ISO:ISO
##焦点距離：FocalLength
##絞り:FNumber
##シャッタースピード：ShutterSpeed
my_exif_dict={36867:'DateCreated',
271:'Make',272:'Model',
272:'Model',42035:'LensMake',42036:'LensModel',
33434:'ExposureTime',33437:'FNumber',
34855:'ISOSpeedRatings',37386:'FocalLength'}

value = sys.argv
file = value[1]

img = Image.open(file)
img_exif = img.getexif()

if img_exif:
    img_exif_dict = dict(img_exif)
    for key in my_exif_dict.keys():
     try:
      val = img_exif_dict[key]
      print(ExifTags.TAGS[key]+"--"+str(val))
     except KeyError:
      print(ExifTags.TAGS[key]+"--")
else:
    print("No exif data")

#参考
#KeyErrorの回避方法
#https://techacademy.jp/magazine/20693
#exif 規格
#http://www.cipa.jp/std/documents/j/DC-008-2012_J.pdf
