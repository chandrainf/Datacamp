'''
Improving style guide compliancy


One of the reasons why Python is an easy language to get into, is because there’s a lot of similarity between code from different developers. That’s because the Python syntax relies on indents for scoping rules. Many developers follow the style guide of Python, known as PEP8.

In the project you've been building so far, you want to enforce that people follow the rules laid out in PEP8. You can do so with Flake8, which is a static code checker (it does not run your code). You run flake8 in the same way that you run pytest. It will show warnings and errors for code that is not compliant with PEP8.

In this exercise, you need to focus only on the ~/workspace/spark_pipelines/pydiaper.

Instructions
100XP

- Add flake8 to the development section in the Pipfile, which is in the project’s root folder. This file serves a similar purpose as the requirements.txt files you might have seen in other Python projects. It solves some problems with those though. To add flake8 correctly, look at the line that mentions pytest.
- Add flake8 to the .circleci/config.yml file, just before the line that tells CircleCI to run pytest. Make sure to duplicate the syntax of pipenv run. When you have done that, you can optionally execute flake8 from the shell in the project’s root folder with this command: pipenv run flake8. It will show you how many errors and warnings were generated. This is what CircleCI would automatically execute for you and it could stop executing subsequent steps, when this command generates errors, like in this case.

'''
# modified pydiaper/config.yml

version: 2
jobs:
    build:
        working_directory: ~/data_scientists/optimal_diapers/
        docker:
            - image: gcr.io/my-companys-container-registry-on-google-cloud-123456/python: 3.6.4
        steps:
            - checkout
            - run:
                command: |
                sudo pip install pipenv
                pipenv install
            - run:
                command: |
                pipenv run flake8 .
                pipenv run pytest .
            - store_test_results:
                path: test-results
            - store_artifacts:
                path: test-results
                destination: tr1
