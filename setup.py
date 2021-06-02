from typing import List

from setuptools import find_packages, setup

package_name = "checkarg"
requirements: List[str] = []
setup_requirements = ["pytest-runner", "wheel"]
test_requirements = ["flake8==3.7.8", "pytest==5.2.0", "pytest-cov==2.8.1"]

setup(
    name=package_name,
    version="0.1.0",
    url="https://github.com/Farfetch/checkarg.git",
    license="MIT License (MIT)",
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    setup_requires=setup_requirements,
    install_requires=requirements,
    tests_require=test_requirements,
    author="farfetch",
    author_email="opensource@farfetch.com",
    description="Guard clause library for Python projects, to validate arguments on every python function/method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
