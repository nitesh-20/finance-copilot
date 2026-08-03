from setuptools import setup, find_packages

# Read requirements.txt, ignore comments
try:
    with open("requirements.txt", "r") as f:
        REQUIRES = [line.split("#", 1)[0].strip() for line in f if line.strip()]
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name="Finance Copilot",
    version="0.1.5",
    include_package_data=True,
    author="Finance Copilot Developers",
    author_email="info@finance_copilot.local",
    url="https://github.com/Finance Copilot/Finance Copilot",
    license="MIT",
    packages=find_packages(),
    install_requires=REQUIRES,
    description="Finance Copilot: An Open-Source AI Agent Platform for Financial Applications using LLMs",
    long_description="""Finance Copilot""",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="Financial Large Language Models, AI Agents",
    platforms=["any"],
    python_requires=">=3.10",
)
