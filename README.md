# Advent of Code

2022 is the first year I am participating in [Advent of Code](https://adventofcode.com/). I am using this repository to store my solutions.

I am working with [Python](https://www.python.org/) and trying to solve all the solutions using standard Python libraries. The code is stored in the `2022` directory and each solution is stored in `day{number}.py` files. The dependencies are stored in `requirements.txt` and can be installed using `pip install -r requirements.txt`.

To create a new virtual environment:

```bash
mkdir -p ~/projects/foo
cd ~/projects/foo
python -m virtualenv --prompt . venv
```

Activate the environment:

```bash
source venv/bin/activate
```

And install the dependencies:

```bash
pip install -r requirements.txt
```

For maintaining code quality I am using pre-commit hooks. The hooks are stored in `.pre-commit-config.yaml` and can be installed using `pre-commit install`.

## 2022

### Day 1

[Day 1](https://adventofcode.com/2022/day/1) is about reading a list of numbers (calories of food carried by Elves) and finding the Elf that carries most of them, and provide the total amount of calories.

The solution is available in [day1.py](2022/day01.py).
