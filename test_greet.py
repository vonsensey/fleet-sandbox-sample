from greet import greet


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_personalizes_with_name():
    assert "Ali" in greet("Ali")


def test_greet_shouts_when_loud():
    assert greet("Ali", loud=True) == greet("Ali").upper()


def test_greet_swedish_with_name():
    assert greet("Ali", lang="sv") == "Hej Ali från Fleet Sandbox!"


def test_greet_swedish_without_name():
    assert greet(lang="sv") == "Hej från Fleet Sandbox!"


def test_greet_swedish_loud():
    assert greet("Ali", lang="sv", loud=True) == "HEJ ALI FRÅN FLEET SANDBOX!"


def test_greet_english_is_default():
    assert greet("Ali") == greet("Ali", lang="en")


def test_greet_unsupported_language_raises():
    import pytest
    with pytest.raises(ValueError):
        greet("Ali", lang="fr")
