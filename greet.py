def greet(name=None, loud=False):
    if name:
        msg = f"Hello {name} from the Fleet Sandbox!"
    else:
        msg = "Hello from the Fleet Sandbox!"
    return msg.upper() if loud else msg

def farewell(name=None, loud=False):
    if name:
        msg = f"Goodbye {name} from the Fleet Sandbox!"
    else:
        msg = "Goodbye from the Fleet Sandbox!"
    return msg.upper() if loud else msg
