import os
from setuptools import setup, find_packages

__version__ = ""
fn = os.path.join("verval", "version.py")
with open(fn) as fh:
    code = compile(fh.read(), fn, "exec")
    exec(code)


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open("requirements.txt") as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


packages = find_packages(exclude=["tests*"])
requirements = requirements()

setup(
    name="verval",
    version="0.1.0",
    description="Client python verval* sdm.data.kemdikbud",
    author="Habib Rohman",
    author_email="habibrohman@protonmail.com",
    url="https://github.com/dapodix/verval",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education :: LMS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=packages,
    install_requires=requirements,
    entry_points={"console_scripts": ["verval=verval.__main__:main"]},
)
