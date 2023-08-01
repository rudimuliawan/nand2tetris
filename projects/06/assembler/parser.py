from a_instruction import AInstruction
from c_instruction import CInstruction


def is_a_instruction(mnemonic):
    return mnemonic.startswith('@')


def is_c_instruction(mnemonic):
    return not is_a_instruction(mnemonic)


def parse(mnemonic):
    if is_a_instruction(mnemonic):
        mnemonic = mnemonic.replace("@", "")
        if mnemonic.isdigit():
            return AInstruction.to_binary(mnemonic)

        raise Exception("Invalid A instruction")

    elif is_c_instruction(mnemonic):
        return CInstruction.get_binary_syntax(mnemonic)

    else:
        raise Exception(f"Invalid instruction {mnemonic}")
