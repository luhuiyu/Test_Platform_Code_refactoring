
with open('1.txt', 'r',encoding='UTF-8') as f:
    for line in f.readlines():
        if '[kas]' in line:
            pass
        else:
            with open('2.txt', 'a', encoding='UTF-8') as c:
                c.writelines(line)




