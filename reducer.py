#!/usr/bin/env python3
import sys

current_city = None
temps = []

for line in sys.stdin:
    city, temp = line.strip().split("\t")
    temp = float(temp)

    if city == current_city:
        temps.append(temp)
    else:
        if current_city is not None:
            min_t = min(temps)
            max_t = max(temps)
            avg_t = sum(temps) / len(temps)
            print(f"{current_city} {min_t} {max_t} {avg_t:.2f}")

        current_city = city
        temps = [temp]

if current_city is not None:
    min_t = min(temps)
    max_t = max(temps)
    avg_t = sum(temps) / len(temps)
    print(f"{current_city} {min_t} {max_t} {avg_t:.2f}")