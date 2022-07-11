# Import summit
from summit.benchmarks import SnarBenchmark
from summit.strategies import NelderMead, MultitoSingleObjective
from summit.run import Runner

# Instantiate the benchmark
exp = SnarBenchmark()

# Since the Snar benchmark has two objectives and Nelder-Mead is single objective, we need a multi-to-single objective transform
transform = MultitoSingleObjective(
    exp.domain, expression="-sty/1e4+e_factor/100", maximize=False
)
for v in exp.domain.variables:
    print(v.name)

# Set up the strategy, passing in the optimisation domain and transform
nm = NelderMead(exp.domain, transform=transform)

# Use the runner to run closed loop experiments
r = Runner(
    strategy=nm, experiment=exp,max_iterations=50
)
# r.run()
