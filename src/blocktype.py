from enum import Enum, auto


class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    UNORDERED_LIST = "*/-"
    ORDERED_LIST = "[0-9]+. "


def block_to_block_type(block: str) -> BlockType:
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING

    if block.startswith(("```")) and block.endswith(("```")):
        return BlockType.CODE

    if False not in [line.startswith(">") for line in block.split("\n")]:
        return BlockType.QUOTE

    if False not in [
        line.startswith("*") or line.endswith("-") for line in block.split("\n")
    ]:
        return BlockType.UNORDERED_LIST

    if False not in [
        line.startswith("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        for line in block.split("\n")
    ]:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
