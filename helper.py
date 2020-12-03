def get_input(day, part=1):
    """Read the input file and return the content as a string."""
    with open(f'input/day_{day:02d}_{part}.txt', 'r') as data:
        return data.read()
