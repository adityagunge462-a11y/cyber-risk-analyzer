import base64

encoded = "RkxBR3tzdGFydF9jdGY="

decoded = base64.b64decode(encoded).decode()

print(decoded)
