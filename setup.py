from setuptools import setup

extras_require = {}
extras_require["lint"] = sorted(set(["pyflakes", "black"]))
extras_require["test"] = sorted(
    set(
        [
            "check-manifest",
            "pytest~=6.0",
            "pytest-cov~=2.8",
            "pytest-console-scripts~=0.2",
        ]
    )
)
extras_require["develop"] = sorted(
    set(
        extras_require["lint"]
        + extras_require["test"]
        + ["bumpversion~=0.5", "pre-commit", "twine"]
    )
)
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(extras_require=extras_require)
