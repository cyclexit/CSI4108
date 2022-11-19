import hashlib, hmac

OUTPUT_BIT_LEN = 512
OUTPUT_BYTE_LEN = OUTPUT_BIT_LEN // 8

def my_hmac(key: bytes, msg: bytes):
    IPAD = 0x36
    OPAD = 0x5c
    full_ipad = 0
    full_opad = 0
    for _ in range(0, OUTPUT_BYTE_LEN):
        full_ipad = (full_ipad << 8) + IPAD
        full_opad = (full_opad << 8) + OPAD
    # res = hashlib.sha512((key ^ full_ipad) | msg)
    # print(len(hex(full_ipad)), hex(full_ipad)) # debug
    # print(full_ipad.to_bytes(OUTPUT_BYTE_LEN, "big")) # debug
    # print(len(hex(full_opad)), hex(full_opad)) # debug
    # print(full_opad.to_bytes(OUTPUT_BYTE_LEN, "big")) # debug

def main():
    message = b"I am using this input string to test my own implementation of HMAC-SHA-512."
    key = b"This is my simple key."
    my_hmac(key, message)

if __name__ == "__main__":
    main()