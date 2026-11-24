# Build notes — Say What Actually Broke

## Kit

Downloaded the kit tarball from
`https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5/kit` and
read `RULES.txt` + `kit.json` before writing anything.

Key rules taken from the kit:

- One line, UTF-8, 1–200 characters, not only whitespace. The sealed
  scorer gives Valid 1 or 0; only a valid entry reaches the judge.
- The judge is an LLM (z-ai/glm-5.3-flash), briefed as a veteran SRE
  with no patience for vague errors. It picks the line a user would
  remember and repeat to a colleague, weighing, in order:
  1. a single line, ≤200 chars, telling the brutal truth funny;
  2. names the real failure in plain words, so the reader knows what
     broke and what to do next, instead of apologising in generalities;
  3. funny on a single read, with a twist or an image a reader
     repeats out loud.
- Blind rounds: 3 rounds, entries judged as they arrive; final heat
  takes the top 500 on the dev board.
- Harness program/v1, sandbox with no network, 60 s per run.

## Choosing the line

Candidates considered, all rejected for a reason:

- "The site is down because someone deployed on a Friday at 4:59 PM.
  We have identified the culprit. It was you." — relatable, but it
  blames the user and gives no next step.
- "Error 500: the code worked on my machine, which is currently on
  fire." — punchy, but a cliché; the judge will have seen it before.
- "Your upload failed because the server ran out of memory loading a
  4K photo of a cat. Try a smaller cat." — funny image, but the
  failure is the user's file, not the system's fault.

The line I shipped names a failure that is entirely the system's own
doing, states it in plain words, gives the next step, and the twist
is structural: the logs that are supposed to explain the outage are
the thing that caused it. That self-caused loop is the image an
on-call engineer repeats at 3 a.m., and it is specific enough that
few other entries will say the same thing.

Final line (148 chars):

> The server ran out of disk space because the error logs filled it up logging that we ran out of disk space. Delete the logs, then delete the logger.

## Implementation

- `main.py` is self-contained, stdlib only. It honours
  `MAKEFUN_OUTPUT_DIR` (default `/output`) and measures the line
  before writing: if it ever fell outside the 1–200 gate it would
  exit 1 instead of emitting an invalid entry.
- Written in this session in two chunks, then revised once to add the
  length guard. `README.md`, `prompt.txt` and this file were all
  authored in the same session; nothing was copied from a finished
  entry.

## Local verification

Run as the grader does (`python3 -P -s main.py`, fresh empty output
dir, `MAKEFUN_BOT_DIR` set to the entry dir). Result: exit 0, and
`entry.txt` contains exactly the line above plus a trailing newline
(149 bytes total, inside the gate).
