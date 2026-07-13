def greet(name=None, loud=False, lang="en"):
    if lang == "sv":
        msg = f"Hej {name} från Fleet Sandbox!" if name else "Hej från Fleet Sandbox!"
    elif lang == "en":
        msg = f"Hello {name} from the Fleet Sandbox!" if name else "Hello from the Fleet Sandbox!"
    else:
        raise ValueError(f"Unsupported language: {lang!r}")
    return msg.upper() if loud else msg
