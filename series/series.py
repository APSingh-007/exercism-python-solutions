def slices(series, length):
    errors = [not series, length > len(series), length < 0, length == 0]
    info = [
        "series cannot be empty",
        "slice length cannot be greater than series length",
        "slice length cannot be negative",
        "slice length cannot be zero",
    ]
    if any(errors):
        raise ValueError(info[errors.index(True)])

    return [series[sli : length + sli] for sli in range(0, len(series) - length + 1)]
