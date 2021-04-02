import termios
import fcntl
import sys
import os


class Colours:
    c = '\033[0m'

    RedDark = '\033[31m'
    GreenDark = '\033[32m'
    YellowDark = '\033[33m'
    BlueDark = '\033[34m'
    PinkDark = '\033[35m'
    CyanDark = '\033[36m'

    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Pink = '\033[95m'
    Cyan = '\033[96m'


class Other:
    def __init__(self, minmax=(0, 0)):
        self.min = minmax[0]
        self.max = minmax[1]


class Style:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Standard(Style):
    def __init__(self):
        super().__init__(
            indicator=["○", "●"],
            colours=[Colours.Red, Colours.Green],
            selected=[Colours.Red, Colours.Green],
            separator=": "
        )


class Triangle(Style):
    def __init__(self):
        super().__init__(
            indicator=["▷", "▶"],
            colours=[Colours.Red, Colours.Green],
            selected=[Colours.Red, Colours.Green],
            separator=": "
        )


class Arrow(Style):
    def __init__(self):
        super().__init__(
            indicator=[" ", "→"],
            colours=["", Colours.Green],
            selected=[Colours.Red, Colours.Green],
            separator=" - "
        )


class Pipe(Style):
    def __init__(self):
        super().__init__(
            indicator=["┃", "┣"],
            colours=[Colours.GreenDark, Colours.Green],
            selected=[Colours.Red, Colours.Green],
            separator=" - "
        )


