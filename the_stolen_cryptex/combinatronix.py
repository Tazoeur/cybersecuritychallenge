tab = [
    'ad e0',
    '78 81',
    'a1 f3',
    '3e bb',
    '47 04',
]

for byte in tab:
    for byte2 in tab:
        if byte2 != byte:
            for byte3 in tab:
                if byte3 != byte2 and byte3 != byte:
                    for byte4 in tab:
                        if byte4 != byte3 and byte4 != byte2 and byte4 != byte:
                            print('{} {} {} {} {}'.format("48 40 6C 46 20 4B 33 79", byte, byte2, byte3, byte4))
