from app.utils import to_usd

def test_to_usd():
    #if large number, it should use thousands separator:
    assert to_usd(123456789.98) == "$123,456,789.98"
    #it should round to two decimals
    assert to_usd(0.45555) == "$0.46"


