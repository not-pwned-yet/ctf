# README

## Avengers Assemble

### Solve

Converted the assembly into C pseudocode so it's easy to read.
```c
int32_t main (void) {
    int32_t var_14h;
    int32_t var_ch;
    int32_t var_4h;
    printf ("Input 1st number:");
    scanf (loc.fmt, var_4h);
    printf ("Input 2nd number:");
    scanf (loc.fmt, var_ch);
    printf ("Input 3rd number:");
    scanf (loc.fmt, var_14h);
    ebx = var_ch;
    ebx += var_4h;
    if (ebx == 0xdeadbeef) {
        if (var_4h <= 0x6f56df65) {
            if (var_ch > 0x6f56df8d) {
                goto label_0;
            }
            if (var_ch < 0x6f56df8d) {
                goto label_0;
            }
            ecx = var_14h;
            ebx = var_ch;
            ecx ^= ebx;
            if (ecx != 0x7d6289f5) {
                goto label_0;
            }
        }
    } else {
label_0:
        printf ("Not Correct\n");
        return eax;
    }
    printf ("Correct\n");
    return eax;
}
```
2nd input is added with the 1st input and then the checking begins.
The result of the addition must be equal to oxdeadbeef which is  3735928559 in decimal. Then, the 1st input must be equal or less than 1867964261. 3rd input can't be more than 1867964301 or  less than 1867964301 (it must be 1867964301).

The program operates XOR on 3rd input with 2nd input. The result of this operation must be equal  2103609845.

```python
# solve.py
def find_solution():
    second = 0x6f56df8d
    first = 0xdeadbeef - second
    third = second ^ 2103609845

    assert first + second == 0xdeadbeef, "Sum condition failed"
    assert first <= 0x6f56df65, "First number upper bound failed"
    assert second == 0x6f56df8d, "Second number condition failed"
    assert second ^ third == 2103609845, "XOR condition failed"

    return first, second, third

solution = find_solution()
print("The correct inputs are:")
print(f"1st number: {solution[0]}")
print(f"2nd number: {solution[1]}")
print(f"3rd number: {solution[2]}")
```

The correct inputs are:
1st number: 1867964258
2nd number: 1867964301
3rd number: 305419896

Verifying:
![](https://i.imgur.com/mX4QfqA.png)

**Flag**: `OSCTF{1867964258_1867964301_305419896}`
