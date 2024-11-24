import re

def separate_batch_script(text):
    # Use regex to find the batch code within the code block
    pattern = r'(@echo off.*?exit)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def separate_keywords(text):
    keywords = re.split(r",\s*", text)
    # Strip whitespace and newline characters from each keyword
    keywords = [keyword.strip() for keyword in keywords]
    return keywords
