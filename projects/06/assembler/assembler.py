import sys

from parser import parse


def main():
    binary_code = []

    with open(sys.argv[1], 'r') as source_file:
        line_number = 0
        for mnemonic in source_file:
            if mnemonic.startswith("//") or mnemonic.strip() == "":
                continue

            mnemonic = mnemonic.replace("\n", "")
            binary_code.append(parse(mnemonic))
            line_number += 1

    with open(sys.argv[2], 'w') as target_file:
        target_file.writelines("\n".join(binary_code))


if __name__ == "__main__":
    main()
