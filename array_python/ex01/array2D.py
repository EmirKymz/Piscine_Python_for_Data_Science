def slice_me(family: list, start: int, end: int) -> list:
    """
    Controls the input values as follows:
    - The start and end values should be integers.
    - The family should be a list.
    - The family should not be empty.
    - The start and end values should not be greater
    than the length of the list.

    The function:
    - Prints the shape of the list.
    - Prints the shape of the sliced list.
    - Prints the sliced list.
    - Returns a string containing the above information.
    """
    try:
        assert (isinstance(start, int) and isinstance(end, int)), \
            "Error: Start and end should be of type int"
        assert start <= len(family) or end <= len(family), \
         "Error: Start or end is greater than the length of the list"
        assert len(family) > 0, "Error: Empty list"
        assert isinstance(family, list), \
            "Error: family should be of type list"
    except AssertionError as e:
        print(e)
        exit(1)
    str = f"My shape is : ({len(family)}, {len(family[0])})\n\
My new shape is : ({len(family[start:end])}\
, {len(family[start:end][0])})\n{family[start:end]}"
    return str
