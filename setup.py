#!/usr/bin/env python3

import distutils.core

distutils.core.setup(
    name='process_throttler',
    version='0.1',
    author='Xand Meaden',
    author_email='xand.meaden@kcl.ac.uk',
    url='https://github.com/kcl-nmssys/process_throttler',
    description='Throttler for CPU and memory-intensive user processes',
    scripts=['bin/process_throttler'],
    data_files=[('/etc/cron.d', ['etc/cron.d/process_throttler']), ('/etc', ['etc/process_throttler.yaml'])],
    options={'bdist_rpm': {'requires': 'python36,python36-PyYAML,python36-psutil'}}
)
