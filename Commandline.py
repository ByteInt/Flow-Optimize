import math
import pathlib
import time
from random import random

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

    # STRATEGY the strategy in pysummit

    #
    domain = Domain()

    # area for adding domain
    domain += CategoricalVariable(
        name='cate',
        description='2',
        levels=[
            'a',
            'b'
        ]
    )
    domain += ContinuousVariable(
        name='conti',
        description='4',
        bounds=[0, 1]
    )
    domain += ContinuousVariable(
        name='conti_2',
        description='5',
        bounds=[0,1],
        is_objective=True
    )
    domain += ContinuousVariable(
        name='yld',
        description='6',
        bounds=[0,100],
        is_objective=True
    )
    print(domain.variables)
    # Generate title of the csv file
    generate_title()
    # Test data
    generate_data()
    # The problem is that, the changes of csv file can only be applied when the program is over.
    time.sleep(1)

    '''transform = MultitoSingleObjective(
        domain, expression = "", maximize = True
    )'''

    strategy = SOBO(domain)
    data_path = pathlib.Path()
    ds = DataSet.read_csv(data_path / 'experiment.csv')


def generate_title():
    # global writer, csvfile
    with open('experiment.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        row_1 = ['NAME']
        row_2 = ['TYPE']
        for variable in domain.variables:
            print(str(variable.name))
            row_1.append(str(variable.name))
            row_2.append('DATA')
        print(row_1)
        writer.writerow(row_1)
        writer.writerow(row_2)


def generate_data():
    with open('experiment.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(100):
            if i<50:
                cate = 'a'
            else:
                cate = 'b'
            randrow = [i, cate, random(), random(), 100*random()]
            writer.writerow(randrow)
        csvfile.close()

if __name__ == '__main__':
    initiate()
    exp = ExperimentalEmulator(model_name='Model', domain=domain, dataset=ds)
    exp.train(max_epochs=500, cv_fold=10, test_size=0.2)
    next_experiments = strategy.suggest_experiments(2)
    print(str(next_experiments))
