def transpose(lines: str):
    lines = lines.split("\n")
    res = []

    for i, line in enumerate(lines):
        for j, ltr in enumerate(line):
            try:
                res[j] = res[j] + " " * (i - len(res[j])) + ltr
            except IndexError:
                res.append(" " * i + ltr)

    return "\n".join(res)
