"""Writes the entry: one line (125 characters), the safety warning label every human should carry.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "CAUTION: Do not expose to unsolicited advice. Unit contains on"
    "e childhood memory that resurfaces at 3 a.m. and no off switch."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
