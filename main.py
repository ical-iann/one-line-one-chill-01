"""One Line, One Chill (u-azazex-one-line-one-chill-6d4d5488).

Program/v1 entry: writes a single sentence of horror to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "The baby monitor crackled, and in my daughter's voice it whispered my full name \u2014 a name I have never once spoken aloud in this house."


def main() -> None:
    # Enforce the competition gate locally: 1-200 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
