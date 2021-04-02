import math
import time

text = {
    0: {
        0: "⠀",
        1: "⠠",
        2: "⠰",
        3: "⠸"
    },
    1: {
        0: "⠄",
        1: "⠤",
        2: "⠴",
        3: "⠼"
    },
    2: {
        0: "⠆",
        1: "⠦",
        2: "⠶",
        3: "⠾"
    },
    3: {
        0: "⠇",
        1: "⠧",
        2: "⠷",
        3: "⠿"
    }
}


class Graph:
    def __init__(self, data=[]):
        self.data = data

    def genString(self):
        data = self.data
        if len(data) % 2:
            data = data + [3]
        m = max(data)
        rows = math.ceil(m/3)
        r = []
        for y in range(rows):
            low = max(m - (y*3) - 3, 0)
            high = m - (y*3)
            pairs = []
            for x in range(0, len(data), 2):
                pairs.append((data[x], data[x+1]))
            s = ""
            for pair in pairs:
                h0, h1 = pair[0], pair[1]
                if pair[0] < low:
                    h0 = 3
                elif pair[0] > high:
                    h0 = 0
                else:
                    h0 = high - pair[0]
                if pair[1] < low:
                    h1 = 3
                elif pair[1] > high:
                    h1 = 0
                else:
                    h1 = high - pair[1]
                s += text[int(h0)][int(h1)]
            r.append(s)
        return r
