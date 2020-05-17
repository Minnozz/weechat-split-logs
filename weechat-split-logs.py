#!/usr/bin/env python3

import sys
import glob
import os
from datetime import datetime

def split_log_file(log_file_path, output_dir_format):
    print(f"Processing {log_file_path}...")
    base_name = os.path.basename(log_file_path)

    current_file_name = ""
    current_file = None

    with open(log_file_path, 'r') as fp:
        n = 0
        for line in fp:
            line_date = datetime.strptime(line[0:10], "%Y-%m-%d")
            output_dir = line_date.strftime(output_dir_format)
            output_file_name = os.path.join(output_dir, base_name)

            if output_file_name != current_file_name:
                if current_file != None:
                    # print(f"\tWrote {n} lines to {current_file_name}")
                    current_file.close()

                os.makedirs(output_dir, 0o755, True)
                try:
                    current_file = open(output_file_name, 'x')
                except FileExistsError:
                    current_file = open(output_file_name + ".split", 'a')
                    print(f"\tCreated {output_file_name}.split because {output_file_name} already existed")

                current_file_name = output_file_name
                n = 0

            current_file.write(line)
            n += 1

    if current_file != None:
        # print(f"\tWrote {n} lines to {current_file_name}")
        current_file.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <log/dir> <output/dir/with/%Y/%m>")
        print("Supported date formatting: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior")
        sys.exit(1)

    log_dir = sys.argv[1]
    output_dir_format = sys.argv[2]

    log_files_in = glob.glob(os.path.join(log_dir, "*.weechatlog"))

    for log_file_path in log_files_in:
        split_log_file(log_file_path, output_dir_format)
