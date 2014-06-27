from PIL import Image, ImageDraw
import random
import math
from pippi import dsp

npoints = 1000
ncycles = 500
w,h = 2000, 2000

i = Image.new('RGB', (w, h), (255,255,255))

draw = ImageDraw.Draw(i)

aa = dsp.breakpoint([ dsp.randint(10, 1000) for p in range(10) ], ncycles)
bb = dsp.breakpoint([ dsp.randint(10, 40) for p in range(10) ], ncycles)
cc = dsp.breakpoint([ dsp.randint(10, 40) for p in range(10) ], ncycles)

R,G,B = random.randint(0,255), random.randint(0,255), random.randint(0,255)

for t in range(ncycles):
    R = (t / 3) % 255

    a = aa[t]
    b = bb[t]
    c = cc[t]

    yoffset, xoffset = h / 2, w / 2 

    for p in range(npoints):
        # I took these equations from this dude: http://stackoverflow.com/a/22895353
        d = p * 2 * math.pi / npoints;
        y = yoffset + round((a - b) * math.sin(d) - c * math.sin((a - b) / b * d))
        x = xoffset + round((a - b) * math.cos(d) - c * math.cos((a - b) / b * d))

        draw.point((x, y), fill=(R,G,B))

i.save('hypo.jpg')
