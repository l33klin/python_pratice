#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2019-09-16 10:35
@Author  : Jann
@Contact : l33klin@gmail.com
@Site    : 
@File    : base64_to_image.py
@Desc    : Description
"""
import base64

image_str = ''''''


imgdata = base64.b64decode(image_str)
filename = 'to_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)
# f gets closed when you exit the with statement
# Now save the value of filename to your database

