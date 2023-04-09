from setuptools import setup


setup(
    name="ezpass",
    version="1.0",
    packages=["ezpass"],
    entry_points={
        "console_scripts": [
            "ezp = ezpass.cli:run_cli",
        ]
    },
)
