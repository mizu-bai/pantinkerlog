import setuptools

setuptools.setup(
    name="pantinkerlog",
    version="0.1.0",
    author="mizu-bai",
    author_email="shiragawa4519@outlook.com",
    description="Read Tinker log.",
    url="https://github.com/mizu-bai/panvenus",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "pytinkerlog",
        "pandas",
    ],
)
