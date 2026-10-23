from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aqx-rate-calculator",
    version="1.0.0",
    author="AQX Logistics LLC",
    author_email="tech@aqxlogistics.com",
    description="Official Python SDK & CLI for international air freight calculations, California 0% tax savings, and landed cost modeling to Saudi Arabia, UAE, and Europe.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://aqxlogistics.com",
    project_urls={
        "Homepage": "https://aqxlogistics.com",
        "Tracking": "https://aqxlogistics.com/track",
        "Blog & Guides": "https://aqxlogistics.com/blog",
        "Source": "https://github.com/AQXLOGISTICS/middle-east-ecommerce-dropshipping-california-air-cargo-rates-2026",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "aqx-calc=aqx_rate_calculator.cli:main",
        ],
    },
)
