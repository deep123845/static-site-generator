from enum import Enum


class BlockType(Enum):
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED = "UNORDERED"
    ORDERED = "ORDERED"
    NORMAL = "NORMAL"


def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks


def block_to_block_type(block):
    if block[0] == "#":
        num_hash = 0
        for i in range(6):
            if block[i] == "#":
                num_hash += 1
        if block[num_hash] == " ":
            return BlockType.HEADING
        else:
            return BlockType.NORMAL

    if block[0:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE

    lines = block.split("\n")
    num_lines = len(lines)

    for i in range(num_lines):
        if lines[i][0:2] != "> ":
            break
        if i == num_lines - 1:
            return BlockType.QUOTE

    for i in range(num_lines):
        if lines[i][0:2] != "- ":
            break
        if i == num_lines - 1:
            return BlockType.UNORDERED

    curr_num = 1
    for i in range(num_lines):
        if lines[i].find(f"{curr_num}. ") != 0:
            break
        curr_num += 1
        if i == num_lines - 1:
            return BlockType.ORDERED

    return BlockType.NORMAL
