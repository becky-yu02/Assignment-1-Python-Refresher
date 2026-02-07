def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""

    echo_part = text.split()[-1]
    # Add the last repetitions characters, then the last repetitions - 1,
    # ... then period at the end.
    if len(echo_part) < repetitions:
        echo_lines = [echo_part[-i:] for i in range(len(echo_part), 0, -1)]
    else:
        echo_lines = [echo_part[-i:] for i in range(repetitions, 0, -1)]

    return "\n".join(echo_lines) + "\n" + "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
