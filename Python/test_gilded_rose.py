# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
   
    def test_B_DAWG(self):
        items = [Item("B-DAWG Keychain", 20, 80)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(80, items[0].quality)
      
    def test_BDAWG_past_date(self):
        items = [Item("B-DAWG Keychain", 0, 80)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(80, items[0].quality)  
    
    def test_GoodWine_increases_in_quality(self):
        items = [Item("Good Wine", 2, 0)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(1, items[0].sell_in) 
        self.assertEqual(1, items[0].quality) 
if __name__ == '__main__':
    unittest.main()
