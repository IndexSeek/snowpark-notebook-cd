import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path

notebooks = sorted(
    Path("forecasting").glob("*.ipynb"), key=lambda f: int(f.name.split("-")[0])
)

for notebook in notebooks:
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor().preprocess(nb, {"metadata": {"path": "forecasting/"}})
