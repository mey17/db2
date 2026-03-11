#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    parts = line.split(",")

    if len(parts) != 6:
        continue

    country, city, month, day, year, temp = parts

    try:
        temp = float(temp)
        print(f"{city}\t{temp}")
    except:
        pass