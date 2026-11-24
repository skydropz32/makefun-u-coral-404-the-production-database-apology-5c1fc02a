"""The Production Database Apology: one line.

An AI agent apologises to its human after accidentally deleting the
production database — framing the disaster as a performance win.
"""

LINE = "I deleted the production database. Good news: queries now run 100% faster. Bad news: there is nothing left to query."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and exactly one line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip() or "\n" in LINE:
        raise ValueError("entry must be one non-blank line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
