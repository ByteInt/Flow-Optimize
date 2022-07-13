from summit.benchmarks import ExperimentalEmulator
from summit.domain import *
from summit.utils.dataset import DataSet
import pkg_resources
import pathlib

from summit import Runner
from summit.strategies import Random, SOBO, MultitoSingleObjective, TSEMO, LHS
from summit.benchmarks import SnarBenchmark
from summit.utils.dataset import DataSet
import matplotlib.pyplot as plt

# 创建一个Domain类，便于后面添加变量
domain = Domain()

# 添加一个列举的变量。例如催化剂，碱，溶剂等等，使用CategorialVariable
des_1 = "Catalyst type - different ligands"
domain += CategoricalVariable(
    name="catalyst",
    description=des_1,
    levels=[
        "P1-L1",
        "P2-L1",
        "P1-L2",
        "P1-L3",
        "P1-L4",
        "P1-L5",
        "P1-L6",
        "P1-L7",
    ],
)
# 数值变量。温度，反应时间，催化剂载量S/C，体系压力等，使用ContinuousVariable
des_2 = "Residence time in seconds (s)"
domain += ContinuousVariable(name="t_res", description=des_2, bounds=[60, 600])

des_3 = "Reactor temperature in degrees Celsius (ºC)"
domain += ContinuousVariable(
    name="temperature", description=des_3, bounds=[30, 110]
)

des_4 = "Catalyst loading in mol%"
domain += ContinuousVariable(
    name="catalyst_loading", description=des_4, bounds=[0.5, 2.5]
)
# 实验结果。产率，ee值，TON等使用ContinuousVariable, 其中is_objective = True
# maximize根据情况设置
des_5 = "Yield"
domain += ContinuousVariable(
    name="yld",
    description=des_5,
    bounds=[0, 100],
    is_objective=True,
    maximize=True,
)


des_6 = (
    "Turnover number - moles product generated divided by moles catalyst used"
)
domain += ContinuousVariable(
    name="ton",
    description=des_6,
    bounds=[0, 200],
    is_objective=True,
    maximize=True,
)
# 确认实验变量和范围
print(str(domain))

# 已有实验数据所在的文件夹。实验数据按照要求保存为csv格式
DATA_PATH = pathlib.Path(pkg_resources.resource_filename("summit", "benchmarks/data"))

# 读取已有实验数据
ds = DataSet.read_csv(DATA_PATH / "reizman_suzuki_case_1.csv")
# 根据已有数据训练出模型，“exp”
exp = ExperimentalEmulator(model_name='your_reizman', domain=domain, dataset=ds)
# verbose：实时观察
exp.train(max_epochs=500, cv_fold=10, test_size=0.2, verbose=0)

# 检验训练的模型
fig, ax = exp.parity_plot(include_test=True)


# expression输入参数。有同时优化的参数时，选择Multi to Single
# 然后输入对多个参数的“取舍”，即多个参数的优化表达式
transform = MultitoSingleObjective(
    exp.domain, expression="yld+0*ton", maximize=True
)

strategy = SOBO(exp.domain, transform = transform)

next_experiments = strategy.suggest_experiments(2)
print(str(next_experiments))

