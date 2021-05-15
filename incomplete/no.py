import os
import colourterm
import time
import datetime
import random
import subprocess
import prettyprint as pp

th, tw = (int(i) for i in os.popen('stty size', 'r').read().split())


def printLines(lines):
    os.system("clear")
    s = "\n".join([str(l) for l in lines[-th:]])
    string = "  Please do not press any key while update is in progress"
    print(s + "\n" + colourterm.colour(text=("white" if int(datetime.datetime.utcnow().timestamp()) % 2 else "black"), background="red") + string + (" "*(tw-len(string))) + colourterm.clear(), end="\r")


count = 0
lines = [" "]*th
packages = [s.split(" ")[0] for s in str(subprocess.check_output(["pamac", "list"]))[1:-1].split("\\n")][:-1]

while True:
    for package in packages:
        time.sleep(random.randint(10,200)/100)
        updateLength = random.randint(1, 10)
        installLength = random.randint(1, 5)

        lines.append(f"\nPreparing...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Synchronizing package databases...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Resolving dependencies...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Checking inter-conflicts\n\n")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)

        lines.append(f"To install: ({updateLength})\n  {package}\n\n")
        printLines(lines)
        time.sleep(random.randint(100,200)/100)
        lines.append(f"Total download size: {random.randint(10, 100)}MB")
        lines.append(f"Total installed size: {random.randint(100, 500)}MB")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)

        for x in range(updateLength):
            start = f"Download of {package} started"
            end = f"[{x+1}/{updateLength}]"
            lines.append(f"{start}{' '*(tw-len(start)-len(end))}{end}")
            printLines(lines)
            time.sleep(random.randint(0,50)/100)
        lines.append(f"Checking keyring...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Checking integrity...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Loading package files...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Checking file conflicts...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Checking available disc space...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Installing discord (0.0.14-1)...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Running post-transaction hooks...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Arming ConditionNeedsUpdate...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Updating the desktop file MIME type cache...")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
        lines.append(f"Transaction successfully finished.")
        printLines(lines)
        time.sleep(random.randint(0,50)/100)
