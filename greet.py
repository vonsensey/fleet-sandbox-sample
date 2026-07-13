def greet(name=None, loud=False):
    if name is not None and not isinstance(name, str):
        raise TypeError(f"name must be str or None, got {type(name).__name__}")
    if name:
        msg = f"Hello {name} from the Fleet Sandbox!"
    else:
        msg = "Hello from the Fleet Sandbox!"
    return msg.upper() if loud else msg
