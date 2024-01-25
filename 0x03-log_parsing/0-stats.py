#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics """
import sys
import re

count = 0
total_file_size = 0
dict_status = {}
pattern = (
    r'^(\d{1,3}\.){3}\d{1,3}'
    r' - '
    r'\[\d{4}-\d{2}-\d{2}'
    r' \d{2}:\d{2}:\d{2}\.\d+\]'
    r' "GET /projects/260 HTTP/1\.1"'
    r' \d{3}'
    r' \d+$'
)
for line in sys.stdin:

    try:

        if re.match(pattern, line):
            count += 1
            match_file_size = re.search(r'\d+$', line)
            match_status = re.search(r'(\d+)\s+\d+$', line)

            if match_file_size:
                file_size = match_file_size.group()
                total_file_size += int(file_size)
            else:
                print("No number found at the end of the string.")

            if match_status:
                status = match_status.group(1)
                if status in dict_status:
                    dict_status[status] += 1
                else:
                    dict_status[status] = 1
            else:
                print("no second number")

            if count % 10 == 0:
                print('Simulating CTRL+C interruption after 10 lines...')
                raise KeyboardInterrupt
        else:
            continue

    except KeyboardInterrupt:
        count = 0
        print('File size: {:d}'.format(total_file_size))
        for key, value in sorted(dict_status.items()):
            print('{}: {:d}'.format(key, value))
