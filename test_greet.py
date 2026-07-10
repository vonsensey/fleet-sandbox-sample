from greet import greet


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_personalizes_with_name():
    assert "Ali" in greet("Ali")
