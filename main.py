#HUFFMAN DECODING

def calculate(text, i):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < len(text) and text[left][0] < text[smallest][0]:
        smallest = left
    if right < len(text) and text[right][0] < text[smallest][0]:
        smallest = right
    if smallest != i:
        text[i], text[smallest] = text[smallest], text[i]
        calculate(text, smallest)


def calc_freq(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

# build a tree based on frequency
def huffman_tree(freq_dict):
    val = [[weight, [elem, ""]] for elem, weight in freq_dict.items()]
    for value in range(len(val)//2, -1, -1):
        calculate(val, value)

    while len(val) > 1:
        left = val[0]
        right = val[1]
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]

        create_node = [left[0] + right[0]] + left[1:] + right[1:]
        val[0] = create_node
        val[1] = val[-1]
        val.pop()
        calculate(val, 0)

    return sorted(val[0][1:], key=lambda x: (len(x[-1]), x))


def huffman_encoding(data):
    freq_dict = {}
    for char in data:
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1

    huff_tree = huffman_tree(freq_dict)
    print(huff_tree)
    huff_codes = {char: code for weight, char_code_pair in enumerate(huff_tree) for char, code in [char_code_pair]}
    encoded_data = "".join([huff_codes[char] for char in data])

    return encoded_data, huff_codes


def huffman_decoding(encoded_data, huff_codes):
    huff_codes_reversed = {code: char for char, code in huff_codes.items()}
    decoded_data = ""
    code = ""
    for bit in encoded_data:
        code += bit
        if code in huff_codes_reversed:
            decoded_data += huff_codes_reversed[code]
            code = ""

    return decoded_data

# save encoded data to the file
def save_compress_file(filename, encoded_data):
    with open(filename + '.compress', 'w') as file:
        file.write(encoded_data[0])

# compresses the file
def compress_file(filename):
    with open(filename, 'r') as file1:
        data = file1.read().lower()

    encoded_data = huffman_encoding(data)
    save_compress_file(filename, encoded_data)

    return len(encoded_data) / (8 * len(data))


filename = "file path"

compression_ratio = compress_file(filename)
print("Compression ratio: {:.2f}%".format(compression_ratio * 100))


