from defusedxml import ElementTree as etree
import cairosvg
import os

svg_path = 'icon.svg'
cairosvg.svg2png(url=svg_path, write_to='icon-192.png', output_width=192, output_height=192)
cairosvg.svg2png(url=svg_path, write_to='icon-512.png', output_width=512, output_height=512)
print('Conversion successful')
