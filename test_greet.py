from greet import greet


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_with_name_is_personalized():
    assert "Ali" in greet("Ali")
