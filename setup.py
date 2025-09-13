from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from the given file.
    Ignores empty lines and comments.
    """
    requirements = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and line != "-e .":
                requirements.append(line)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="suyashvishnoi13",
    author_email="23103152@mail.jiit.ac.in",
    packages=find_packages(where="src"),   # 👈 tell setuptools to look inside src
    package_dir={"": "src"},               # 👈 map root to src
    install_requires=get_requirements("requirements.txt"),
)
