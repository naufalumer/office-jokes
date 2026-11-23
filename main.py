"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one line about office life to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no files read besides this one.
"""

import os

JOKE = (
    'In my exit interview, they asked what would have made me stay. '
    'I said, "This interview, three years ago."'
)


def main():
    # The gate accepts 1 to 199 characters; refuse to write a line that
    # could never be judged rather than submitting a silent invalid entry.
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 199:
        raise SystemExit(f"joke is {len(joke)} characters, gate needs 1-199")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
