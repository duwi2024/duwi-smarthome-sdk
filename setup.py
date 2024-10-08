from setuptools import setup, find_packages

VERSION = '0.7.4'
DESCRIPTION = 'sdk for duwi third platform'

with open("README.md", encoding="utf-8") as fh:
    doc_long_description = fh.read()

setup(
    name="duwi-smarthome-sdk",
    version=VERSION,
    author="duwi",
    author_email="duwitech@163.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['aiohttp', 'websockets'],
    keywords=['python', 'duwi', 'sdk', 'third', 'platform'],
    entry_points={},
    license="MIT",
    url="https://github.com/duwi2024/homeassistant-sdk",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires=">=3.7",
)
