# Pinea
A collection of utility programs, designed for me but can be used by anyone

-----


## Colourterm
> Coloured text in your terminal. Support for bold, italics and maybe others soon

### Support
OS      | Terminal       | Support
--------|----------------|---------
Linux   | TTYs           | Full
Linux   | Konsole        | Full
Linux   | Yakuake        | Part [1]
Windows | Command prompt | None
Windows | Powershell     | None
Windows | Terminal       | Full
macOS   | Terminal       | Full

Code | Missing
-----|-------------------
0    | Text colours
1    | Background colours
2    | Bold + Italics


Is your terminal not included? Create a PR and add it, along with its support level. <br> Linux should work assuming your terminal supports ANSI colour codes and has 8 bit colour depth

### Usage
```py
import colourterm

"""
colour = colourterm.colour(
  text=int|str,
  soft_text=bool,
  background=int|str,
  soft_background=bool,
  decoration=str
)
"""

colour = colourterm.colour(text='green', background='black', decoration='bi')
# Create green text on a black background. Set the text to bold and italics
print(f"{colour}Hello world!")

colour = colourterm.colour(text='red', soft_text=True)
# Create soft red text on no background.
# Soft can also be applied to the background with soft_background=True
# It is recommended that you colourterm.clear() if a background is used, to remove trailing backgrounds over multiple lines
print(f"{colour}Hello world!")

# Set text to the default colour, usually white text on no background
print(f"{colourterm.clear()}Hello world!")

"""
Colour codes can be either the name, or its value listed below:
0 black
1 red
2 green
3 yellow
4 blue
5 magenta
6 cyan
7 white
"""
```
