#!/usr/bin/env python3

# ----------------------------------------------------------------------
# strToInt3.py
# Jacob Reppeto
# ----------------------------------------------------------------------

from typing import Dict, List, Optional

def strToInt3(s: str) -> Optional[int]:
    """
    Converts a string containing either digits or written-out numbers into an integer.
    There may also be additional characters in the string that are not part of the
    number and they are to be ignored. See the assignment description for more details.
    The function processes each character of the input string and attempts to identify
    either numeric digits or written-out equivalent words for numbers zero to nine.
    If the string contains a combination of numeric digits and words, they will be
    combined in order, and the resulting integer will be returned. If no recognizable
    numeric content is found in the string, the function returns None.

    :param s: The input string that may contain numeric digits or written-out
        words representing numbers.
    :type s: str
    :return: The integer value represented by the numeric content in the string, or
        None if no numeric content is found.
    :rtype: Optional[int]
    """
    numbers: dict[str, int] = { "zero": 0, "one": 1, "two": 2,
                                "three": 3, "four": 4, "five": 5,
                                "six": 6, "seven": 7, "eight": 8,
                                "nine": 9 }

    digits: list[int] = []

    for i in range(len(s)):

        if s[i].isdigit():
            digits.append(int(s[i]))

        else:

            for key, value in numbers.items():

                if s[i] == key[0]:
                    found = True

                    pos = i + 1

                    for ch in key[1:]:

                        nexPos = s.find(ch, pos)

                        if nexPos != -1:
                            pos = nexPos + 1

                        else:
                            found = False
                            break

                    if found:
                        digits.append(value)

    if len(digits) == 0:
        return None
    else:

        total = 0

        for digit in digits:
            total = total * 10 + digit

        return total




def main():
    print(strToInt3("otwone")) # Expected: 121
    print(strToInt3("tw3xo4n5sio8nxe")) # Expected: 231495618

# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()