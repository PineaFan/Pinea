"""
0  1  2  3  4  5  6
--------------------
Bl Re Gr Ye Be Pu Cy

30  | Text
40  | Background
90  | Soft text
100 | Soft background

0 Clear
1 Bold
2 Underline
3 Italics

"""


class Colours:
    Black = 0
    Red = 1
    Green = 2
    Yellow = 3
    Blue = 4
    Magenta = 5
    Cyan = 6
    White = 7

    Text = 30
    Background = 40
    SoftText = 90
    SoftBackground = 100


def colour(text=0, soft_text: bool = False, background=0, soft_background: bool = False, decoration=""):
    if isinstance(text, int):
        text = max(min(text, 7), 0)
    if isinstance(background, int):
        background = max(min(background, 7), 0)
        if background == 0:
            background = 7
        elif background == 7:
            background == 0

    strings = {
        "black": 0,
        "red": 1,
        "green": 2,
        "blue": 4,
        "yellow": 3,
        "cyan": 6,
        "magenta": 5,
        "white": 7
    }

    if isinstance(text, str):
        text = strings[text.lower()]
    if isinstance(background, str):
        background = strings[background.lower()]

    decorations = ""
    if "b" in decoration:
        decorations += ";1"
    if "i" in decoration:
        decorations += ";3"

    if background is not None:
        background += Colours.SoftBackground if soft_background else Colours.Background
    else:
        background = ""
    if text is not None:
        text += Colours.SoftText if soft_text else Colours.Text
    else:
        text = ""

    return f"\033[{background};{text}{decorations}m"


def clear():
    return f"\033[0;0m"
