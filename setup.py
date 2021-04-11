from setuptools import setup, find_packages

__version__ = "1.0"
setup(
    name="kaggle-shopee-product-matching",
    version=__version__,
    python_requires="~=3.7",
    install_requires=[
        "datatable==0.11.1",
        "gcsfs==0.7.2",
        "google-cloud-logging==1.15.1",
        "google-cloud-storage==1.30.0",
        "langid==1.1.6",
        "lightgbm==3.1.1",
        "optuna==2.6.0",
        "pandas==1.2.2",
        "pyarrow==3.0.0",
        "scikit-learn==0.24.1",
        "tensorflow==2.4.1",
    ],
    extras_require={
        "tests": [
            "black==20.8b1",
            "mypy==0.812",
            "pytest==6.2.3",
            "pytest-cov==2.11.1",
        ],
        "notebook": ["jupyterlab==1.2.16", "seaborn==0.11.1", "tqdm==4.56.2"],
    },
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    description="Kaggle Shopee Product Matching competition",
    license="MIT",
    author="seahrh",
    author_email="seahrh@gmail.com",
    url="https://github.com/seahrh/kaggle-shopee-product-matching",
)
