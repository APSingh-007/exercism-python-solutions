def grep(pattern: str, flags: str, files: list[str]) -> str:
    res = []
    multiple_files = len(files) > 1

    case_insensitive = "-i" in flags
    number_lines = "n" in flags
    check_complete_line = "-x" in flags
    only_filename = "l" in flags
    reverse_grep = "-v" in flags

    for name in files:
        with open(name, "r") as file:
            for index, line in enumerate(file):
                found = False
                line = line.strip()
                line_copy = line
                pattern_copy = pattern
                if "-i" in flags:
                    line_copy = line.lower()
                    pattern_copy = pattern.lower()
                if "-n" in flags:
                    line = f"{index+1}:{line}"
                if multiple_files:
                    line = f"{name}:{line}"
                if pattern_copy in line_copy:
                    if "-x" in flags and pattern_copy != line_copy:
                        continue
                    if "-v" not in flags:
                        if "-l" in flags:
                            if name not in res:
                                res.append(name)
                        else:
                            res.append(line)
                    found = True

                if "-v" in flags and not found:
                    res.append(line)

    if res:
        return "\n".join(res) + "\n"
    return ""
