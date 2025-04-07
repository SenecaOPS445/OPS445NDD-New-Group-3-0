def parse_arguments():
    """
    Parse command-line arguments for user input
    """
    # Create an argument parser
    parser = argparse.ArgumentParser

    # Add argument for interval (seconds between CPU samples)
    parser.add_argument("--interval", type=int, default=2)

    # Add argument for output directory or file
    parser.add_argument("--output", default="Reports")

    return parser.parse_args()  # Return the parsed arguments
