#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Image module for inkycal Project
Copyright by aceisace
Development satge: Beta
"""

from os import path
from PIL import ImageOps
import requests
import numpy

"""----------------------------------------------------------------"""
#path = 'https://github.com/aceisace/Inky-Calendar/raw/master/Gallery/Inky-Calendar-logo.png'
#path  ='/home/pi/Inky-Calendar/images/canvas.png'
path      = inkycal_image_path
path_body = inkycal_image_path_body
mode = 'auto'         # 'horizontal' # 'vertical' # 'auto'
upside_down = False    # Flip image by 180 deg (upside-down)
alignment = 'center'  # top_center, top_left, center_left, bottom_right etc.
colours = 'bwr'       # bwr # bwy # bw
render = True         # show image on E-Paper?
"""----------------------------------------------------------------"""

# First determine dimensions
if mode == 'horizontal':
  display_width, display_height == display_height, display_width


    
print('Done')
