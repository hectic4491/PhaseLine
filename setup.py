# setup.py
from setuptools import setup, find_packages

setup(
  name = "phaseline",
  version = "0.1.0",
  packages = find_packages(),
  install_requires = [
    "numpy",
    "matplotlib",
    "scipy",
    "pytest"
  ],
  entry_points = {
    "console_scripts": [
      "phaseline=oscilloscope:main"
    ]
  },
  author = "Robert G. Hunt III",
  description = "A real-time waveform viewer and signal analyzer.",
  long_description = open("README.md", encoding = "utf-8").read(),
  long_description_content_type = "text/markdown",
  license = "MIT",
  classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
  python_requires = ">=3.12.3"
)