def greet(name=None, loud=False):
    if name:
        msg = f"Hello {name} from the Fleet Sandbox!"
    else:
        msg = "Hello from the Fleet Sandbox!"
    return msg.upper() if loud else msg
