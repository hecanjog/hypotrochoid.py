from PIL import Image, ImageDraw
import random
import math
from pippi import dsp

npoints = 1000
ncycles = 100
nframes = 15 * 10
w,h = 1280, 800

aa = dsp.breakpoint([ random.randint(1, 1000) for p in range(10) ], ncycles)
bb = dsp.breakpoint([ random.randint(1, 40) for p in range(10) ], ncycles)
cc = dsp.breakpoint([ random.randint(1, 40) for p in range(10) ], ncycles)

Rs = dsp.breakpoint([ random.randint(200, 255) for p in range(4) ], ncycles)
Gs = dsp.breakpoint([ random.randint(0, 255) for p in range(3) ], ncycles)
Bs = dsp.breakpoint([ random.randint(200, 255) for p in range(5) ], ncycles)

background = (random.randint(100, 200), random.randint(0, 255), random.randint(100, 200))

choosepoints = [ random.randint(0, 500) for p in range(ncycles * npoints * nframes) ]

y1ss = [ dsp.breakpoint([ random.randint(1, 50) for p in range(10) ], npoints) for s in range(ncycles) ]
x1ss = [ dsp.breakpoint([ random.randint(1, 50) for p in range(10) ], npoints) for s in range(ncycles) ]

counter = 0
for frame in range():
    i = Image.new('RGB', (w, h), background)

    draw = ImageDraw.Draw(i)

    for t in range(ncycles):
        R = int(Rs[t])
        G = int(Gs[t])
        B = int(Bs[t])

        a = aa[t]
        b = bb[t]
        c = cc[t]

        yoffset, xoffset = h / 2, w / 4 

        y1s = y1ss[t]
        x1s = x1ss[t]

        for p in range(npoints):
            # I took these equations from this dude: http://stackoverflow.com/a/22895353
            d = p * 2 * math.pi / npoints;
            y = int(yoffset + round((a - b) * math.sin(d) - c * math.sin((a - b) / b * d)))
            x = int(xoffset + round((a - b) * math.cos(d) - c * math.cos((a - b) / b * d)))

            if choosepoints[counter % len(choosepoints)] > 1:
                draw.point((x, y), fill=(R,G,B))
            else:
                y1 = int(y + y1s[p])
                x1 = int(x + x1s[p])

                draw.chord([x,y,x1,y1], x % 360, y % 360, fill=(R,G,B))

            counter += 1

    i.save('frames/hypo%i004.jpg' % frame)
