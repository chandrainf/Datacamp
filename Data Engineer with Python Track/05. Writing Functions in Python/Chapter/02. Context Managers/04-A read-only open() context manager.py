'''
A read-only open() context manager


You have a bunch of data files for your next deep learning project that took you months to collect and clean. It would be terrible if you accidentally overwrote one of those files when trying to read it in for training, so you decide to create a read-only version of the open() context manager to use in your project.

The regular open() context manager:

    - takes a filename and a mode ('r' for read, 'w' for write, or 'a' for append)
    - opens the file for reading, writing, or appending
    - yields control back to the context, along with a reference to the file
    - waits for the context to finish
    - and then closes the file before exiting

Your context manager will do the same thing, except it will only take the filename as an argument and it will only open the file for reading.

Instructions
100 XP

- Yield control from open_read_only() to the context block, ensuring that the read_only_file object gets assigned to my_file.
- Use read_only_file's .close() method to ensure that you don't leave open files lying around.

'''
@contextlib.contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.
    Args:
      filename (str): The location of the file to read
    Yields:
      file object
    """
    read_only_file = open(filename, mode='r')
    # Yield read_only_file so it can be assigned to my_file
    yield read_only_file
    # Close read_only_file
    read_only_file.close()


with open_read_only('my_file.txt') as my_file:
    print(my_file.read())
