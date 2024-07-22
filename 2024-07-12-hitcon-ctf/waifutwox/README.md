# Waifutwox

Note: submit the flag as flag.replace('Q', '{').replace('Z', '}').lower()

Weebs: 2D waifus are better than 3D girls because they are adorable and not annoying.
The 2D waifus: https://storage.googleapis.com/hitcon-ctf-2024-qual-attachment/waifutwox/waifutwox-f2d7aa662f71515ed0edc5a7b299ce8c0fb80b71.tar.gz
Author: wxrdnx

## Progress

hint: YXZlcmFnZV9mbGFnW2k6aSs0XQ== means average_flag\[i:i+4] (image name) from base64 encoding.
the interactive input the program wants only from 0 to 3 (connected to the hint)

Current plan: identify the function that wraps 0x00008ae (address that calls "Invalid base64" string).
Future plan: try to bruteforcing the image file name into the matching base64 format (assumption).

**Flag**: ``
