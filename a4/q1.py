import hashlib, hmac

OUTPUT_BIT_LEN = 512
OUTPUT_BYTE_LEN = OUTPUT_BIT_LEN // 8

def byte_xor(a: bytes, b: bytes) -> bytes:
    return (int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')).to_bytes(max(len(a), len(b)), 'big')

def my_hmac(key: bytes, msg: bytes) -> bytes:
    IPAD = 0x36
    OPAD = 0x5c
    full_ipad = 0
    full_opad = 0
    for _ in range(0, OUTPUT_BYTE_LEN):
        full_ipad = (full_ipad << 8) + IPAD
        full_opad = (full_opad << 8) + OPAD
    full_ipad = full_ipad.to_bytes(OUTPUT_BYTE_LEN, "big")
    full_opad = full_opad.to_bytes(OUTPUT_BYTE_LEN, "big")
    if len(key) < OUTPUT_BYTE_LEN:
        key = b'\x00' * (OUTPUT_BYTE_LEN - len(key)) + key
    inner = hashlib.sha512(byte_xor(key, full_ipad) + msg).digest()
    outer = hashlib.sha512(byte_xor(key, full_opad) + inner).digest()
    return outer

def main():
    message = b"I am using this input string to test my own implementation of HMAC-SHA-512."
    key = b"This is my simple key."
    my_res =  my_hmac(key, message)
    print(len(my_res), my_res)
    truth = hmac.HMAC(key, message, digestmod=hashlib.sha512).digest()
    print(len(truth), truth)

if __name__ == "__main__":
    main()