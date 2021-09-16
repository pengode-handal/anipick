
from setuptools import find_packages, setup

with open('readme.md', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt', 'r') as fh:
    module = fh.read()
setup(
    name="Anipick",
    author="Kenzawa/Babwa",
    author_email="babwaxgura@gmail.com",
    version='1.4.0',
    description="Anime module for search Anime, Manga, Quote info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries",
],
    python_requires='>=3.6',               
    py_modules=["anipick"],             
    url="https://github.com/pengode-handal/anipick",
    packages=find_packages(),
    install_requires=module,
)