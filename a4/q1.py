import hashlib, hmac

OUTPUT_BIT_LEN = 512
OUTPUT_BYTE_LEN = OUTPUT_BIT_LEN // 8

def byte_xor(a: bytes, b: bytes) -> bytes:
    return (int.from_bytes(a, 'little') ^ int.from_bytes(b, 'little')).to_bytes(max(len(a), len(b)), 'little')

def my_hmac(key: bytes, msg: bytes):
    IPAD = 0x36
    OPAD = 0x5c
    block_size = OUTPUT_BYTE_LEN * (len(msg) // OUTPUT_BYTE_LEN)
    if len(msg) % OUTPUT_BYTE_LEN > 0:
        block_size += OUTPUT_BYTE_LEN
    full_ipad = 0
    full_opad = 0
    for _ in range(0, block_size):
        full_ipad = (full_ipad << 8) + IPAD
        full_opad = (full_opad << 8) + OPAD
    full_ipad = full_ipad.to_bytes(block_size, "little")
    full_opad = full_opad.to_bytes(block_size, "little")
    if len(key) < block_size:
        key = key + b'\x00' * (block_size - len(key))
    inner = hashlib.sha512(byte_xor(key, full_ipad) + msg)
    outer = hashlib.sha512(byte_xor(key, full_opad) + inner.digest())
    return outer

def main():
    message = b"I am using this input string to test my own implementation of HMAC-SHA-512."
    key = b"This is my simple key."
    my_res =  my_hmac(key, message)
    print(my_res.block_size, my_res.digest())
    truth = hmac.HMAC(key, message, digestmod=hashlib.sha512)
    print(truth.block_size, truth.digest())

if __name__ == "__main__":
    main()