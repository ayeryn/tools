"""
Parses leetcode examples into markdown
"""


def bold_text(text: str):
    return '**' + text + '**\n'


def code_snippet(text: str):
    return f"```\n{text}\n```\n"


def process_explanation(text: str):
    words = text.split(':')
    return '**' + words[0] + ':**<br>\n' + words[1] + '<br>\n'


def process_example(text: str):
    lines = text.split('\n')
    ret = ''
    i = 0

    while i < len(lines):
        if 'Explanation' in lines[i]:
            ret += process_explanation(lines[i])
        elif 'Input' in lines[i]:
            line = lines[i] + '\n'
            i += 1
            line += lines[i]
            ret += code_snippet(line)
        elif ':' in lines[i]:
            ret += bold_text('Example' + lines[i])
        else:
            ret += lines[i] + '<br>\n'

        i += 1
    return ret


def process_file(filename='leetcode_examples.txt'):
    f = open(filename)
    text = f.read()
    examples = text.split('Example')
    ret = ''
    i = 1

    while i < len(examples):
        ret += process_example(examples[i])
        i += 1

    print(ret)


process_file()
