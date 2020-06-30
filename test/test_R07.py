from R07 import say_hello

def test_R07_no_params():
    assert say_hello() == "Hello R-07!"

def test_R07_with_params():
    assert say_hello("Rahul") == "Hello, Rahul!"

