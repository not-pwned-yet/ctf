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

