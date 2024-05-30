from setuptools import setup, find_packages


setup(
    name="lyama_buddy",
    version="0.1.0",
    author="Vinni Cedraz",
    url="https://github.com/Vinni-Cedraz/lyama_buddy",
    description="llama 70b with groq on your terminal",
    packages=find_packages(),
    install_requires=[
        "groq",
        "termcolor",
        "art",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "lyama_buddy = lyama_buddy.main:main",
        ],
    },
)
