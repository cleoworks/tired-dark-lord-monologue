#!/usr/bin/env python3
"""The Tired Dark Lord — make.fun entry.

Writes one 100-word monologue, spoken by a fantasy villain who is
secretly just very tired, to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input,
no randomness.

The monologue is the Dowager Poisoner: she has poisoned the coronation
vintage three reigns ago, keeps forty years of ledgers, and hands every
would-be killer a number. Her tiredness never gets announced — it shows
in one lost thread ("...what was I saying?") and in the last line.
"""

import os

# The monologue in four beats, joined with single spaces: the welcome,
# the history, the ledger, and the sting. Exactly 100 words, 546
# characters, no trailing newline: the gate counts characters (1-600),
# and the tie-break favours the smaller text.
BEAT_WELCOME = (
    "Come in, dear. Mind the step. The third one sags. The wine is poured. "
    "Which cup is yours? No matter."
)
BEAT_HISTORY = (
    "I poisoned the coronation vintage three reigns ago; the cellar still "
    "hasn't forgiven me. You came to kill me? Lovely. Take a number. "
    "The usurper took one. The priest took two."
)
BEAT_LEDGER = (
    "Everyone wants the throne; nobody wants the ledgers. Forty years of "
    "ledgers. I know every traitor's handwriting, none of their faces. "
    "Drink up. Or don't. The poison needs you to stay for supper, and "
    "supper \u2014 ...what was I saying?"
)
BEAT_STING = "Sit down. The night is young. I am not."

MONOLOGUE = " ".join([BEAT_WELCOME, BEAT_HISTORY, BEAT_LEDGER, BEAT_STING])


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
