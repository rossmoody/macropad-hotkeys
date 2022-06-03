def test():
    print("Testy")

config = {
    "name": "CircuitPy Helper",
    "macros": [
        (0x607770, "Test", [test]),
    ],
}
