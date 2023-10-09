from setuptools import setup, find_packages, Extension
# Workaround for issue
# https://bugs.python.org/issue15881
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='o2x5xx',
    version='0.2',
    description='A Python library for ifm O2x5xx (O2D5xx / O2I5xx) devices',
    author='Michael Gann',
    author_email='support.efector.object-ident@ifm.com',
    license='MIT',
    packages=['o2x5xx', 'o2x5xx.device', 'o2x5xx.pcic', 'o2x5xx.rpc', 'o2x5xx.static'],
    package_dir={'o2x5xx': './source'},
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
    install_requires=[
        "numpy==1.26.0",
        "Pillow==10.0.1",
        "matplotlib==3.8.0",
        "setuptools==68.2.2",
        "pyodbc==4.0.34"
      ]
    )