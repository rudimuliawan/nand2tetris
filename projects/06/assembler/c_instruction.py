COMPUTING_A_TABLE = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101",
}


COMPUTING_M_TABLE = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "M": "110000",
    "!D": "001101",
    "!M": "110001",
    "-D": "001111",
    "-M": "110011",
    "D+1": "011111",
    "M+1": "110111",
    "D-1": "001110",
    "M-1": "110010",
    "D+M": "000010",
    "D-M": "010011",
    "M-D": "000111",
    "D&M": "000000",
    "D|M": "010101",
}


DESTINATION_TABLE = {
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}


JUMP_TABLE = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}


class CInstruction:

    @classmethod
    def has_jump_instruction(cls, mnemonic):
        return ";" in mnemonic

    @classmethod
    def get_jump_instruction(cls, mnemonic):
        return mnemonic.split(";")[-1]

    @classmethod
    def has_dest_instruction(cls, mnemonic):
        return "=" in mnemonic

    @classmethod
    def get_dest_instruction(cls, mnemonic):
        return mnemonic.split("=")[0]

    @classmethod
    def get_comp_instruction(cls, mnemonic):
        if cls.has_jump_instruction(mnemonic):
            mnemonic = mnemonic[0:mnemonic.find(";")]

        if cls.has_dest_instruction(mnemonic):
            mnemonic = mnemonic[mnemonic.find("=")+1:]

        return mnemonic

    @classmethod
    def get_symbolic(cls, mnemonic):
        symbolic = {
            "dest": None,
            "comp": None,
            "jump": None,
        }

        symbolic["comp"] = cls.get_comp_instruction(mnemonic)

        if cls.has_dest_instruction(mnemonic):
            symbolic["dest"] = cls.get_dest_instruction(mnemonic)

        if cls.has_jump_instruction(mnemonic):
            symbolic["jump"] = cls.get_jump_instruction(mnemonic)

        return symbolic

    @classmethod
    def get_binary_syntax(cls, mnemonic):
        binary_syntax = "111"
        symbolic = cls.get_symbolic(mnemonic)

        if "M" in symbolic["comp"]:
            binary_syntax += "1"
        else:
            binary_syntax += "0"

        comp = symbolic["comp"]
        if "A" in comp:
            binary_syntax += COMPUTING_A_TABLE[comp]
        else:
            binary_syntax += COMPUTING_M_TABLE[comp]

        if symbolic["dest"]:
            dest = symbolic["dest"]
            binary_syntax += DESTINATION_TABLE[dest]
        else:
            binary_syntax += DESTINATION_TABLE["null"]

        if symbolic["jump"]:
            jump = symbolic["jump"]
            binary_syntax += JUMP_TABLE[jump]
        else:
            binary_syntax += JUMP_TABLE["null"]

        return binary_syntax
