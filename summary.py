import json

def token_count(text):
    return len(text.strip().split())

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    specific_magnitude = 0
    num2 = num
    while abs(num2) >= 1:
        specific_magnitude += 1
        num2 /= 10.0
    # add more suffixes if you need them
    return '%.{}f%s'.format(3-specific_magnitude) % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

row_length = None
num_jokes_total = 0
num_tokens_total = 0

ROW_FORMAT = "{:<17} | {:>5} jokes | {:>5} tokens"

for filename in sorted(["wocka.json", "stupidstuff.json", "reddit_jokes.json"]):
    with open(filename) as f:
        jokes = json.load(f)
        num_tokens = sum([token_count(x.get("body")) for x in jokes])
        row_str = ROW_FORMAT.format(filename, human_format(len(jokes)), human_format(num_tokens))
        num_jokes_total += len(jokes)
        num_tokens_total += num_tokens
        if row_length is None:
            row_length = len(row_str)
            print("-" * row_length)
        print(row_str)

print("-" * row_length)
print(ROW_FORMAT.format("TOTAL", human_format(num_jokes_total), human_format(num_tokens_total)))
print("-" * row_length)