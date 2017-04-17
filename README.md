# python-log-generator-cli

## Requirements:
You need to have the [Faker](https://pypi.python.org/pypi/Faker#downloads) python library installed to use this

## Usage:
On terminal within the directory of this repo:

    python generate_logs.py 5 test1.txt test2.txt

The command above will generate 5 new logs within the two files "test1.txt" and "test2.txt" in the same directory. The first argument after "python generate_logs.py" is the number of logs you want to generate. You can put any number of file paths after the first argument to put logs in those files.
