from time import sleep

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        sleep(0.05)
    print()