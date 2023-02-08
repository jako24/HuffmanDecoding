# HuffmanDecoding

This code implements the Huffman Encoding algorithm, which is a data compression method used to convert data (such as text) into a more compact form by replacing frequently occurring characters with shorter binary codes. The algorithm consists of four main steps:

1. Calculation of frequency of characters in the text.
2. Building a Huffman tree based on the frequency of characters.
3. Encoding the data using the Huffman tree to produce the compressed representation.
4. Decoding the compressed data back into the original text.

The code uses several helper functions, such as calculate, calc_freq, huffman_tree, huffman_encoding, huffman_decoding, save_compress_file, and compress_file, to perform these steps.

# HOW THE CODE WORKS

Steps: 
1. Create a text file
2. Input the file's location in "filename = [file path]"
3. After executing the code, a new file with '.compress' added to its name will be generated in the same directory.
