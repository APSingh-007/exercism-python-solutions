def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    is_question = hey_bob.endswith("?")

    if hey_bob.isupper():
        if is_question:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."
