import os
import sys
from collections import Counter

def count_shebangs(directory):
    shebangs = Counter()
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    first_line = f.readline()
                    if first_line.startswith('#!'):
                        shebangs[first_line.strip()] += 1
            except Exception as e:
                print(f"Error reading file {file}: {e}", file=sys.stderr)
    return shebangs           

# Make sure to update this path to a real directory on your system
directory = "/Users/mac/Desktop/claranet/test_env"

print(f"Analyzing directory: {directory}")

shebang_counts = count_shebangs(directory)

if not shebang_counts:
    print("No shebang lines found.")
else:
    for shebang, count in shebang_counts.items():
        print(f"{count} {shebang}")
