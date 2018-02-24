import os, sys
import prometheus_client
import argparse
from setuptools import setup, find_packages

setup(
    name = "process_status_exporter",
    version = "0.0.1",
    author = "wulixuan",
    author_email = "wulixuan@inspur.com",
    description = ("Process status exporter for Prometheus monitoring system."),
    long_description = ("See xxx"),
    license = "Apache Software License 2.0",
    keywords = "prometheus monitoring instrumentation process status exporter",
    url = "",
    packages = find_packages(),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License",
    ],
)