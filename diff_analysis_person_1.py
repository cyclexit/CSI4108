# constants
NUM_OF_BITS = 16
MAX_VALUE = 1 << NUM_OF_BITS - 1
PLAINTEXT_NUM = 10000

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

def permutation(bit_str_16: str):
    assert(len(bit_str_16) == NUM_OF_BITS)
    res = list(bit_str_16)
    for i in range(0, NUM_OF_BITS):
        # print(4 * (i % 4) + (i // 4)) # debug
        res[4 * (i % 4) + (i // 4)] = bit_str_16[i]
    # print(bit_str_16) # debug
    # print(''.join(res)) # debug
    return ''.join(res)

if __name__ == "__main__":
    num_bits = 16
    num = 55382
    permutation(f"{num:0{num_bits}b}")
    pass
