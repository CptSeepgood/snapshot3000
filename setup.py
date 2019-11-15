from setuptools import setup

setup(
    name='snapshot3000',
    version='0.1',
    author="Jeremy Whittaker",
    author_email="jer.whittaker@gmail.com",
    description="Snapshot 3000 is a tool to manage AWS EC2 snapshots",
    package=['shotty'],
    url="https://github.com/CptSeepgood/snapshot3000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',


)
