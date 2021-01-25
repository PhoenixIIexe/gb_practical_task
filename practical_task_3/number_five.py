def suma(st):
    suma = int(0)
    for i in st:
        suma += int(i)
    print(suma, type(suma))
    return suma


# $ - Специальный символ!!!

stop = bool(True)
s = int(0)

while stop:
    st = str(input())
    st_list = st.split()

    if st_list.count('$') == 1:
        st_list.remove('$')
        s += suma(st_list)
        stop = False
    else:
        s += suma(st_list)

print(s)
