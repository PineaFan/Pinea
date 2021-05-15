import os
import prettyprint as pp

def printcol(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

for r in range(0, 255):
    pass

th, tw = os.popen('stty size', 'r').read().split()
th, tw = int(th), int(tw)

wcols = []
count = 0
for _ in range(0, tw):
    wcols.append(round(count))
    count += 255/tw
hcols = []
count = 0
for _ in range(0, th):
    hcols.append(round(count))
    count += 255/th

r = 0
while True:
    r = (r + 1) % 256
    string = []
    for g in range(0, len(hcols)):
        string.append("")
        for b in range(0, len(wcols)):
            string[-1] += f"{printcol(r, g, b)}█"
    print("".join(string))