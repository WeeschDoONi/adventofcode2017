from collections import deque
from functools import reduce
from operator import xor


def process_circle_list(lengths, repeat):
    circle_list = deque(range(256))
    cur_pos = deque(range(256))
    skip_size = 0
    
    for _ in range(repeat):
        for length in lengths:
            circle_list.extend(reversed(deque(circle_list.popleft() for _ in range(length))))
            circle_list.rotate(-skip_size)
            cur_pos.rotate(-length-skip_size)
            skip_size += 1
            
    circle_list.rotate(cur_pos.popleft())
            
    return circle_list


def calc_hex_hash(data):

    data_ascii = [ord(c) for c in data]        
    data_ascii.extend([17, 31, 73, 47, 23])  

    sparse_hashes = process_circle_list(lengths=data_ascii, repeat=64) 
    sparse_hashes = list(sparse_hashes)

    dense_hashes = [reduce(xor, sparse_hashes[i*16:(i+1)*16]) for i in range(16)]

    return ''.join('%02x'%x for x in dense_hashes)