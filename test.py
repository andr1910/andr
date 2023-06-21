def str(data):
    for i in range(int(len(data)/2)):
        if data[i] != data[len(data)-i-1]:
            return False
    return True
print(str("abxba"))