class MenuResponse:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Menu:
    def __init__(self, options={}, style: Style = Standard(), title=None, description=None, type="Single", complete=None):
        self.options = options
        self.style = style
        self.title = title
        self.description = description
        self.type = type
        self.complete = complete
        if type == "Multi" and not isinstance(complete, str):
            raise AttributeError("You must provide a string to submit the options")

    def read_single_keypress(self):
        fd = sys.stdin.fileno()
        flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
        attrs_save = termios.tcgetattr(fd)
        attrs = list(attrs_save)
        attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK | termios.ISTRIP | termios.INLCR | termios. IGNCR | termios.ICRNL | termios.IXON)
        attrs[1] &= ~termios.OPOST
        attrs[2] &= ~(termios.CSIZE | termios. PARENB)
        attrs[2] |= termios.CS8
        attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON | termios.ISIG | termios.IEXTEN)
        termios.tcsetattr(fd, termios.TCSANOW, attrs)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
        ret = []
        try:
            ret.append(sys.stdin.read(1))
            fcntl.fcntl(fd, fcntl.F_SETFL, flags_save | os.O_NONBLOCK)
            c = sys.stdin.read(1)
            while len(c) > 0:
                ret.append(c)
                c = sys.stdin.read(1)
        except KeyboardInterrupt:
            ret.append('\x03')
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
            fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
        return tuple(ret)

    def display(self):
        if self.type == "Single":
            selected = 0
            flattened = []
            items = 0
            typed = ""
            for key, item in self.options.items():
                if isinstance(item, dict):
                    items += len(list(item))
                    flattened += [(k, v) if not isinstance(v, Other) else v for k, v in item.items()]
                else:
                    items += 1
                    flattened.append((key, item))

            while True:
                os.system("clear")
                x = 0
                if self.title:
                    print(self.title)
                if self.description:
                    print(self.description)
                for option, text in self.options.items():
                    if isinstance(text, dict):
                        print(f"{' '*len(self.style.indicator[0])} {option}{self.style.separator}")
                        for option, text in text.items():
                            sel = int(x == selected)
                            indicator = self.style.indicator[sel]
                            colour = self.style.colours[sel]
                            if isinstance(text, Other):
                                if len(typed) > text.max:
                                    t = list(typed)
                                    t.insert(text.max, Colours.Red)
                                    text = "".join(t) + f" (Too long | {len(t)}/{text.max})" + Colours.c
                                    colour = Colours.YellowDark
                                elif len(typed) < text.min:
                                    text = Colours.Red + typed + ("-"*(text.min-len(typed))) + f" (Too short {len(typed)}/{text.min})" + Colours.c
                                    colour = Colours.YellowDark
                                else:
                                    text = typed
                            print(f"  {colour}{indicator}{Colours.c} {option}{self.style.separator}{text}")
                            x += 1
                    else:
                        sel = int(x == selected)
                        indicator = self.style.indicator[sel]
                        colour = self.style.colours[sel]
                        if isinstance(text, Other):
                            if len(typed) > text.max:
                                t = list(typed)
                                t.insert(text.max, Colours.Red)
                                text = "".join(t) + f" (Too long | {len(t)}/{text.max})" + Colours.c
                                colour = Colours.YellowDark
                            elif len(typed) < text.min:
                                text = Colours.Red + typed + ("-"*(text.min-len(typed))) + f" (Too short {len(typed)}/{text.min})" + Colours.c
                                colour = Colours.YellowDark
                            else:
                                text = typed
                        print(f"{colour}{indicator}{Colours.c} {option}{self.style.separator}{text}")
                        x += 1
                key = self.read_single_keypress()
                if key in [("\x03",), ("\x1b",)]:
                    if key == ("\x03",):
                        os.system("clear")
                        return MenuResponse(statsus="Failed", response=("Ctrl+C"))
                    break
                if key == ("\x1b", "[", "A"):
                    selected -= 1
                elif key == ('\x1b', '[', 'B'):
                    selected += 1
                elif key in [("\r",), ('\x1b', '[', 'C')]:
                    break
                elif isinstance(flattened[selected][1], Other):
                    if key == ('\x7f',):
                        typed = typed[:-1]
                    elif len(key[0]) == 1:
                        typed += key[0]
                else:
                    return MenuResponse(status="Failed", response=None)
                selected = max(0, min(selected, items-1))
            os.system("clear")
            if isinstance(flattened[selected][1], Other):
                if (flattened[selected][1].max > len(typed) >= flattened[selected][1].min):
                    return MenuResponse(statsus="Option", response=(flattened[selected][0], typed))
                else:
                    return MenuResponse(statsus="Failed", response=("Other did not meet length requirements"))
            return MenuResponse(statsus="Option", response=(flattened[selected][0]))
        elif self.type == "Multi":
            flattened = {}
            flattened[self.complete] = [0, "Submit"]
            selected = 0
            items = 1
            typed = ""
            for key, item in self.options.items():
                items += 1
                flattened[key] = [0, item]

            while True:
                os.system("clear")
                x = 0
                if self.title:
                    print(self.title)
                if self.description:
                    print(self.description)
                for option, text in flattened.items():
                    sel = int(x == selected)
                    indicator = self.style.indicator[sel]
                    on = self.style.selected[text[0]]
                    colour = self.style.colours[sel]
                    if isinstance(text[1], Other):
                        text = text[1]
                        if len(typed) > text.max:
                            t = list(typed)
                            t.insert(text.max, Colours.Red)
                            text = "".join(t) + f" (Too long | {len(t)}/{text.max})" + Colours.c
                            colour = Colours.YellowDark
                        elif len(typed) < text.min:
                            text = Colours.Red + typed + ("-"*(text.min-len(typed))) + f" (Too short {len(typed)}/{text.min})" + Colours.c
                            colour = Colours.YellowDark
                        else:
                            text = typed
                    else:
                        text = text[1]
                    if option == self.complete:
                        print(f"  {colour}{indicator}{Colours.c} {on}{option}{Colours.c}")
                    else:
                        print(f"  {colour}{indicator}{Colours.c} {on}{option}{self.style.separator}{text}{Colours.c}")
                    x += 1
                key = self.read_single_keypress()
                if key in [("\x03",), ("\x1b",)]:
                    if key == ("\x03",):
                        os.system("clear")
                        return MenuResponse(statsus="Failed", response=("Ctrl+C"))
                    break
                if key == ("\x1b", "[", "A"):
                    selected -= 1
                elif key == ('\x1b', '[', 'B'):
                    selected += 1
                elif key in [("\r",), ('\x1b', '[', 'C')]:
                    if selected == 0:
                        break
                    flattened[list(flattened.keys())[selected]][0] = int(not bool(flattened[list(flattened.keys())[selected]][0]))
                elif isinstance(flattened[list(flattened.keys())[selected]][1], Other):
                    if key == ('\x7f',):
                        typed = typed[:-1]
                    elif len(key[0]) == 1:
                        typed += key[0]
                else:
                    return MenuResponse(status="Failed", response=None)
                selected = max(0, min(selected, items-1))
            os.system("clear")
            out = []
            for k, v in flattened.items():
                if isinstance(v[1], Other):
                    if (v[1].max > len(typed) >= v[1].min) and v[0]:
                        out.append((k, typed))
                    elif not (v[1].max > len(typed) >= v[1].min) and v[0]:
                        return MenuResponse(statsus="Failed", response=("Other did not meet length requirements"))
                    else:
                        out.append((k, 0))
                else:
                    out.append((k, v[0]))
            return MenuResponse(statsus="List", response=(out))
        else:
            raise ValueError(f"{self.type} is not a valid type")


print(Menu(
    options={
        "Fast": "SPEED",
        "Average": "aight",
        "Slow": "speed up",
        "Other": Other(minmax=(2, 20))
    },
    style=Triangle(),
    title=f"{Colours.Green} Response Time",
    complete="Enter",
    type="Single"
).display().response)