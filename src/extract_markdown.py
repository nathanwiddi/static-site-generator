import re
from markdown_blocks import markdown_to_blocks

def extract_title(markdown):
    # Split the markdown into blocks
    filtered_blocks = markdown_to_blocks(markdown)
    
    # Look through each block
    for block in filtered_blocks:
        lines = block.split("\n")
        for line in lines:
            # Look for a line starting with single #
            pattern = r"^#\s+(.*?)\s*$"  # Added \s* at end to handle trailing whitespace
            match = re.match(pattern, line)
            if match:
                return match.group(1).strip()
    
    # If we get here, no title was found
    raise Exception("No h1 header found in markdown file")