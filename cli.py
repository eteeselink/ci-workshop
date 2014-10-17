from logparser import parser
from aggregator import aggregator
from extrapolator import extrapolator
from visualizer import visualizer

def parse(argv):
    return []


def run(argv):
    print("parsing arguments: " + str(argv))
    args = parse(argv)

    print(parser.hello())
    print(aggregator.hello())
    print(extrapolator.hello())
    print(visualizer.hello())
