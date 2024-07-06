# README

## number mashing

Mash your keyboard numpad in a specific order and a flag might just pop out! \
Points: 184 \
Author: Joseph \
Category: Reverse Engineering

### Solve

The input: 2147483648 -1 \
2^31 divided by -1 is returning the first input itself bcuz it causing integer overflow in 32-bit based systems.

**Flag**: `DUCTF{w0w_y0u_just_br0ke_math!!}`
