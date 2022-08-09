import pytest
import argparse



parser = argparse.ArgumentParser(description="Selective Test Case Runner",
    allow_abbrev=False,
)
parser.add_argument("-t", "--test", type=str, default="all",
    choices=['positive', 'negative'],
    help="Enter only positive or negative if all the test case will be run"
)

args = parser.parse_args()

pytest_command = ["test_cases/"]
if args.test == "all":
    pytest.main(pytest_command)
else:
    pytest.main(pytest_command.append("k", args.test))