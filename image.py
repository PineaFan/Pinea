from PIL import Image
from numpy import asarray
import os
import math
import pineaprint as pp


def printcol(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


# Fetch terminal size
th, tw = os.popen('stty size', 'r').read().split()
terminal = math.floor(int(tw)/2), int(th)

# Download image
image = Image.open("cmp.png")  # Add filename here
data = asarray(image)
size = image.size

# Scaling
if terminal[0] > size[0] or terminal[1] > size[1]:
    scale = ("repeat", math.floor(min(size[0] / terminal[0], size[1] / terminal[1])))
else:
    scale = ("skip", math.floor(max(size[0] / terminal[0], size[1] / terminal[1])))

# Display
countx = -1
county = -1
for x in data:
    county += 1
    if county % scale[1] != 0 and scale[0] == "skip":
        continue
    string = ""
    for y in x:
        countx += 1
        if countx % scale[1] != 0 and scale[0] == "skip":
            continue
        lis = y.tolist()
        s = printcol(lis[0], lis[1], lis[2])
        string += f"{s}██" * (scale[1] if scale[0] == "repeat" else 1)
    print(string)
