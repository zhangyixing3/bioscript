#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@FileName: 读取fa
@Time: 2022/7/27,20:31
@Name: Zhang Yixing
"""
import sys
import time
import pyfastx
import logging
from collections import defaultdict
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        logging.log(logging.DEBUG,
                    "\033[36mTotal time running %s: %s seconds\033[0m" % (function.__name__, str(t1 - t0)))
        return result

    return function_timer


@fn_timer
def readfile(file):
    aDict = defaultdict(list)

    for line in open(file):
        if line[0] == '>':
            key = line[1:-1]
        else:
            aDict[key].append(line.strip())
    for key, value in aDict.items():
        aDict[key] = ''.join(value)


@fn_timer
def readfile2(file):
    res = {}
    with open(file) as f:
        for line in f:
            if line.startswith('>'):
                id = line.strip().split()[0]
                res[id] = ''
            else:
                res[id] += line.strip()


@fn_timer
def getf(file):
    a = {}
    for item in pyfastx.Fastx(file):
        a[item[0]] = item[1]


def main():
    LOG_FORMAT = "%(asctime)s\n   in line %(lineno)d %(filename)s \033[31m%(levelname)s:\033[0m%(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt='%Y/%d/%m %H:%M')  
    if len(sys.argv) != 2:
        logging.log(logging.WARNING, "\033[31mUsage: python %s fasta_file\033[0m" % sys.argv[0])
    else:
        file = sys.argv[1]
        readfile(file)
        getf(file)
        # readfile2(file)


if __name__ == "__main__":
    main()
