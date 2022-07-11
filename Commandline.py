import pathlib
import pkg_resources
from summit.domain import *
from summit.benchmarks import SnarBenchmark, ExperimentalEmulator
from summit.utils.dataset import DataSet
from summit.strategies import NelderMead, MultitoSingleObjective, SOBO
import csv
from summit.run import Runner
import Device


def initiate():
    global domain, ds, strategy, writer
    # The csv file for experiment data
    writer = csv.writer(open('experiment.csv', 'w', newline=''))

    # STRATEGY the strategy in pysummit

    #
    domain = Domain()

    # area for adding domain
    domain += CategoricalVariable(
        name='1',
        description='2',
        levels=[
            'a',
            'b'
        ]
    )
    domain += ContinuousVariable(
        name='3',
        description='4',
        bounds=[0, 1]
    )
    domain += ContinuousVariable(
        name='yld',
        description='5',
        bounds=[0,100],
        is_objective=True
    )

    row = []
    for variable in domain.variables:
        print(variable.name)
        row.append(variable.name)

    '''transform = MultitoSingleObjective(
        domain, expression = "", maximize = True
    )'''

    strategy = SOBO(domain)
    ds = DataSet.read_csv("experiment.csv")


if __name__ == '__main__':
    initiate()
    exp = ExperimentalEmulator(model_name='Model', domain=domain, dataset=ds)
    exp.train(max_epochs=500, cv_fold=10, test_size=0.2)
    next_experiments = strategy.suggest_experiments(2)
    print(next_experiments)

