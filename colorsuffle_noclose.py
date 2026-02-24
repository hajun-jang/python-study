import os, random, time

os.system('cls')


def random_safe_unicode_char():
    while True:
        code_point = random.randint(1, 9999)
        # 서로게이트 문자 제거
        if 0xD800 <= code_point <= 0xDFFF:
            continue
        char = chr(code_point)
        if char.isprintable():
            return char

while True:
    word = ""
    for _ in range(random.randint(1, 250)):
        word += random_safe_unicode_char()
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    print(f"\033[38;2;{r};{g};{b}m{word}\033[0m")
    time.sleep(0.1)
