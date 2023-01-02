#!/usr/bin/env python3
"""Python based GitHub Action
"""
import os
import time

import requests  # pylint: disable=unused-import # noqa We are just importing this to prove the dependency installed correctly


def main():
    """Greets someone and outputs current time
    """
    who_to_greet = os.environ["INPUT_WHO-TO-GREET"]
    current_time = time.ctime()

    print(f'Hello, {who_to_greet}')

    with open(os.environ['GITHUB_OUTPUT'], 'a',
              encoding="utf-8") as env_file:
        print(f'CURRENT_TIME={current_time}', file=env_file)


if __name__ == '__main__':
    main()
