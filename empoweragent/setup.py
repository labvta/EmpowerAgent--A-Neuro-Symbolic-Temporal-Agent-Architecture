from setuptools import setup, find_packages

setup(
    name="empoweragent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.10",
        "pytorch-lightning>=1.5",
        "numpy",
        "tqdm",
        "networkx",
        "matplotlib"
    ],
    author="Your Name",
    author_email="you@example.com",
    description="A neuro-symbolic cognitive agent with empowerment, STDP, NHMS and logic reasoning.",
    long_description=open("README.md").read() if Path("README.md").exists() else '',
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/empoweragent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
