from enum import Enum

class BlockType(Enum):
    paragraph = "PARAGRAPH"
    heading = "HEADING"
    code = "CODE"
    quote = "QUOTE"
    unordered_list = "UNORDERED"
    ordered_list = "ORDERED"


def markdown_to_blocks(markdown):
    block_list = []

    for block in markdown.split("\n\n"):
        if block.strip() == "":
            continue
        block_list.append(block.strip())


    return block_list