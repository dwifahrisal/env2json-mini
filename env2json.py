#!/usr/bin/env python3
""".env -> json. support komentar, string kosong, dan quoted value"""
import json
import sys


def parse(path: str) -> dict:
    out = {}
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        out[k] = v
    return out


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else ".env"
    dst = sys.argv[2] if len(sys.argv) > 2 else "env.json"
    data = parse(src)
    with open(dst, "w") as f:
        json.dump(data, f, indent=2)
    print(f"{len(data)} variabel -> {dst}")


if __name__ == "__main__":
    main()
