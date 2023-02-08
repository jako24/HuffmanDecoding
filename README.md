# HuffmanDecoding

This code implements the Huffman Encoding algorithm, which is a data compression method used to convert data (such as text) into a more compact form by replacing frequently occurring characters with shorter binary codes. The algorithm consists of four main steps:

Calculation of frequency of characters in the text.
Building a Huffman tree based on the frequency of characters.
Encoding the data using the Huffman tree to produce the compressed representation.
Decoding the compressed data back into the original text.
The code uses several helper functions, such as calculate, calc_freq, huffman_tree, huffman_encoding, huffman_decoding, save_compress_file, and compress_file, to perform these steps.
