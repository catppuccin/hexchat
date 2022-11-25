#!/usr/bin/env python3
"""
Generates a HexChat 'colors.conf' file for each flavour
of Catppuccin.
"""

from enum import Enum, auto
from pathlib import Path
from typing import TextIO

from catppuccin import Colour, Flavour

# how much to darken/lighten colours
COLOUR_MOD_PERCENT = 1.4

class ColourOp(Enum):
    LIGHTEN = auto()
    DARKEN = auto()

def redistribute_rgb(r, g, b):
    """
    all credit to: https://stackoverflow.com/a/141943
    """
    threshold = 255.999
    m = max(r, g, b)
    if m <= threshold:
        return int(r), int(g), int(b)
    total = r + g + b
    if total >= 3 * threshold:
        return int(threshold), int(threshold), int(threshold)
    x = (3 * threshold - total) / (3 * m - total)
    gray = threshold - x * m
    return int(gray + x * r), int(gray + x * g), int(gray + x * b)


def lighten(colour: Colour) -> Colour:
    r = colour.red * COLOUR_MOD_PERCENT
    g = colour.green * COLOUR_MOD_PERCENT
    b = colour.blue * COLOUR_MOD_PERCENT
    return Colour(*redistribute_rgb(r, g, b))


def darken(colour: Colour) -> Colour:
    r = colour.red / COLOUR_MOD_PERCENT
    g = colour.green / COLOUR_MOD_PERCENT
    b = colour.blue / COLOUR_MOD_PERCENT
    return Colour(*redistribute_rgb(r, g, b))

scheme = {
    0: {"colour": "text"}, # white
    1: {"colour": "base"}, # black
    2: {"colour": "blue"}, # blue
    3: {"colour": "green"}, # green
    4: {"colour": "red"}, # light red
    5: {"colour": "rosewater", "op": ColourOp.DARKEN}, # brown
    6: {"colour": "mauve"}, # purple
    7: {"colour": "peach"}, # orange
    8: {"colour": "yellow"}, # yellow
    9: {"colour": "green", "op": ColourOp.LIGHTEN}, # light green
    10: {"colour": "teal"}, # cyan
    11: {"colour": "teal", "op": ColourOp.LIGHTEN}, # light cyan
    12: {"colour": "sky"}, # light blue
    13: {"colour": "pink"}, # pink
    14: {"colour": "surface2"}, # grey
    15: {"colour": "overlay2"}, # light grey
    
    16: {"colour": "text"}, # white
    17: {"colour": "base"}, # black
    18: {"colour": "blue"}, # blue
    19: {"colour": "green"}, # green
    20: {"colour": "red"}, # light red
    21: {"colour": "rosewater", "op": ColourOp.DARKEN}, # brown
    22: {"colour": "mauve"}, # purple
    23: {"colour": "peach"}, # orange
    24: {"colour": "yellow"}, # yellow
    25: {"colour": "green", "op": ColourOp.LIGHTEN}, # light green
    26: {"colour": "teal"}, # cyan
    27: {"colour": "teal", "op": ColourOp.LIGHTEN}, # light cyan
    28: {"colour": "sky"}, # light blue
    29: {"colour": "pink"}, # pink
    30: {"colour": "surface2"}, # grey
    31: {"colour": "overlay2"}, # light grey

    256: {"colour": "text"}, # selected foreground
    257: {"colour": "surface2"}, # selected background
    258: {"colour": "text"}, # foreground
    259: {"colour": "base"}, # background
    260: {"colour": "overlay1"}, # interface marker line
    261: {"colour": "yellow"}, # interface new data
    262: {"colour": "green"}, # interface highlight
    263: {"colour": "blue"}, # interface new message
    264: {"colour": "overlay1"}, # interface away user
    265: {"colour": "maroon"}, # interface spell checker
}

def to_dupe(hex: str) -> str:
    components = [hex[x:x+2] * 2 for x in [0, 2, 4]]
    return " ".join(components)

def hex_from_scheme(flavour: Flavour, ctp) -> str:
    colour = getattr(flavour, ctp["colour"])
    match ctp.get("op"):
        case ColourOp.LIGHTEN:
            colour = lighten(colour)
        case ColourOp.DARKEN:
            colour = darken(colour)
    return colour.hex

def write_colours(flavour: Flavour, *, fp: TextIO) -> None:
    duped_scheme = { n: to_dupe(hex_from_scheme(flavour, c)) for n, c in scheme.items() }
    for n, dup in duped_scheme.items():
        print(f"color_{n} = {dup}", file=fp)

def main():
    for flavour in "latte", "frappe", "macchiato", "mocha":
        output_dir = Path(flavour)
        output_dir.mkdir(parents=True, exist_ok=True)
        colors_conf = output_dir / "colors.conf"

        flavour = getattr(Flavour, flavour)()
        with colors_conf.open("w") as fp:
            write_colours(flavour, fp=fp)
    pass

if __name__ == '__main__':
    main()