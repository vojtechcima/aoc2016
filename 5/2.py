import hashlib
INPUT = "ugkcyxxp"
index = 0
password = "--------"
while "-" in password:
    h = str(hashlib.md5(INPUT + str(index)).hexdigest())
    if h.startswith("00000") and h[5].isdigit():
        if int(h[5]) < 8:
            if str(password[int(h[5])]) == "-":
                password = password[:int(h[5])] + \
                    h[6] + password[int(h[5]) + 1:]
    index += 1
result = password
print result
