# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            if item.name == 'B-DAWG Keychain':
                item.quality = 80
                continue
            
            if item.name == 'Good Wine':
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    
            
            if item.name != "Good Wine" and item.name != "Backstage passes for Re:Factor" \
                    and item.name != "Backstage passes for HAXX":
                if item.quality > 0:
                    item.quality = item.quality - 1
           
                
                    if item.name == "Backstage passes for Re:Factor" or item.name == "Backstage passes for HAXX":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Good Wine":
                    if item.name != "Backstage passes for Re:Factor" and item.name != "Backstage passes for HAXX":
                        if item.quality > 0:
                            item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
               
                    


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
