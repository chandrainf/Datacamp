'''
Fixture chaining using tmpdir

The built-in tmpdir fixture is very useful when dealing with files in setup and teardown. tmpdir combines seamlessly with user defined fixture via fixture chaining.

In this exercise, you will use the power of tmpdir to redefine and improve the empty_file() fixture that you wrote in the last exercise and get some experience with fixture chaining.

Instructions 1/2
50 XP

- Add the correct argument to the fixture empty_file() so that it chains with the built-in fixture tmpdir.
- Use the appropriate method to create an empty file "empty.txt" inside the temporary directory created by tmpdir.

'''
import pytest


@pytest.fixture
# Add the correct argument so that this fixture can chain with the tmpdir fixture
def empty_file(tmpdir):
    # Use the appropriate method to create an empty file in the temporary directory
    file_path = tmpdir.join("empty.txt")
    open(file_path, "w").close()
    yield file_path


'''

Instructions 2/2
50 XP
Question

In what order will the setup and teardown of empty_file() and tmpdir be executed?

Possible Answers :

    - setup of empty_file()  setup of tmpdir  teardown of tmpdir  teardown of empty_file().

    - setup of tmpdir  setup of empty_file()  teardown of empty_file()  teardown of tmpdir.

    - setup of tmpdir  setup of empty_file()  teardown of tmpdir  teardown of empty_file().

Answer : setup of tmpdir  setup of empty_file()  teardown of empty_file()  teardown of tmpdir.

'''
