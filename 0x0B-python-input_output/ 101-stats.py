#!/usr/bin/python3

"""101-stats.py: reads stdin line by line and computes metrics"""


def print_stats(file_size, status_codes):
    """Prints the computed metrics"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            file_size += int(data[-1])
            status_codes[data[-2]] += 1
            if counter == 10:
                print_stats(file_size, status_codes)
                counter = 0
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats
