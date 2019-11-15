# snapshot3000
acloud guru project


## About

this is a demo that uses boto3 to manage aws ec2 instance snapshots.

## Configure

shotty uses the configuration file created by the AWS cli e.g.

'aws configure --profile shotty'

## running

'pipenv run python shotty/shotty.py <command> <--project=PROJECT>'

*command* is instances, volumes, or snapshots
*subcommand* - depends in command
*project* is optional
