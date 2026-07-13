from greet import greet, greet_many


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_personalizes_with_name():
    assert "Ali" in greet("Ali")


def test_greet_shouts_when_loud():
    assert greet("Ali", loud=True) == greet("Ali").upper()


def test_greet_many_returns_one_per_name():
    assert greet_many(["Ali", "Bob"]) == [greet("Ali"), greet("Bob")]


def test_greet_many_empty_returns_empty_list():
    assert greet_many([]) == []


def test_greet_many_loud_propagates():
    result = greet_many(["Ali"], loud=True)
    assert result == [greet("Ali").upper()]
