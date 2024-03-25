#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys


def print_stats(status_counts, total_size):
    """Prints the file size and the number of lines for each status code"""
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count != 0:
            print("{}: {:d}".format(status_code, count))


status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_number = 0

try:
    for line in sys.stdin:
        line_number += 1
        if line_number % 10 == 0:
            print_stats(status_counts, total_size)

        parts = line.split()
        try:
            status_code = parts[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1
        except IndexError:
            pass

        try:
            file_size = int(parts[-1])
            total_size += file_size
        except (ValueError, IndexError):
            pass

    print_stats(status_counts, total_size)

except KeyboardInterrupt:
    print_stats(status_counts, total_size)
    raise
