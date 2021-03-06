# Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#     http://www.apache.org/licenses/LICENSE-2.0
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import platform
from setuptools import setup, find_packages

pkgs = find_packages()
pkgs.append('tools')

# To build and upload a new version, follow the steps below.
# Notes:
# - this is a "Universal Wheels" package that is pure Python and supports both Python2 and Python3
# - Twine is a secure PyPi upload package
# - Make sure you have bumped the version!
# $ pip install twine
# $ pip install wheel
# $ python setup.py bdist_wheel --universal
# $ twine upload dist/*
requirements = ['Flask', 'Pillow', 'requests', 'flask-cors',
                'psutil', 'jsonschema', 'onnx-mxnet>=0.4.2', 'boto3', 'importlib2',
                'fasteners']
if platform.system().lower() == 'linux':
    requirements = ['mxnet-cu90mkl>=1.1'] + requirements
else:
    requirements = ['mxnet-mkl>=1.1'] + requirements
setup(
    name='mxnet-model-server',
    version='0.3',
    description='Model Server for Apache MXNet is a tool for serving neural net models for inference',
    url='https://github.com/awslabs/mxnet-model-server',
    keywords='MXNet Model Server Serving Deep Learning Inference AI',
    packages=pkgs,
    install_requires=requirements,
    entry_points={
        'console_scripts': ['mxnet-model-server=mms.mxnet_model_server:start_serving',
                            'mxnet-model-export=mms.export_model:export']
    },
    include_package_data=True,
    license='Apache License Version 2.0'
)
