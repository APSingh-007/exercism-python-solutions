# def answer(question: str) -> int:
#     question = (
#         question.replace("What is", "")
#         .replace("plus", "+")
#         .replace("minus", "-")
#         .replace("multiplied by", "*")
#         .replace("divided by", "//")
#         .replace("?", "")
#     )

#     for token in question.split(" "):
#         if token.isalpha():
#             raise ValueError("unknown operation")

#     if len(question.split()) % 2 == 0:
#         raise ValueError("syntax error")

#     exp, runs = "", 0
#     for item in question.split():
#         exp += item
#         runs += 1
#         if runs % 3 == 0:
#             try:
#                 if exp.startswith("+"):
#                     raise ValueError("syntax error")
#                 exp = str(eval(exp))
#             except Exception:
#                 raise ValueError("syntax error")
#             runs = 1
#     return int(exp)

OPS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__",
}


def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question:
        raise ValueError("syntax error")
    if question.isdigit():
        return int(question)

    found_op = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            found_op = True
    if not found_op:
        raise ValueError("unknown operation")

    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.values():
                raise ValueError("syntax error")
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except:
            raise ValueError("syntax error")
    return ret[0]
