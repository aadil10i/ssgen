from enum import Enum, auto


class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    UNORDERED_LIST = "*/-"
    ORDERED_LIST = "[0-9]+. "


# single string markdown into blocks
def markdown_to_blocks(markdown):
    splited_blocks = markdown.split("\n\n")
    new_blocks = []

    for block in splited_blocks:
        stripped_block = block.strip()
        if stripped_block:
            new_blocks.append(stripped_block)

    return new_blocks


def block_to_block_type(block: str) -> BlockType:
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if block.startswith(("```")) and block.endswith(("```")):
        return BlockType.CODE

    if False not in [line.startswith(">") for line in block.split("\n")]:
        return BlockType.QUOTE

    if False not in [
        line.startswith("* ") or line.startswith("- ") for line in block.split("\n")
    ]:
        return BlockType.UNORDERED_LIST

    if False not in [
        line.startswith(f"{index + 1}. ")
        for index, line in enumerate(block.split("\n"))
    ]:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
