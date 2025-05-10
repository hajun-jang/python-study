import os, random, time

os.system('cls')
while True:
    word = ""
    for _ in range(random.randint(1, 100)):
        word += f"{chr(random.randint(32, 126))}"
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(f"\033[38;2;{r};{g};{b}m" + f"{word}" + "\033[0m")
    time.sleep(0.1)