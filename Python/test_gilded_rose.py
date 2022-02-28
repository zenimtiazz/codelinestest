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
        
    def test_GoodWine_increases_by_2_after_date_quality(self):
        items = [Item("Good Wine", 0, 37)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(39, items[0].quality)
        
    def test_GoodWine_hits50_quality(self):
        items = [Item("Good Wine", 20, 50)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(50, items[0].quality)


    def test_normal_item_quality(self):
        items = [Item("Ring of Cleansening Code", 10, 20)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(19, items[0].quality)   

    def test_normal_item_degrade_twice_as_fast(self):
        items = [Item("Ring of Cleansening Code", 0, 11)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(9, items[0].quality)
      
    #The quality of an item in never negative 
    
    def test_normal_item_stops_at_0(self):
        items = [Item("Ring of Cleansening Code", 10, 0)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(0, items[0].quality) 
        
    def test_backstage_pass_increases_quality(self):
        items = [Item("Backstage passes for Re:Factor", 15, 20)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(21, items[0].quality)
        
    def test_backstage_pass_stops_at_50(self):
        items = [Item("Backstage passes for Re:Factor", 15, 50)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(50, items[0].quality)
        
    def test_backstage_quality_double_increase_less_than_10_days(self):
        items = [Item("Backstage passes for Re:Factor", 10, 40)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(42, items[0].quality)
    
    def test_backstage_quality_triple_increase_less_than_5_days(self):
        items = [Item("Backstage passes for Re:Factor", 3, 25)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(28, items[0].quality)

    def test_backstage_pass_less_than_0(self):
        items = [Item("Backstage passes for Re:Factor", 0, 25)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(0, items[0].quality)
    
    def test_smelly_items_degrading(self):
        items = [Item("Duplicate Code",3 , 6)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(4, items[0].quality)

     
    def test_smelly_items_at_0_quality(self):
        items = [Item("Duplicate Code",0 , 40)]
        gilded = GildedRose(items)
        gilded.update_quality()
        self.assertEqual(36, items[0].quality)

if __name__ == '__main__':
    unittest.main()
