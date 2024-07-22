def forward_mangle(input_str):
    result = bytearray(input_str.encode())
    counter1 = counter2 = 0
    key1 = b"RdqQTv\x01\x03\x04\x02\x06\x05"
    
    for i in range(len(result)):
        f = result[i]
        e = key1[counter1] ^ f
        d = (f >> 6) | (f << 2) & 0xFF
        c = ((f << (8 + key1[counter2 + 6] * -1)) & 0xFF) | (f >> (key1[counter2 + 6] & 0x1F))
        b = key1[counter1] ^ ((f >> 2) | (f << 6) & 0xFF)
        a = i & 1
        lower = 1 if 0x61 <= f <= 0x7a else 0
        
        result[i] = (a * (d * (lower ^ 1) + lower * e) + 
                     (a ^ 1) * (b * (lower ^ 1) + lower * c)) & 0xFF
        
        counter1 = (counter1 + a) % 6
        counter2 = (counter2 + a) % 6
    
    return result

def reverse_mangle(target):
    flag = ['_'] * len(target)
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789_{}'
    
    for i in range(len(target)):
        for c in charset:
            test_flag = flag.copy()
            test_flag[i] = c
            result = forward_mangle(''.join(test_flag))
            if result[i] == target[i]:
                flag[i] = c
                break
    
    return ''.join(flag)

# Corrected target handling
target_str = "b4,31,8e,02,af,1c,5d,23,98,7d,a3,1e,b0,3c,b3,c4,a6,06,58,28,19,7d,a3,c0,85,31,68,0a,bc,03,5d,3d,0b"
target = bytes([int(x, 16) for x in target_str.split(',')])

flag = reverse_mangle(target)
print(flag)
