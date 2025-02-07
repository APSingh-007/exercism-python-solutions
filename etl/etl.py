def transform(legacy_data: dict):
    result = {}
    for key, values in legacy_data.items():
        for item in values:
            result[item.lower()] = key
    return result
