from setuptools import setup, find_packages

setup(
    name="python_alacritty",
    version="1.0",
    packages=find_packages(),
    include_packages_data=True,
    install_requires=[
        "argparse",
    ],
    entry_points="""
        [console_scripts]
        set-theme=app.pyterminal:main
    """
)
