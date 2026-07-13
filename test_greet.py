from greet import greet, farewell


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_personalizes_with_name():
    assert "Ali" in greet("Ali")


def test_greet_shouts_when_loud():
    assert greet("Ali", loud=True) == greet("Ali").upper()


def test_farewell_returns_a_farewell():
    assert "Goodbye" in farewell()


def test_farewell_mentions_the_sandbox():
    assert "Sandbox" in farewell()


def test_farewell_personalizes_with_name():
    assert "Ali" in farewell("Ali")


def test_farewell_shouts_when_loud():
    assert farewell("Ali", loud=True) == farewell("Ali").upper()
