#!/usr/bin/env python
import sys
from newslatter_crypto.crew import NewslatterCryptoCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'list 10 news about cryptocurrency trends for July 2024'
    }
    NewslatterCryptoCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        NewslatterCryptoCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
