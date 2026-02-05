def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""

    echo_list = list()
    # Add the last repetitions characters, then the last repetitions - 1,
    # ... then period at the end.
    for i in range(repetitions, 0, -1):    
        echo_list.append(text[-i:])

    return "\n".join(echo_list) + "\n" + "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
