ask = input(" Nhap chu de :").lower()

letters = {}

bangchucai = "abcdefghijklmnopqrstuvwxyz"

for chu in ask:
    if chu in bangchucai:
        if chu not in letters :
            letters[chu] = 1
        else :
            letters[chu] += 1

for chu in sorted(letters):
    print(chu, letters[chu])
