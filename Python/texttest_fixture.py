# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
        Item(name="Ring of Cleansening Code", sell_in=10, quality=20),
        Item(name="Good Wine", sell_in=2, quality=0),
        Item(name="Elixir of the SOLID", sell_in=5, quality=7),
        Item(name="B-DAWG Keychain", sell_in=0, quality=80),
        Item(name="B-DAWG Keychain", sell_in=-1, quality=80),
        Item(name="Backstage passes for Re:Factor", sell_in=15, quality=20),
        Item(name="Backstage passes for Re:Factor", sell_in=10, quality=49),
        Item(name="Backstage passes for HAXX", sell_in=5, quality=49),
        # these smelly items do not work properly yet
        Item(name="Duplicate Code", sell_in=3, quality=6),
        Item(name="Long Methods", sell_in=3, quality=6),
        Item(name="Ugly Variable Names", sell_in=3, quality=6)
    ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
