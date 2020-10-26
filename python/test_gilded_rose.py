# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_brie(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)

        update_quality(item)
        self.assertEqual(1, item.sell_in)
        self.assertEqual(1, item.quality)

        update_quality(item)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(2, item.quality)

        update_quality(item)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(3, item.quality)

    def test_sulfuras(self):
        item = Item(
            name="Sulfuras, Hand of Ragnaros",
            sell_in=0,
            quality=80
        )

        update_quality(item)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_backstage(self):
        item = Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=11,
            quality=20
        )

        update_quality(item)
        self.assertEqual(10, item.sell_in)
        self.assertEqual(20, item.quality)

        update_quality(item)
        self.assertEqual(9, item.sell_in)
        self.assertEqual(22, item.quality)

        for _ in range(4):
            update_quality(item)
        self.assertEqual(5, item.sell_in)
        self.assertEqual(30, item.quality)

        update_quality(item)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(33, item.quality)

        for _ in range(5):
            update_quality(item)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

        update_quality(item)
        self.assertEqual(-2, item.sell_in)
        self.assertEqual(0, item.quality)

        update_quality(item)
        self.assertEqual(-3, item.sell_in)
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
