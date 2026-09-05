import base64

encoded = "464c41477b6865785f69735f66756e7d"

decoded = base64.b64decode(encoded).decode()

print(decoded)
