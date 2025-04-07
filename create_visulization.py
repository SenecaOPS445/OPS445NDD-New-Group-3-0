def create_visualization(percentage):
    """
    Create a simple text-based visualization.

    One '#' character represents 2% of usage.

    """

    num_hashes = int(percentage / 2) # this calculates how many # symbols to use based on the %
    return '#' * num_hashes #this will return a string with that many # characters
