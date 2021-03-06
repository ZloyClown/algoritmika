import random
f = open('BD/bd1.txt', 'w')
f.write('sasat')
f.close()
for i in range(20):
    f = open(f"{i}", 'w')
    f.write(f"{random.randint(1, 1000)}")
    f.close()