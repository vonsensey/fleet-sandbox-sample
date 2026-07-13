def greet(name=None, loud=False):
    if name:
        msg = f"Hello {name} from the Fleet Sandbox!"
    else:
        msg = "Hello from the Fleet Sandbox!"
    return msg.upper() if loud else msg


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description="Fleet Sandbox greeting")
    parser.add_argument("name", nargs="?", default=None, help="name to greet")
    parser.add_argument("--loud", action="store_true", help="shout the greeting")
    args = parser.parse_args(argv)
    print(greet(args.name, loud=args.loud))


if __name__ == "__main__":
    main()
