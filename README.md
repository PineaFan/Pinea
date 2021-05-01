# Pinea
A collection of utility programs

---
## Contents
- <a href="#colourterm"> Colourterm</a>
- <a href="#options"> Options</a>
- <a href="#prettyprint"> Prettyprint</a>

<hr id="colourterm">

## Colourterm
> Coloured text in your terminal. Support for bold, italics and maybe others soon

### Support
OS      | Terminal         | Support
--------|------------------|---------
Linux   | TTYs             | Full
Linux   | Konsole          | Full
Linux   | Yakuake          | Part [1]
Windows | Command prompt   | None [012]
Windows | Powershell       | None [012]
Windows | Windows Terminal | Full
macOS   | Terminal         | Full

Code | Missing
-----|-------------------
0    | Text colours
1    | Background colours
2    | Bold + Italics


> Is your terminal not included? Create a PR and add it, along with its support level. <br> Linux should work assuming your terminal supports ANSI colour codes and has 8 bit colour depth

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
# It is recommended that you colourterm.clear() if a background is used, to remove trailing backgrounds over multiple lines
print(f"{colour}Hello world!")

colour = colourterm.colour(text='red', soft_text=True)
# Create soft red text on no background.
# Soft can also be applied to the background with soft_background=True
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

<hr id="prettyprint">

## Prettyprint
> Easily print a complex data structure

### Support
OS      | Terminal         | Support
--------|------------------|---------
Linux   | TTYs             | Full
Linux   | Konsole          | Full
Linux   | Yakuake          | Full
Windows | Command prompt   | Part [0]
Windows | Powershell       | Part [0]
Windows | Windows Terminal | Full
macOS   | Terminal         | Full

Code | Missing
-----|-------------
0    | Text colours

> Is your terminal not included? Create a PR and add it, along with its support level.

### Usage
```py
import prettyprint

"""
prettyprint.pprint(
  data=any,  # Data to print
  indent: int = 4,  # How far indented each list, tuple etc. should be indented
  show_types: bool = False,  # If the type of each item should be shown e.g. <int>
  colour_coded: bool = True,  # If colours should be used to show different types
  cutoff: bool = True,  # If text over multiple lines should be cut off
  debug: bool = False,  # Show length of itterables,
  return_string: bool = False  # Does not automatically print, but instead returns the string it processed
)
"""

# Enabling debug will automatically enable show_types

prettyprint.pprint(
  {"a": [1, 2], "b": {1.4, False}, "c": [1, 2, [3, (4, 5)]]},
  debug=True
)

"""
<dict | Length: 3> {
    <str | Length: 1> a: <list | Length: 2> [
        <int> 1
        <int> 2
    ]
    <str | Length: 1> b: <set | Length: 2> {
        <bool> False
        <float> 1.4
    }
    <str | Length: 1> c: <list | Length: 3> [
        <int> 1
        <int> 2
        <list | Length: 2> [
            <int> 3
            <tuple | Length: 2> (
                <int> 4
                <int> 5
            )
        ]
    ]
}
"""
```