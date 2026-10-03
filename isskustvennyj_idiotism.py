# q-learning
import random as r
VVERX=0
VLEVO = 1
VNIZ = 2
VPRAVO = 3
SPISOK = [VVERX, VLEVO, VNIZ, VPRAVO]
SLOVAR = {
    VVERX: "VVERX",
    VLEVO: "VLEVO",
    VNIZ: "VNIZ",
    VPRAVO: "VPRAVO"
}
PRIGODITSA = {
    VVERX: [-1,0],
    VLEVO: [0,-1],
    VNIZ: [1,0],
    VPRAVO: [0,1]
}

q_table = {}

for i in range(-1, 9):
    for j in range(-1, 21):
        q_table[(i,j)] = [0,0,0,0,]

# q_table[(0,0)][0] = -1000000000000000000000000000000000000000000
# q_table[(0,0)][3] = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
ALPHA = 0.9
GAMMA = 0.1

def main():
    step = 0
    ochki = 0
    ppp, ppp_shirina, ppp_vysota = funktsiya("file")
    y = poisk_tipa(ppp, "2")
    yy = poisk_tipa(ppp, "3")
    print(y, yy)
    sostoyanie = {"koordinaty": list(y), "path": []}
    while True:
        onstanty = konstanty(idiot_two(tuple(sostoyanie["koordinaty"]), ppp_shirina, ppp_vysota, ppp), sostoyanie, ppp_shirina, ppp_vysota, ppp)
        sostoyanie["path"].append(list(sostoyanie["koordinaty"]))
        # print(sostoyanie["koordinaty"])
        step+=1
        sostoyanie = onstanty[0]
        # print(sostoyanie["koordinaty"])
        # print(onstanty[2])
        ochki+=onstanty[2]
        # breakpoint()
        if onstanty[1]:
            print("Yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            print("Shagov:", step)
            print("Nagrada tip:", ochki)
            print(risovniye(ppp))
            uuu = otdelnaya_funktsiya(sostoyanie["path"])
            vvv = uuu
            step = 0
            sostoyanie = {"koordinaty": list(y), "path": []}
            ochki = 0
            uuu = aaaaaaaaaaaaaaaaaaaa(uuu)
            print(uuu)
            # while True:
            #     onstanty = konstanty(uuu[step], sostoyanie, ppp_shirina, ppp_vysota, ppp)
            #     step+=1
            #     sostoyanie = onstanty[0]
            #     print(sostoyanie["koordinaty"])
            #     print(onstanty[2])
            #     ochki+=onstanty[2]
            #     if onstanty[1]:
            #         print("Yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            #         print("Shagov:", step)
            #         print("Nagrada tip:", ochki)
            #         print(risovniye(ppp))
            #         print(gaholahola(vvv, risovniye(ppp)))
            #         break
            print(gaholahola(vvv, risovniye(ppp)))
            # print(q_table)
            break
        

def funktsiya(file):
    with open(file, "r") as asas:
        asass = asas.read()
        ppp = asass.split("\n")
        ppp = [list(i) for i in ppp]

    ppp_shirina = len(ppp[0])
    ppp_vysota = len(ppp)

    return ppp, ppp_shirina, ppp_vysota

def poisk_tipa(ppp, startilistop):
    for j, stroka in enumerate(ppp):
        for l, stolbec in enumerate(stroka):
            if ppp[j][l] == startilistop:
                return j, l
    raise Exception("Exception")

def konstanty(deystviya, sostoyanie, ppp_shirina, ppp_vysota, ppp):
    ochki = -1
    if deystviya == VVERX:
        if figna((sostoyanie["koordinaty"][0]-1, sostoyanie["koordinaty"][1]), ppp_shirina, ppp_vysota, ppp):
            sostoyanie["koordinaty"][0]-=1
        else:
            ochki = -10
    if deystviya == VNIZ:
        if figna((sostoyanie["koordinaty"][0]+1, sostoyanie["koordinaty"][1]), ppp_shirina, ppp_vysota, ppp):
            sostoyanie["koordinaty"][0]+=1
        else:
            ochki = -10
    if deystviya == VLEVO:
        if figna((sostoyanie["koordinaty"][0], sostoyanie["koordinaty"][1]-1), ppp_shirina, ppp_vysota, ppp):
            sostoyanie["koordinaty"][1]-=1
        else:
            ochki = -10
    if deystviya == VPRAVO:
        if figna((sostoyanie["koordinaty"][0], sostoyanie["koordinaty"][1]+1), ppp_shirina, ppp_vysota, ppp):
            sostoyanie["koordinaty"][1]+=1
        else:
            ochki = -10

    if ppp[sostoyanie["koordinaty"][0]][sostoyanie["koordinaty"][1]] == "3":
        ttt = True
    else:
        ttt = False

    if ttt:
        ochki = 100

    return sostoyanie, ttt, ochki

def figna(koordinaty, ppp_shirina, ppp_vysota, ppp):
    if 0<=koordinaty[0]<ppp_vysota and 0<=koordinaty[1]<ppp_shirina:
        if ppp[koordinaty[0]][koordinaty[1]] != "1":
            return True
    return False

def risovniye(ppp):
    risovalka = ""
    for j, i in enumerate(ppp):
        for l, k in enumerate(i):
            if ppp[j][l] == "0":
                risovalka+=" "
            elif ppp[j][l] == "1":
                risovalka+="#"
            elif ppp[j][l] == "2":
                risovalka+="@"
            elif ppp[j][l] == "3":
                risovalka+="X"
        risovalka+="\n"

    return risovalka

def otdelnaya_funktsiya(path):
    # print(path)
    new_new_path = []
    for j, i in enumerate(path):  
            if i not in new_new_path:
                new_new_path.append(list(i))
            else:
                jj = new_new_path.index(i)
                del new_new_path[jj+1:]

    return new_new_path

def aaaaaaaaaaaaaaaaaaaa(spisok):
    k = []
    for j, i in enumerate(spisok):
        if j != 0:
            k.append({(-1,0):VVERX,(1,0):VNIZ,(0,-1):VLEVO,(0,1):VPRAVO}[(i[0]-spisok[j-1][0],i[1]-spisok[j-1][1])])

    return k

def gaholahola(vvv, izobrazhenie):
    izobrazhenie = izobrazhenie.split("\n")
    izobrazhenie = [list(j) for j in izobrazhenie]
    for i in vvv:
        izobrazhenie[i[0]][i[1]] = "1"

    izobrazhenie = ["".join(y) for y in izobrazhenie]
    izobrazhenie = "\n".join(izobrazhenie)

    return izobrazhenie

def idiot_two(state, ppp_shirina, ppp_vysota, ppp):
    shag = maxiumim(q_table[state])
    izmenit(state, shag, ppp_shirina, ppp_vysota, ppp)
    return shag

def maxiumim(spisok):
    maximiumim = max(spisok)

    indexes = []
    for j, i in enumerate(spisok):
        if i == maximiumim:
            indexes.append(j)


    return r.choice(indexes)

def izmenit(state, action, ppp_shirina, ppp_vysota, ppp):
    global q_table

    old_state = state

    new_state = (old_state[0]+PRIGODITSA[action][0], old_state[1]+PRIGODITSA[action][1])

    old_q = q_table[old_state][action]

    reward = konstanty(action, {"koordinaty": list(state), "path": [], "tvoyuzhdiviziyu": ""}, ppp_shirina, ppp_vysota, ppp)[2]

    best_future_q = max(q_table[new_state])

    new_q = old_q + ALPHA * (
    reward
    + GAMMA * best_future_q
    - old_q
)
    q_table[state][action] = new_q

for i in range(10):
    main()