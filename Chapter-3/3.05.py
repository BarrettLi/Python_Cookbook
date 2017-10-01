# Problem: You have a byte string and you need to unpack it into an integer value. 
# Alternately, you need to convert a large integer back into a byte string

# suppose your program needs to workd with a 16-element byte string that holds a
# 128-bit integer value
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# to interpret the bytes as an integer, use int.from_bytes(), and specify the byte
# ordering
len(data) # 16
int.from_bytes(data, 'little') # 69120565665751139577663547927094891008
int.from_bytes(data, 'big') # 94522842520747284487117727783387188

# to convert a large integer value back into a byte string, use the int.to_bytes()
# method, specifying the number of bytes and the byte order
x = 94522842520747284487117727783387188
x.to_bytes(16, 'big') # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
x.to_bytes(16, 'little') # b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# discussion
data # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct
hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo # 94522842520747284487117727783387188

# the specification of the byte order just indicates whether the bytes that
# make up the integer value are listed from the least to most significant or the 
# other way around.
x = 0x01020304
x.to_bytes(4, 'big') # b'\x01\x02\x03\x04'
x.to_bytes(4, 'little') # b'\x04\x03\x02\x01'

# if you try to pack an integer into a byte string, but it won't fit, you'll get an error.
# You can use the int.bit_length() method to determine how many bits are required to
# store a value if needed.
x = 523 ** 23 # 335381300113661875107536852714019056160355655333978849017944067
x.to_bytes(16, 'little') # OverflowError: int too big to convert
x.bit_length() # 208
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1

x.to_bytes(nbytes, 'little')
