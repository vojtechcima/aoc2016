import hashlib
INPUT = "ugkcyxxp"
index = 0
password = ""
while len(password) < 8:
    h = str(hashlib.md5(INPUT + str(index)).hexdigest())
    if h.startswith("00000"):
        password += h[5]
    index += 1
result = password
print result
