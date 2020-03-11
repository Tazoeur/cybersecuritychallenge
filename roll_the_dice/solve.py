
reading = [
    "26 52 22 64 61 64 15 11 64 12 32 12 15 55 12",
    "22 61 35 66 46 25 54 14 15 26 51 21 21 12 12"
]

alphabets = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
             ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
              "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

tab = []
for alphabet in alphabets:
    assert(len(alphabet) == 36)
    for i in range(36):
        for line in reading:
            password = ""
            for couple in line.split(" "):
                x = int(int(couple)/10)
                y = int(couple) % 10
                assert(0 < x < 7)
                assert(0 < y < 7)
                password += alphabet[(x*6+y + i) % 36]
            tab.append(password)


for password in tab:
    print(password, end=" ")
