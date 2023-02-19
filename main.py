# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        base1 = i+1
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(base1)
            opening_brackets_stack.append(next)

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                if not are_matching(opening_brackets_stack[-1], next):
                    return base1
                else:
                    opening_brackets_stack.pop()
                    opening_brackets_stack.pop()
            else:
                return base1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0]

    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
