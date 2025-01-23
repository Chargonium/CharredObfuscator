import random
from base64 import urlsafe_b64encode

def get_char():
    """
    Generate a random Chinese character.
    :return: str, a single random Chinese character
    """
    chinese_base = 0x4E00  # Starting Unicode code point for Chinese characters
    chinese_end = 0x9FFF   # Ending Unicode code point for Chinese characters
    random_code_point = random.randint(chinese_base, chinese_end)
    return chr(random_code_point)

def binary_to_chinese(binary_data):
    chinese_base = 0x4E00
    result = ''

    for byte in binary_data:
        char = chr(chinese_base + byte)
        result += char
    return result

def chinese_to_binary(chinese_str):
    chinese_base = 0x4E00
    binary_data = bytearray()

    for char in chinese_str:
        byte = ord(char) - chinese_base
        binary_data.append(byte)

    return bytes(binary_data)

lines = []

with open("testing/main.py", "br") as file:
    for line in file.readlines():
        if line.startswith(b" ") or line.startswith(b"    "):
            lines[len(lines)-1] = lines[len(lines)-1]+line
        else:
            lines.append(line)


execChar = get_char()
decodeChar = get_char()
decode2Char = get_char()

argChar = get_char()
byteChar = get_char()
binDataChar = get_char()
charChar = get_char()

# These i also gotta define using execs :Troll:
bytearrayChar = get_char() # 
chineseBaseChar = get_char() # #
ordChar = get_char() #
bytesChar = get_char() # 

decode_chinese = f"""def {decode2Char}({argChar}):
    {binDataChar}={bytearrayChar}()
    for {charChar} in {argChar}:
        {byteChar}={ordChar}({charChar})-{chineseBaseChar};{binDataChar}.append({byteChar})

    return {bytesChar}({binDataChar})
"""

with open("testing/obf.py", "w", encoding="utf-8") as file:    
    
    tmp = f"{execChar}({decodeChar}('"
    for index, line in enumerate(lines):
        tmp += urlsafe_b64encode(line).decode()
        tmp += "'));"
        if not index == len(lines)-1:
            tmp+=f"{execChar}({decodeChar}('"


    lines = [
        f"from base64 import urlsafe_b64decode",
        f"exec(urlsafe_b64decode('{urlsafe_b64encode(f"{execChar}=exec".encode()).decode()}'))", # TODO : Make these definitions also happen inside some obfuscated execs !
        f"{execChar}(urlsafe_b64decode('{urlsafe_b64encode(f"{decodeChar}=urlsafe_b64encode".encode()).decode()}'));"
        f"{bytesChar}=bytes"
        f"{ordChar}=ord",
        f"{bytearrayChar}=bytearray",
        f"{chineseBaseChar}=0x4E00", 
        f"{execChar}({decodeChar}(\"{urlsafe_b64encode(decode_chinese.encode()).decode()}\"))"
    ]

    fillers = []
    filler_chars = []
    for _ in range(len(lines)):
        tmp = ""
        filler_chars.append(get_char())
        for _ in range(random.randint(100, 300)):
            tmp += get_char()
            pass
        fillers.append(tmp)

    for index, line in enumerate(lines):
        file.write(f"{filler_chars[index]}='{fillers[index]}';")
        file.write(f"{line}")
        if not index+1==len(lines):
            file.write(";")

    #file.write(f";{execChar}({decodeChar}('{urlsafe_b64encode(tmp.encode()).decode()}'))")

    