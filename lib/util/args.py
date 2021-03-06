from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser(description="Util module for Replica-GH.")
    parser.add_argument('--file-extension-stats', action='store_true',
                        help='count the distribution of file extensions in the dataset')
    parser.add_argument('--aggregate', action='store_true',
                        help='aggregate stats across entities')
    args = parser.parse_args()
    return args
