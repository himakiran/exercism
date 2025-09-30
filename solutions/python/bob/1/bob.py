def response(hey_bob):
    question=False
    all_caps=False
    all_space=False
    if hey_bob.endswith('?') or hey_bob.rstrip().endswith('?'):
        question=True
    if hey_bob.isupper():
        all_caps=True
    if hey_bob.isspace():
        all_space=True
    if (question and all_caps):
        return "Calm down, I know what I'm doing!"
    if (question and not all_caps):
        return "Sure."
    if (all_caps and not question):
        return "Whoa, chill out!"
    if all_space or hey_bob=="":
        return "Fine. Be that way!"
    return "Whatever."
        