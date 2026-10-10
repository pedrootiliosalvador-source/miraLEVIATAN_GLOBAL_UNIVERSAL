from leviathan_universal.core import build_message


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Mira Leviathan Global Universal")
    parser.add_argument("--name", default="Developer", help="Name to personalize the welcome message")
    args = parser.parse_args()

    print(build_message(args.name))


if __name__ == "__main__":
    main()
