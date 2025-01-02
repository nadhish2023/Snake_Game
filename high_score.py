def read_highscore():
    try:
        file=open("highscore.txt","r")
        hs=int(file.read())
        file.close()
        return hs
    except:
        file = open("highscore.txt", "w")
        file.write('0')
        file.close()
        return 0

def write_high_score(newscore):
    file = open("highscore.txt", "w")
    file.write(str(newscore))
    file.close()
