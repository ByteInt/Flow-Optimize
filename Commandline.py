import math
import pathlib
import time
from random import random
import pkg_resources
from summit.domain import *
from summit.benchmarks import SnarBenchmark, ExperimentalEmulator
from summit.utils.dataset import DataSet
from summit.strategies import NelderMead, MultitoSingleObjective, SOBO, Random, FullFactorial, TSEMO
import csv
from summit.run import Runner

import Detector
import Device


def initiate():
    global domain, ds, strategy, writer
    # The csv file for experiment data

    domain = Domain()

    # area for adding domain
    '''domain += CategoricalVariable(
        name='cate',
        description='2',
        levels=[
            'a',
            'b'
        ]
    )'''
    domain += ContinuousVariable(
        name='conti',
        description='4',
        bounds=[0, 1]
    )
    domain += ContinuousVariable(
        name='conti_2',
        description='5',
        bounds=[0,1],
    )
    domain += ContinuousVariable(
        name='yld',
        description='6',
        bounds=[0,100],
        is_objective=True,
        maximize=True
    )
    print(domain.variables)
    # Generate title of the csv file
    generate_title()
    # Test data
    # generate_data()

    '''transform = MultitoSingleObjective(
        domain, expression = "", maximize = True
    )'''


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
        csvfile.close()


def single_experiment(var1, var2):
    # Setting some equipments to var1, 2 and 3
    print('New experiment in progress with following parameters:\nvar1:' + var1
          + '\nvar2:' + var2)
    # Waiting time based on experiment settings
    time.sleep(1)
    result = 50 * (float(var1) + float(var2))
    with open('experiment.csv', newline='') as csvfile:
        lines = csvfile.readlines()
        last_line = lines[-1]
        last_entry = last_line.split(',')[0]
        if last_entry == 'TYPE':
            index = 0
        else:
            index = int(last_entry) + 1
        csvfile.close()
    with open('experiment.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        next_row = [index, var1, var2, result]
        writer.writerow(next_row)
        csvfile.close()


if __name__ == '__main__':
    initiate()
    # pre-experiments: data are given by random
    strategy = Random(domain)
    for i in range(4):
        next_experiments = str(strategy.suggest_experiments(1)).split('\n')[2].split()
        print(str(next_experiments))
        single_experiment(next_experiments[1], next_experiments[2])
    data_path = pathlib.Path()
    # new experiments: data are given by an optimizing strategy
    ds = DataSet.read_csv(data_path / 'experiment.csv')
    strategy = NelderMead(domain)
    # Seems that NelderMead is not available as SOBO
    # The NelderMead method would sometimes report:
    # TypeError: '>' not supported between instances of 'float' and 'NoneType'
    # FullFactorial only gives boundary suggestions
    levels = dict(conti=[0, 1], conti_2 = [0, 1])
    for i in range(50):
        exp = ExperimentalEmulator(model_name='Model', domain=domain, dataset=ds)
        experiments = strategy.suggest_experiments()
        for j in range(len(str(experiments).split('\n')) - 2):
            next_experiments = str(experiments).split('\n')[j + 2].split()
            print(next_experiments)
            single_experiment(next_experiments[1], next_experiments[2])
        '''next_experiment = str(experiments).split('\n')[2].split()
        print(next_experiment)
        single_experiment(next_experiment[1], next_experiment[2])'''
        ds = DataSet.read_csv(data_path / 'experiment.csv')
        # exp.train(max_epochs=500)
