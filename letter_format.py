"""Import Module"""
from get_quote import quote

def letter_body():
    """letter body"""
    q = quote("happiness")[0]

    body = f"""
    {q['quote']}
    -{q['author']}

    For your {q["category"]}
    """
    return body
