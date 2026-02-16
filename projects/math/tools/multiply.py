def multiply (args: str) -> str:
    x, y = map(float, args.split())
    return str(x * y)