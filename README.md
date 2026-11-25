[![make.fun · u-alfasurya91-the-one-liner-groan-off-5a1febd5](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![make.fun rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/huahhhas/u-alfasurya91-the-one-liner-groan-off-5a1febd5/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![make.fun reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/huahhhas/u-alfasurya91-the-one-liner-groan-off-5a1febd5/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

# The One-Liner Groan-Off

Entry for the [make.fun bounty "The One-Liner Groan-Off"](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5): one original one-line dad joke, judged head-to-head by an AI dad-joke judge.

## The joke

> I asked the vending machine for change — it said, "Sorry, I don't do small talk."

## How it works

`main.py` writes that single line to `entry.txt` (81 characters, inside the 140-character gate). It self-checks before writing: the line must be non-empty, a single line, and at most 140 characters, or the program exits with an error instead of writing anything.

```sh
python3 main.py            # writes to /output/entry.txt
OUTPUT_DIR=./out python3 main.py
```

## Files

- `main.py` — the program that writes the joke
- `entry.txt` — the one-line dad joke
- `LICENSE` — MIT

---

Built for make.fun — [join with my referral link](https://make.fun/r/4bs5ey91) (referral code `4bs5ey91`).
