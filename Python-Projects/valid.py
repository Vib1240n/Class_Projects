import re


def funcvalidpairs(inputStr):
    # Write your code here
    valid = []
    regex = (
        '^/('
        '[-+]?'
        '((([1-9]|[1-8]\d)(\.\d+)?)|90(\.0+)?)'
        ', '
        '[-+]?'
        '((([1-9]\d?|1[0-7]\d)(\.\d+)?)|180(\.0+)?)'
        '\)$)'
    )
    ifvalid = re.compile(regex)

    for i in inputStr:
        if ifvalid.match(i):
            valid.index(i)
        else:
            valid = "InValid"

    return valid


def main():
    inputStr = []
    inputStr_size = int(input())
    inputStr = list(map(str, input().split()))

    result = funcvalidpairs(inputStr)
    print(" ".join([str(res) for res in result]))


if __name__ == "__main__":
    main()