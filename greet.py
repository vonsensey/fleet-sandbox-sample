def greet(name=None, loud=False):
    if name:
        msg = f"Hello {name} from the Fleet Sandbox!"
    else:
        msg = "Hello from the Fleet Sandbox!"
    return msg.upper() if loud else msg


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description="Fleet Sandbox greeting.")
    parser.add_argument("--name", default=None, help="Name to greet.")
    parser.add_argument("--loud", action="store_true", help="Shout the greeting.")
    args = parser.parse_args(argv)

    msg = greet(args.name, loud=args.loud)
    print(msg)
    return msg


if __name__ == "__main__":
    main()
