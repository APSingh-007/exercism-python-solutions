def flatten(iterable):
    flat = []
    for item in iterable:
        flat += (
            flatten(item)
            if isinstance(item, list)
            else ([] if item is None else [item])
        )
    return flat
