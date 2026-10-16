"""An original teaching parser. Python 3, standard library only. MIT licensed."""
import struct
import sys
from pathlib import Path


def parse(data):
    if len(data) < 8:
        raise ValueError("truncated header")
    if data[:4] != b"LBX1":
        raise ValueError("wrong signature")
    count = struct.unpack_from("<I", data, 4)[0]
    if len(data) != 8 + count * 2:
        raise ValueError("size does not match count")
    return [struct.unpack_from("<H", data, 8 + i * 2)[0] for i in range(count)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 inspect_lbx.py samples/a.lbx")
    try:
        print(parse(Path(sys.argv[1]).read_bytes()))
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
