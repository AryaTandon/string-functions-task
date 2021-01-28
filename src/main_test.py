import main

def test_capitalise_string():
    assert main.capitalise_string("word") == "word".upper()

def test_capitalise_string2():
    assert main.capitalise_string("one") == "one".upper()

def test_capitalise_string3():
    assert main.capitalise_string("two") == "two".upper()

def test_capitalise_string4():
    assert main.capitalise_string("three") == "three".upper()