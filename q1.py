'''
    This script is used to simulate the rotor machine described in the a2 q1.
'''

cnt = 20

# initial state
fast_in = [((i - 4) % 26) for i in range(0, 26)]
fast_out = [13, 21, 3, 15, 1, 19, 10, 14, 26, 20, 8, 16, 7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24]
fast_out = [i - 1 for i in fast_out]

print("fast:")
print(fast_in)
print(fast_out)

medium_in = [((i - 1) % 26) for i in range(0, 26)]
medium_out = [20, 1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2, 22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17]
medium_out = [i - 1 for i in medium_out]
print("medium:")
print(medium_in)
print(medium_out)

slow_in = [i for i in range(0, 26)]
slow_out = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4, 23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 14]
slow_out = [i - 1 for i in slow_out]
print("slow:")
print(slow_in)
print(slow_out)

def rotate(rotor_in: list, rotor_out: list):
    rotor_in = [rotor_in[-1]] + rotor_in[0:-1]
    rotor_out = [rotor_out[-1]] + rotor_out[0:-1]
    return rotor_in, rotor_out

def char_to_int(ch: str):
    return ord(ch) - ord('A')

def int_to_char(idx: int):
    return chr(idx + ord('A'))

if __name__ == "__main__":
    plaintext = "HELLOWORLD"
    for i in range(0, len(plaintext)):
        # get the ciphertext
        fast_out_idx = fast_out.index(fast_in[char_to_int(plaintext[i])])
        medium_out_idx = medium_out.index(medium_in[fast_out_idx])
        slow_out_idx = slow_out.index(slow_in[medium_out_idx])
        print(plaintext[i], int_to_char(slow_out_idx))

        # update states
        fast_in, fast_out = rotate(fast_in, fast_out)
        assert(len(fast_in) == 26)
        assert(len(fast_out) == 26)
        cnt += 1
        if cnt % 26 == 0:
            print(f"After plaintext[{i}] = {plaintext[i]}, rotate the medium rotor")
            medium_in, medium_out = rotate(medium_in, medium_out)
        if cnt % (26 * 26) == 0:
            print(f"After plaintext[{i}] = {plaintext[i]}, rotate the slow rotor")
            slow_in, slow_out = rotate(slow_in, slow_out)
