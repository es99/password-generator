from setuptools import setup, find_packages

def read(filename):
    return [pacotes.strip() for pacotes in open(filename).readlines()]

setup(
    name="generatorpass",
    version="0.0.1",
    description="Password Generator app running in flask",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)