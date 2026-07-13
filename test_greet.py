from greet import greet, main


def test_greet_returns_a_greeting():
    assert "Hello" in greet()


def test_greet_mentions_the_sandbox():
    assert "Sandbox" in greet()


def test_greet_personalizes_with_name():
    assert "Ali" in greet("Ali")


def test_greet_shouts_when_loud():
    assert greet("Ali", loud=True) == greet("Ali").upper()



def test_main_default_greeting(capsys):
    result = main([])
    assert result == "Hello from the Fleet Sandbox!"
    assert capsys.readouterr().out.strip() == result


def test_main_loud_personalized(capsys):
    result = main(["--name", "Ali", "--loud"])
    assert result == "HELLO ALI FROM THE FLEET SANDBOX!"
    assert capsys.readouterr().out.strip() == result
