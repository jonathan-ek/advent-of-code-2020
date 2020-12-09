def get_input(day, post_fix=1):
    """Read the input file and return the content as a string."""
    with open(f'input/day_{day:02d}_{post_fix}.txt', 'r') as data:
        return data.read()


def flatten(data):
    return [item for sublist in data for item in sublist]
