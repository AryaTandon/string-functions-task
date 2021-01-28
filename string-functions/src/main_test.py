import main

def test_capitalise_string():
    assert main.capitalise_string("word") == "word".upper()
    assert main.capitalise_string("one") == "one".upper()
    assert main.capitalise_string("two") == "two".upper()
    assert main.capitalise_string("three") == "three".upper()