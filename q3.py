p = 1013
q = 1021
M = p * q
seed = 798
random_seq = [seed]

def to_bit_str(val: int, num_of_bits: int):
    return f"{val:0{num_of_bits}b}"

print(f"p={to_bit_str(p, 10)}")
print(f"q={to_bit_str(q, 10)}")
print(f"M={to_bit_str(M, 10)}")

for i in range(0, 15):
    random_seq.append((random_seq[i] ** 2) % M)
    print(f"{i+1}: {random_seq[-1]} = {to_bit_str(random_seq[-1], 20)}")

print(random_seq)
