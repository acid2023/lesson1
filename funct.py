def get_summ(one, two, delimiter='&'):
    str1 = str(one)
    str2 = str(two)
    return str1 + delimiter + str2 
print(get_summ('Learn', 'python').upper())