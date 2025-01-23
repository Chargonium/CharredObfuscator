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

chinese_base = 0x4E00

def binary_to_chinese(binary_data): return "".join([chr(chinese_base+ord(byte)) for byte in binary_data])

def chinese_to_binary(chinese_str): return "".join([chr(ord(char)-chinese_base) for char in chinese_str])

lines = []

#with open("testing/main.py", "br") as file:
#    for line in file.readlines():
#        if line.startswith(b" ") or line.startswith(b"    "):
#            lines[len(lines)-1] = lines[len(lines)-1]+line
#        else:
#            lines.append(line)


execChar = "".join([get_char() for _ in range(random.randint(20,50))])
decodeChar = "".join([get_char() for _ in range(random.randint(20,50))])
decode2Char = "".join([get_char() for _ in range(random.randint(20,50))])

argChar = "".join([get_char() for _ in range(random.randint(20,50))])
byteChar = "".join([get_char() for _ in range(random.randint(20,50))])
binDataChar = "".join([get_char() for _ in range(random.randint(20,50))])
charChar = "".join([get_char() for _ in range(random.randint(20,50))])

# These i also gotta define using execs :Troll:
bytearrayChar = "".join([get_char() for _ in range(random.randint(20,50))])
chineseBaseChar = "".join([get_char() for _ in range(random.randint(20,50))])
ordChar = "".join([get_char() for _ in range(random.randint(20,50))])
bytesChar = "".join([get_char() for _ in range(random.randint(20,50))]) 

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
        f"from base64 import urlsafe_b64decode as A",
        f"exec(A('{urlsafe_b64encode(f"{execChar}=exec".encode()).decode()}').decode())", 
        f"{execChar}(A('{urlsafe_b64encode(f"{decodeChar}=A".encode()).decode()}').decode())",
        f"{execChar}({decodeChar}('{urlsafe_b64encode(f"{bytesChar}=bytes".encode()).decode()}').decode())",
        f"{execChar}({decodeChar}('{urlsafe_b64encode(f"{ordChar}=ord".encode()).decode()}').decode())",
        f"{execChar}({decodeChar}('{urlsafe_b64encode(f"{bytearrayChar}=bytearray".encode()).decode()}').decode())",
        f"{execChar}({decodeChar}('{urlsafe_b64encode(f"{chineseBaseChar}=0x4E00".encode()).decode()}').decode())",
        f"{execChar}({decodeChar}('{urlsafe_b64encode(decode_chinese.encode()).decode()}').decode())"
    ]

    fillers = []
    filler_chars = []
    payload_index = random.randrange(0, len(lines)-1)
    with open("testing/main.py", "br") as payload_file:
        payload = urlsafe_b64encode(payload_file.read()).decode()
    print(payload)
    payload = binary_to_chinese(f"exec(A('{payload}').decode())")
    print(payload)

    for index in range(len(lines)):
        tmp = ""
        filler_chars.append("".join([get_char() for _ in range(random.randint(20,50))]))
        payloadlen = len(payload)
        minlen = payloadlen-20 if payloadlen > 20 else 1
        maxlen = payloadlen+20

        tmp = payload if index==payload_index else "".join([get_char() for _ in range(random.randint(minlen, maxlen))])

        fillers.append(tmp)

    for index, line in enumerate(lines):
        file.write(f"{filler_chars[index]}='{fillers[index]}';")
        file.write(f"{line};")

    file.write(f"{execChar}({decode2Char}({filler_chars[payload_index]}).decode())")

    