def binary_coded_decimal(number: int) -> str:
    """
    Find binary coded decimal (bcd) of integer base 10.
    Each digit of the number is represented by a 4-bit binary.
    Example:
    >>> binary_coded_decimal(-2)
    '0b0000'
    >>> binary_coded_decimal(-1)
    '0b0000'
    >>> binary_coded_decimal(0)
    '0b0000'
    >>> binary_coded_decimal(3)
    '0b0011'
    >>> binary_coded_decimal(2)
    '0b0010'
    >>> binary_coded_decimal(12)
    '0b00010010'
    >>> binary_coded_decimal(987)
    '0b100110000111'
    """
    return "0b" + "".join(
        str(bin(int(digit)))[2:].zfill(4) for digit in str(max(0, number))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    def binary_coded_decimal(number: int) -> str:
    """
    Find binary coded decimal (bcd) of integer base 10.
    Each digit of the number is represented by a 4-bit binary.
    Example:
    >>> binary_coded_decimal(-2)
    '0b0000'
    >>> binary_coded_decimal(-1)
    '0b0000'
    >>> binary_coded_decimal(0)
    '0b0000'
    >>> binary_coded_decimal(3)
    '0b0011'
    >>> binary_coded_decimal(2)
    '0b0010'
    >>> binary_coded_decimal(12)
    '0b00010010'
    >>> binary_coded_decimal(987)
    '0b100110000111'
    """
    return "0b" + "".join(
        str(bin(int(digit)))[2:].zfill(4) for digit in str(max(0, number))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
def binary_coded_decimal(number: int) -> str:
    """
    Find binary coded decimal (bcd) of integer base 10.
    Each digit of the number is represented by a 4-bit binary.
    Example:
    >>> binary_coded_decimal(-2)
    '0b0000'
    >>> binary_coded_decimal(-1)
    '0b0000'
    >>> binary_coded_decimal(0)
    '0b0000'
    >>> binary_coded_decimal(3)
    '0b0011'
    >>> binary_coded_decimal(2)
    '0b0010'
    >>> binary_coded_decimal(12)
    '0b00010010'
    >>> binary_coded_decimal(987)
    '0b100110000111'
    """
    return "0b" + "".join(
        str(bin(int(digit)))[2:].zfill(4) for digit in str(max(0, number))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()



def binary_count_setbits(a: int) -> int:
    """
    Take in 1 integer, return a number that is
    the number of 1's in binary representation of that number.

    >>> binary_count_setbits(25)
    3
    >>> binary_count_setbits(36)
    2
    >>> binary_count_setbits(16)
    1
    >>> binary_count_setbits(58)
    4
    >>> binary_count_setbits(4294967295)
    32
    >>> binary_count_setbits(0)
    0
    >>> binary_count_setbits(-10)
    Traceback (most recent call last):
        ...
    ValueError: Input value must be a positive integer
    >>> binary_count_setbits(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    >>> binary_count_setbits("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0:
        raise ValueError("Input value must be a positive integer")
    elif isinstance(a, float):
        raise TypeError("Input value must be a 'int' type")
    return bin(a).count("1")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_or(a: int, b: int) -> str:
    """
    Take in 2 integers, convert them to binary, and return a binary number that is the
    result of a binary or operation on the integers provided.

    >>> binary_or(25, 32)
    '0b111001'
    >>> binary_or(37, 50)
    '0b110111'
    >>> binary_or(21, 30)
    '0b11111'
    >>> binary_or(58, 73)
    '0b1111011'
    >>> binary_or(0, 255)
    '0b11111111'
    >>> binary_or(0, 256)
    '0b100000000'
    >>> binary_or(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both inputs must be positive
    >>> binary_or(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_or("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both inputs must be positive")
    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    b_binary = str(bin(b))[2:]
    max_len = max(len(a_binary), len(b_binary))
    return "0b" + "".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()




# Information on binary shifts:
# https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
# https://www.interviewcake.com/concept/java/bit-shift


def logical_left_shift(number: int, shift_amount: int) -> str:
    """
    Take in 2 positive integers.
    'number' is the integer to be logically left shifted 'shift_amount' times.
    i.e. (number << shift_amount)
    Return the shifted binary representation.

    >>> logical_left_shift(0, 1)
    '0b00'
    >>> logical_left_shift(1, 1)
    '0b10'
    >>> logical_left_shift(1, 5)
    '0b100000'
    >>> logical_left_shift(17, 2)
    '0b1000100'
    >>> logical_left_shift(1983, 4)
    '0b111101111110000'
    >>> logical_left_shift(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: both inputs must be positive integers
    """
    if number < 0 or shift_amount < 0:
        raise ValueError("both inputs must be positive integers")

    binary_number = str(bin(number))
    binary_number += "0" * shift_amount
    return binary_number


def logical_right_shift(number: int, shift_amount: int) -> str:
    """
    Take in positive 2 integers.
    'number' is the integer to be logically right shifted 'shift_amount' times.
    i.e. (number >>> shift_amount)
    Return the shifted binary representation.

    >>> logical_right_shift(0, 1)
    '0b0'
    >>> logical_right_shift(1, 1)
    '0b0'
    >>> logical_right_shift(1, 5)
    '0b0'
    >>> logical_right_shift(17, 2)
    '0b100'
    >>> logical_right_shift(1983, 4)
    '0b1111011'
    >>> logical_right_shift(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: both inputs must be positive integers
    """
    if number < 0 or shift_amount < 0:
        raise ValueError("both inputs must be positive integers")

    binary_number = str(bin(number))[2:]
    if shift_amount >= len(binary_number):
        return "0b0"
    shifted_binary_number = binary_number[: len(binary_number) - shift_amount]
    return "0b" + shifted_binary_number


def arithmetic_right_shift(number: int, shift_amount: int) -> str:
    """
    Take in 2 integers.
    'number' is the integer to be arithmetically right shifted 'shift_amount' times.
    i.e. (number >> shift_amount)
    Return the shifted binary representation.

    >>> arithmetic_right_shift(0, 1)
    '0b00'
    >>> arithmetic_right_shift(1, 1)
    '0b00'
    >>> arithmetic_right_shift(-1, 1)
    '0b11'
    >>> arithmetic_right_shift(17, 2)
    '0b000100'
    >>> arithmetic_right_shift(-17, 2)
    '0b111011'
    >>> arithmetic_right_shift(-1983, 4)
    '0b111110000100'
    """
    if number >= 0:  # Get binary representation of positive number
        binary_number = "0" + str(bin(number)).strip("-")[2:]
    else:  # Get binary (2's complement) representation of negative number
        binary_number_length = len(bin(number)[3:])  # Find 2's complement of number
        binary_number = bin(abs(number) - (1 << binary_number_length))[3:]
        binary_number = (
            "1" + "0" * (binary_number_length - len(binary_number)) + binary_number
        )

    if shift_amount >= len(binary_number):
        return "0b" + binary_number[0] * len(binary_number)
    return (
        "0b"
        + binary_number[0] * shift_amount
        + binary_number[: len(binary_number) - shift_amount]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()



from timeit import timeit


def get_set_bits_count_using_brian_kernighans_algorithm(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count_using_brian_kernighans_algorithm(25)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(37)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(21)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(58)
    4
    >>> get_set_bits_count_using_brian_kernighans_algorithm(0)
    0
    >>> get_set_bits_count_using_brian_kernighans_algorithm(256)
    1
    >>> get_set_bits_count_using_brian_kernighans_algorithm(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must not be negative
    """
    if number < 0:
        raise ValueError("the value of input must not be negative")
    result = 0
    while number:
        number &= number - 1
        result += 1
    return result


def get_set_bits_count_using_modulo_operator(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count_using_modulo_operator(25)
    3
    >>> get_set_bits_count_using_modulo_operator(37)
    3
    >>> get_set_bits_count_using_modulo_operator(21)
    3
    >>> get_set_bits_count_using_modulo_operator(58)
    4
    >>> get_set_bits_count_using_modulo_operator(0)
    0
    >>> get_set_bits_count_using_modulo_operator(256)
    1
    >>> get_set_bits_count_using_modulo_operator(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must not be negative
    """
    if number < 0:
        raise ValueError("the value of input must not be negative")
    result = 0
    while number:
        if number % 2 == 1:
            result += 1
        number >>= 1
    return result


def benchmark() -> None:
    """
    Benchmark code for comparing 2 functions, with different length int values.
    Brian Kernighan's algorithm is consistently faster than using modulo_operator.
    """

    def do_benchmark(number: int) -> None:
        setup = "import __main__ as z"
        print(f"Benchmark when {number = }:")
        print(f"{get_set_bits_count_using_modulo_operator(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_modulo_operator({number})", setup=setup
        )
        print(f"timeit() runs in {timing} seconds")
        print(f"{get_set_bits_count_using_brian_kernighans_algorithm(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_brian_kernighans_algorithm({number})",
            setup=setup,
        )
        print(f"timeit() runs in {timing} seconds")

    for number in (25, 37, 58, 0):
        do_benchmark(number)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()



def gray_code(bit_count: int) -> list:
    """
    Takes in an integer n and returns a n-bit
    gray code sequence
    An n-bit gray code sequence is a sequence of 2^n
    integers where:

    a) Every integer is between [0,2^n -1] inclusive
    b) The sequence begins with 0
    c) An integer appears at most one times in the sequence
    d)The binary representation of every pair of integers differ
       by exactly one bit
    e) The binary representation of first and last bit also
       differ by exactly one bit

    >>> gray_code(2)
    [0, 1, 3, 2]

    >>> gray_code(1)
    [0, 1]

    >>> gray_code(3)
    [0, 1, 3, 2, 6, 7, 5, 4]

    >>> gray_code(-1)
    Traceback (most recent call last):
        ...
    ValueError: The given input must be positive

    >>> gray_code(10.6)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for <<: 'int' and 'float'
    """

    # bit count represents no. of bits in the gray code
    if bit_count < 0:
        raise ValueError("The given input must be positive")

    # get the generated string sequence
    sequence = gray_code_sequence_string(bit_count)
    #
    # convert them to integers
    for i in range(len(sequence)):
        sequence[i] = int(sequence[i], 2)

    return sequence


def gray_code_sequence_string(bit_count: int) -> list:
    """
    Will output the n-bit grey sequence as a
    string of bits

    >>> gray_code_sequence_string(2)
    ['00', '01', '11', '10']

    >>> gray_code_sequence_string(1)
    ['0', '1']
    """

    # The approach is a recursive one
    # Base case achieved when either n = 0 or n=1
    if bit_count == 0:
        return ["0"]

    if bit_count == 1:
        return ["0", "1"]

    seq_len = 1 << bit_count  # defines the length of the sequence
    # 1<< n is equivalent to 2^n

    # recursive answer will generate answer for n-1 bits
    smaller_sequence = gray_code_sequence_string(bit_count - 1)

    sequence = []

    # append 0 to first half of the smaller sequence generated
    for i in range(seq_len // 2):
        generated_no = "0" + smaller_sequence[i]
        sequence.append(generated_no)

    # append 1 to second half ... start from the end of the list
    for i in reversed(range(seq_len // 2)):
        generated_no = "1" + smaller_sequence[i]
        sequence.append(generated_no)

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()




"""
Author  : Alexander Pantyukhin
Date    : November 1, 2022

Task:
Given a positive int number. Return True if this number is power of 2
or False otherwise.

Implementation notes: Use bit manipulation.
For example if the number is the power of two it's bits representation:
n     = 0..100..00
n - 1 = 0..011..11

n & (n - 1) - no intersections = 0
"""


def is_power_of_two(number: int) -> bool:
    """
    Return True if this number is power of 2 or False otherwise.

    >>> is_power_of_two(0)
    True
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(4)
    True
    >>> is_power_of_two(6)
    False
    >>> is_power_of_two(8)
    True
    >>> is_power_of_two(17)
    False
    >>> is_power_of_two(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must not be negative
    >>> is_power_of_two(1.2)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for &: 'float' and 'float'

    # Test all powers of 2 from 0 to 10,000
    >>> all(is_power_of_two(int(2 ** i)) for i in range(10000))
    True
    """
    if number < 0:
        raise ValueError("number must not be negative")
    return number & (number - 1) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()





"""
Author  : Naman Sharma
Date    : October 2, 2023

Task:
To Find the largest power of 2 less than or equal to a given number.

Implementation notes: Use bit manipulation.
We start from 1 & left shift the set bit to check if (res<<1)<=number.
Each left bit shift represents a pow of 2.

For example:
number: 15
res:    1   0b1
        2   0b10
        4   0b100
        8   0b1000
        16  0b10000 (Exit)
"""


def largest_pow_of_two_le_num(number: int) -> int:
    """
    Return the largest power of two less than or equal to a number.

    >>> largest_pow_of_two_le_num(0)
    0
    >>> largest_pow_of_two_le_num(1)
    1
    >>> largest_pow_of_two_le_num(-1)
    0
    >>> largest_pow_of_two_le_num(3)
    2
    >>> largest_pow_of_two_le_num(15)
    8
    >>> largest_pow_of_two_le_num(99)
    64
    >>> largest_pow_of_two_le_num(178)
    128
    >>> largest_pow_of_two_le_num(999999)
    524288
    >>> largest_pow_of_two_le_num(99.9)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    """
    if isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    if number <= 0:
        return 0
    res = 1
    while (res << 1) <= number:
        res <<= 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def show_bits(before: int, after: int) -> str:
    """
    >>> print(show_bits(0, 0xFFFF))
        0: 00000000
    65535: 1111111111111111
    """
    return f"{before:>5}: {before:08b}\n{after:>5}: {after:08b}"


def swap_odd_even_bits(num: int) -> int:
    """
    1. We use bitwise AND operations to separate the even bits (0, 2, 4, 6, etc.) and
       odd bits (1, 3, 5, 7, etc.) in the input number.
    2. We then right-shift the even bits by 1 position and left-shift the odd bits by
       1 position to swap them.
    3. Finally, we combine the swapped even and odd bits using a bitwise OR operation
       to obtain the final result.
    >>> print(show_bits(0, swap_odd_even_bits(0)))
        0: 00000000
        0: 00000000
    >>> print(show_bits(1, swap_odd_even_bits(1)))
        1: 00000001
        2: 00000010
    >>> print(show_bits(2, swap_odd_even_bits(2)))
        2: 00000010
        1: 00000001
    >>> print(show_bits(3, swap_odd_even_bits(3)))
        3: 00000011
        3: 00000011
    >>> print(show_bits(4, swap_odd_even_bits(4)))
        4: 00000100
        8: 00001000
    >>> print(show_bits(5, swap_odd_even_bits(5)))
        5: 00000101
       10: 00001010
    >>> print(show_bits(6, swap_odd_even_bits(6)))
        6: 00000110
        9: 00001001
    >>> print(show_bits(23, swap_odd_even_bits(23)))
       23: 00010111
       43: 00101011
    """
    # Get all even bits - 0xAAAAAAAA is a 32-bit number with all even bits set to 1
    even_bits = num & 0xAAAAAAAA

    # Get all odd bits - 0x55555555 is a 32-bit number with all odd bits set to 1
    odd_bits = num & 0x55555555

    # Right shift even bits and left shift odd bits and swap them
    return even_bits >> 1 | odd_bits << 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    for i in (-1, 0, 1, 2, 3, 4, 23, 24):
        print(show_bits(i, swap_odd_even_bits(i)), "\n")


#!/usr/bin/env python3

"""Provide the functionality to manipulate a single bit."""


def set_bit(number: int, position: int) -> int:
    """
    Set the bit at position to 1.

    Details: perform bitwise or for given number and X.
    Where X is a number with all the bits - zeroes and bit on given
    position - one.

    >>> set_bit(0b1101, 1) # 0b1111
    15
    >>> set_bit(0b0, 5) # 0b100000
    32
    >>> set_bit(0b1111, 1) # 0b1111
    15
    """
    return number | (1 << position)


def clear_bit(number: int, position: int) -> int:
    """
    Set the bit at position to 0.

    Details: perform bitwise and for given number and X.
    Where X is a number with all the bits - ones and bit on given
    position - zero.

    >>> clear_bit(0b10010, 1) # 0b10000
    16
    >>> clear_bit(0b0, 5) # 0b0
    0
    """
    return number & ~(1 << position)


def flip_bit(number: int, position: int) -> int:
    """
    Flip the bit at position.

    Details: perform bitwise xor for given number and X.
    Where X is a number with all the bits - zeroes and bit on given
    position - one.

    >>> flip_bit(0b101, 1) # 0b111
    7
    >>> flip_bit(0b101, 0) # 0b100
    4
    """
    return number ^ (1 << position)


def is_bit_set(number: int, position: int) -> bool:
    """
    Is the bit at position set?

    Details: Shift the bit at position to be the first (smallest) bit.
    Then check if the first bit is set by anding the shifted number with 1.

    >>> is_bit_set(0b1010, 0)
    False
    >>> is_bit_set(0b1010, 1)
    True
    >>> is_bit_set(0b1010, 2)
    False
    >>> is_bit_set(0b1010, 3)
    True
    >>> is_bit_set(0b0, 17)
    False
    """
    return ((number >> position) & 1) == 1


def get_bit(number: int, position: int) -> int:
    """
    Get the bit at the given position

    Details: perform bitwise and for the given number and X,
    Where X is a number with all the bits - zeroes and bit on given position - one.
    If the result is not equal to 0, then the bit on the given position is 1, else 0.

    >>> get_bit(0b1010, 0)
    0
    >>> get_bit(0b1010, 1)
    1
    >>> get_bit(0b1010, 2)
    0
    >>> get_bit(0b1010, 3)
    1
    """
    return int((number & (1 << position)) != 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()



def get_reverse_bit_string(number: int) -> str:
    """
    return the bit string of an integer

    >>> get_reverse_bit_string(9)
    '10010000000000000000000000000000'
    >>> get_reverse_bit_string(43)
    '11010100000000000000000000000000'
    >>> get_reverse_bit_string(2873)
    '10011100110100000000000000000000'
    >>> get_reverse_bit_string("this is not a number")
    Traceback (most recent call last):
        ...
    TypeError: operation can not be conducted on a object of type str
    """
    if not isinstance(number, int):
        msg = (
            "operation can not be conducted on a object of type "
            f"{type(number).__name__}"
        )
        raise TypeError(msg)
    bit_string = ""
    for _ in range(32):
        bit_string += str(number % 2)
        number = number >> 1
    return bit_string


def reverse_bit(number: int) -> str:
    """
    Take in an 32 bit integer, reverse its bits,
    return a string of reverse bits

    result of a reverse_bit and operation on the integer provided.

    >>> reverse_bit(25)
    '00000000000000000000000000011001'
    >>> reverse_bit(37)
    '00000000000000000000000000100101'
    >>> reverse_bit(21)
    '00000000000000000000000000010101'
    >>> reverse_bit(58)
    '00000000000000000000000000111010'
    >>> reverse_bit(0)
    '00000000000000000000000000000000'
    >>> reverse_bit(256)
    '00000000000000000000000100000000'
    >>> reverse_bit(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive

    >>> reverse_bit(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type

    >>> reverse_bit("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    elif isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    elif isinstance(number, str):
        raise TypeError("'<' not supported between instances of 'str' and 'int'")
    result = 0
    # iterator over [1 to 32],since we are dealing with 32 bit integer
    for _ in range(1, 33):
        # left shift the bits by unity
        result = result << 1
        # get the end bit
        end_bit = number % 2
        # right shift the bits by unity
        number = number >> 1
        # add that bit to our ans
        result = result | end_bit
    return get_reverse_bit_string(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


"""
Author  : Alexander Pantyukhin
Date    : November 1, 2022

Task:
Given a positive int number. Return True if this number is power of 2
or False otherwise.

Implementation notes: Use bit manipulation.
For example if the number is the power of two it's bits representation:
n     = 0..100..00
n - 1 = 0..011..11

n & (n - 1) - no intersections = 0
"""


def is_power_of_two(number: int) -> bool:
    """
    Return True if this number is power of 2 or False otherwise.

    >>> is_power_of_two(0)
    True
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(4)
    True
    >>> is_power_of_two(6)
    False
    >>> is_power_of_two(8)
    True
    >>> is_power_of_two(17)
    False
    >>> is_power_of_two(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must not be negative
    >>> is_power_of_two(1.2)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for &: 'float' and 'float'

    # Test all powers of 2 from 0 to 10,000
    >>> all(is_power_of_two(int(2 ** i)) for i in range(10000))
    True
    """
    if number < 0:
        raise ValueError("number must not be negative")
    return number & (number - 1) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()