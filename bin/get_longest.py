#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@FileName: get_longest
@Time: 2022/3/25,20:50
@Name: Zhang Yixing
"""
import argparse
from Bio import SeqIO


def read_file(file):
    t = {}  # 记录长度和序列名字
    result = {}  # 这个字典用于储存最长转录本 或者 最长cds 或者 最长protein
    for seq_record in SeqIO.parse(file, "fasta"):
        id = seq_record.id.rsplit(".", 1)[0]

        if id not in t:
            result[seq_record.id] = str(seq_record.seq)
            t[id] = [len(seq_record.seq), seq_record.id]
        else:
            if t[id][0] >= len(seq_record.seq):
                continue
            else:
                #result.pop(t[id][1])
                result[seq_record.id] = str(seq_record.seq)
                t[id] = [len(seq_record.seq), seq_record.id]
    return result


def write(filename, res):
    with open(filename, 'w') as f:
        for i, j in res.items():
            f.write(">" + i + "\n")
            f.write(j + "\n")


def main():
    parser = argparse.ArgumentParser(usage='python get_longest.py -i cds.fs -o result.fa')
    parser.add_argument("-i", "--input", help="input filename")
    parser.add_argument("-o", "--output", help="output filename")
    args = parser.parse_args()
    res_dict = read_file(args.input)
    write(args.output, res_dict)


if __name__ == '__main__':
    # res_dict = read_file(r'./cds.fa')
    # write(r'out_cds', res_dict)
    main()

