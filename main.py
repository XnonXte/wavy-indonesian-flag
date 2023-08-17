"""
Indonesian flag animation in Python terminal.

(C) 2023 XnonXte
"""

import time
from colorama import Fore, init

# Autoreset enabled so it won't overflow to the next line.
init(autoreset=True)

# Text coloring with each of the corresponding character.
rp = Fore.RED + "+"
wm = Fore.WHITE + "-"


frames = [
    # Animation frames, based off this guideline on pinterest: https://i.pinimg.com/236x/64/5a/b5/645ab5c2df93402b0fad2482d166235c.jpg
    [
        "   #### ",
        f"    ##{rp}{rp}{rp}{rp}",
        f"    ##{rp*10}",
        f"    ##{wm*10}",
        f"    ##     {wm*5}",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
    ],
    [
        "   #### ",
        f"    ## {rp*4}",
        f"    ##{rp*10}",
        f"    ##{wm*10}",
        f"    ##     {wm*4}",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
    ],
    [
        "   #### ",
        f"    ##   {rp*4}",
        f"    ##{rp*10}",
        f"    ##{wm*10}",
        f"    ##---    ---",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
    ],
    [
        "   #### ",
        f"    ##++    {rp*3}",
        f"    ##{rp*10}",
        f"    ##{wm*10}",
        f"    ##  ----   -",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
        "    ##",
    ],
]


def print_frame(frame):
    print("\033[H\033[J")  # Clearing the terminal.
    for i in frame:
        print(i)
    time.sleep(0.25)


def main():
    while True:
        for i in frames:
            print_frame(i)


if __name__ == "__main__":
    main()
