def is_unique(str):
    alphabet=[True for y in range(255)]
    for i in range(len(str)):
        if (alphabet[(ord(str[i]))] == False):
           return False
        else:
            alphabet[(ord(str[i]))] = False
    return True

#print(is_unique("tes"))
#print(is_unique("test"))

str=["c","o","u",chr(1)]
print(is_unique(str))