p = 1013
q = 1021
M = p * q
seed = 798
random_seq = [seed]

for i in range(0, 15):
    random_seq.append((random_seq[i] ** 2) % M)

print(random_seq)
