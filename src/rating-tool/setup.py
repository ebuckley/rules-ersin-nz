from setuptools import find_packages, setup

setup(
    name='rating_tool',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    entry_points= {
        'console_scripts': ['rating_tool=rating_tool:main']
    }
)