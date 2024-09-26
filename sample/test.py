import random
import re


def random_swap_options(text):
    # Use regex to match the options and their corresponding content
    options = re.findall(r"([a-e]\)) (.+)", text)

    # Extract only the content for shuffling
    contents = [content for _, content in options]

    # Shuffle the contents randomly
    random.shuffle(contents)

    # Reconstruct the text with the shuffled content
    swapped_text = text
    for i, (opt, _) in enumerate(options):
        # Escape the parentheses to avoid regex interpretation
        escaped_opt = re.escape(opt)
        swapped_text = re.sub(
            rf"{escaped_opt} .+", f"{opt} {contents[i]}", swapped_text
        )

    return swapped_text


print(
    random_swap_options(
        """
                   a) hello baby
                   b) good morning
                   c) how are you
                   d) good night
                   e) bye baby
                   """
    )
)
