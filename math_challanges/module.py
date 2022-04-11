from typing import List


def total(xs: List[float]) -> float:
    result: float = 0.0
    # For each item in xs add it to result
    for x in xs:
        result += x
    return result


def join(xs: List[int], delimiter: str) -> str:
    """produce a string of xs separated by delimiter."""
    if len(xs) == 1:
        return str(xs[0])
    if len(xs) == 0:
        return ""
    if delimiter == "":
        return "".join([str(x) for x in xs])
    result = ""
    for item in xs:
        if result == "":
            result = str(item)
        else:
            result += delimiter + str(item)
    return result


def is_string_too_long(string: str) -> bool:
    return len(string) > 255