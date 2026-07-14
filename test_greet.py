from greet import greet, shout


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_personalizes_with_name():
    assert "Ali" in greet("Ali")


def test_greet_shouts_when_loud():
    assert greet("Ali", loud=True) == greet("Ali").upper()


def test_shout_uppercases_with_bang():
    assert shout("hello") == "HELLO!"
    assert shout("Hi there") == "HI THERE!"
