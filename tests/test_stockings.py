from deuxmasbot.stockings import Stocking, Gift

import pytest

def test_gift_has_associated_sprite():
    g =  Gift.generate_gift()
    sprite = g.sprite
    open(sprite) # will except if invalid

def test_generates_gift():
    s = Stocking()
    assert s.gift

@pytest.mark.skip(reason='not implemented yet')
def test_stocking_collection_size():
    pass
