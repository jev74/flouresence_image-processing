#!/usr/bin/env python3
"""Convert fluorescence TIFF images into false-colored JPEG previews.

Install dependencies:
    python -m pip install tifffile numpy pillow imagecodecs

Run:
    python processed_images.py

The program asks for an input folder and filename-key/color mappings. It then
creates ``processed_images`` inside the input folder and writes JPEG previews
there. Original TIFF files are never modified.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd

import numpy as np
import tifffile
from PIL import Image


OUTPUT_FOLDER_NAME = "processed_images"
JPEG_QUALITY = 95
LOW_PERCENTILE = 0.0
HIGH_PERCENTILE = 99.8

ROYGBV_COLORS: dict[str, tuple[int, int, int]] = {
    "red": (255, 0, 0),
    "orange": (255, 127, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "violet": (148, 0, 211),
}


@dataclass(frozen=True)
class ChannelRule:
    keys: tuple[str, ...]
    color_name: str

@dataclass(frozen=True)
class top10:
    channel: str
    scores: tuple[int, ...]



def ask_channel_rules() -> list[ChannelRule]:
    """Interactively collect case-insensitive filename keys and ROYGBV colors."""
    print("\nAdd one channel's keys at a time seperate with semi colons. For example, mcherry, mchery, 587." \
    "Then declare the channel color from the ROYGBV options. ")
    print("Keys are any identifying label on the file names for what color they correspond to. "
        "You can custom enter them, and " \
    "if you made any spelling errors, while saving, making sure to add those" \
    "as additional keys!")

#TODO
    rules: list[ChannelRule] = []

    keys_empty = True
    while (keys_empty == True):
        raw_keys = input("\nChannel key(s) (click enter when done): ").strip()

        #TODO look at in morning
        keys = tuple(dict.fromkeys(k.strip().casefold() for k in raw_keys.split(",") if k.strip()))
        if keys.empty:
            print("No usable key was entered.")
            continue

        #TODO handle duplicates?
        duplicates = None
        if duplicates:
            print("Duplicates keys assigned. Try again!")
            continue

        color = input("Output color (red/orange/yellow/green/blue/violet): ").strip().casefold()
        if color not in ROYGBV_COLORS:
            print(f"Unknown color '{color}'. Please enter a ROYGBV color.")
            continue

        rules.append(ChannelRule(keys=keys, color_name=color))
        print(f"Added {', '.join(keys)} -> {color}")

        if input("add another channel? [y/n]").strip() == "n": 
            keys_empty = False

        return rules


def find_rule(filename: str, rules: list[ChannelRule]) -> ChannelRule | None:
    """Return the unique rule whose key occurs in filename."""
    lowered = filename.casefold()
    matches = [rule for rule in rules if any(key in lowered for key in rule.keys)]
    if not matches:
        return None
    if len(matches) > 1:
        labels = ["/".join(rule.keys) for rule in matches]
        raise ValueError("filename matches multiple channels: " + ", ".join(labels))
    return matches[0]


def saturated_pixels(file_path):
    pass

def maximum_signal(file_path): 
    pass


#TODO set color scaling ( i have on other user ) 
def determine_color_scaling(channels, rules,) -> pd.DataFrame: 
    script_folder = Path(__file__).resolve().parent


    for file_path in script_folder.iterdir():
        if file_path.is_file():
            saturated_pixels = saturated_pixels(file_path)
            if (saturated_pixels > None): 
                print(file_path.name + " is blown out")
            if maximum_signal(file_path) > ##sort top 10 into array, use
            ###this to scale the signal adjustment 

    scaling = {  : }
    return scaling


def processimages() -> None:
    rules = ask_channel_rules
    determine_color_scaling(rules, )


    script_folder = Path(__file__).resolve().parent
    for file_path in script_folder.iterdir():
        if file_path.is_file():
            color = find_rule


def main() -> None:
    rules = ask_channel_rules()
    processimages()

    print(f"Output folder: {folder / OUTPUT_FOLDER_NAME}")


if __name__ == "__main__":
    main()

