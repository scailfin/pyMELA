from setuptools import setup

extras_require = {
    "develop": [
        "check-manifest",
        "pytest~=6.0",
        "pytest-cov~=2.8",
        "pytest-console-scripts~=0.2",
        "bumpversion~=0.5",
        "pyflakes",
        "pre-commit",
        "black",
        "twine",
    ],
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(extras_require=extras_require)
