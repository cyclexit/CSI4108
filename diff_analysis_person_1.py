import random

# constants
NUM_OF_BITS = 16
MAX_VALUE = 1 << NUM_OF_BITS - 1
PLAINTEXT_NUM = 10000
FULL_ENCRYPTION_ROUNDS = 4 # NOTE: round 5 is simply key mixing

# variables
round_keys = [55382, 42954, 53122, 38368, 40273]

s_box = {
    0x0: 0xb,
    0x1: 0x7,
    0x2: 0x5,
    0x3: 0xf,
    0x4: 0x8,
    0x5: 0x9,
    0x6: 0x1,
    0x7: 0xe,
    0x8: 0x4,
    0x9: 0xa,
    0xa: 0x6,
    0xb: 0xd,
    0xc: 0x2,
    0xd: 0xc,
    0xe: 0x0,
    0xf: 0x3,
}

def permutation(bit_str_16: str) -> str:
    assert(len(bit_str_16) == NUM_OF_BITS)
    res = list(bit_str_16)
    for i in range(0, NUM_OF_BITS):
        # print(4 * (i % 4) + (i // 4)) # debug
        res[4 * (i % 4) + (i // 4)] = bit_str_16[i]
    # print(bit_str_16) # debug
    # print(''.join(res)) # debug
    return ''.join(res)

def encrypt_one_round(to_encrypt: int, k: int) -> str:
    # key mixing
    # print(to_encrypt, k) # debug
    to_encrypt ^= k
    # print(to_encrypt) # debug

    # 4-bit s-box
    PART_NUM_OF_BITS = 4
    NUM_OF_PARTS = NUM_OF_BITS / PART_NUM_OF_BITS
    parts = [] # index 0: least significant
    while to_encrypt > 0:
        parts.append(to_encrypt % (1 << PART_NUM_OF_BITS))
        to_encrypt //= 16
    while len(parts) < 4:
        parts.append(0)
    assert(len(parts) == NUM_OF_PARTS)
    parts.reverse()
    # print("before s-box:", parts) # debug
    for i in range(0, len(parts)):
        parts[i] = s_box[parts[i]]
    # print("after s-box:", parts) # debug
    bit_str_16 = ''.join(f"{x:0{PART_NUM_OF_BITS}b}" for x in parts)
    # print(bit_str_16) # debug
    
    # permutation
    res = permutation(bit_str_16)
    # print(res) # debug
    return res

def full_encrypt(plaintext: int) -> int:
    # print(plaintext, f"{plaintext:0{NUM_OF_BITS}b}") # debug
    tmp = plaintext
    for i in range(0, FULL_ENCRYPTION_ROUNDS):
        tmp = int(encrypt_one_round(tmp, round_keys[i]), 2)
        # print(f"Round {i + 1}:") # debug
        # print(tmp, f"{tmp:0{NUM_OF_BITS}b}") # debug
    # last round: simple key mixing
    tmp ^= round_keys[FULL_ENCRYPTION_ROUNDS]
    # print(tmp, f"{tmp:0{NUM_OF_BITS}b}") # debug
    return tmp

if __name__ == "__main__":
    full_encrypt(798)
