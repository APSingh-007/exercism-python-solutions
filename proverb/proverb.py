def proverb(*words, qualifier=None) -> list:
    result = [
        f"For want of a {words[i]} the {words[i+1]} was lost."
        for i in range(0, len(words) - 1)
    ]

    return (
        []
        if not words
        else result + [f"And all for the want of a {qualifier} {words[0]}."]
        if qualifier
        else result + [f"And all for the want of a {words[0]}."]
    )
