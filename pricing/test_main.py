from main import Quote,quote
def test_quote():
    assert quote(Quote(nightly=100,nights=2))['total']=='224.00'
