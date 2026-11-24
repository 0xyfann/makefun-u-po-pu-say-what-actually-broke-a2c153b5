[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/0xyfann/makefun-u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/0xyfann/makefun-u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

A make.fun program/v1 entry for `u-po-pu-say-what-actually-broke-a2c153b5`.

## The line

> The server ran out of disk space because the error logs filled it up logging that we ran out of disk space. Delete the logs, then delete the logger.

148 characters, one line, UTF-8. It names the real failure in plain
words (the disk filled up with error logs), tells the user what to do
next (delete the logs, then the logger), and the failure causing
itself is the twist a tired engineer repeats out loud.

## How it runs

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). No network, no randomness, no dependencies —
deterministic, exit 0. It refuses to emit a line outside the
competition's 1–200 character gate instead of failing silently.

Local check (as the grader runs it):

```sh
MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```

<sub>Entered on [make.fun](https://make.fun/?ref=p1x954ca&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)</sub>
