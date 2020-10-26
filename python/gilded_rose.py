# -*- coding: utf-8 -*-


BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


def step_quality(item, rate=-1):
    item.quality = item.quality + rate if 0 <= item.quality + rate <= 50 else item.quality


def update_quality(item):
    if item.name not in {BRIE, BACKSTAGE_PASS, SULFURAS}:
        # Handle decaying
        if item.sell_in < 0:
            step_quality(item, -2)
        else:
            step_quality(item, -1)
    elif item.name == BACKSTAGE_PASS:
        if item.sell_in <= 0:
            # Quality drops to 0 after the concert
            step_quality(item, item.quality*-1)
        elif 0 < item.sell_in < 6:
            step_quality(item, 3)
        elif 6 <= item.sell_in < 11:
            step_quality(item, 2)
        elif 11 < item.sell_in:
            step_quality(item, 1)
    elif item.name == BRIE:
        step_quality(item, 1)

    if item.name != SULFURAS:
        item.sell_in = item.sell_in - 1


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
