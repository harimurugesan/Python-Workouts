def play(songs, k, q):
    initial = k
    i = 0
    if q == songs[initial]:
        print(0)
    else:
        songloc = songs.index(q)
        if songloc > initial:
            num1 = songloc - initial
        else:
            i += 1
            num1 = initial - songloc
        songlist2 = songs[:: -1]
        songloc2 = songlist2.index(q)
        if initial == 0 and songloc2 == 0:
            print(1)
        else:
            if i == 0:
                m2 = songloc2 + 1
                num2 = m2 + initial
                print(min(num1,num2))
            else:
                m2 = songloc2 + 1
                num2 = initial - m2
                print(min(num1,num2))
play(['a','b','c', 'd', 'c'], 0, 'c')
