# utils.py

import os
import logging

def setup_logging(log_file='app.log'):
    """Set up logging for the application."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger()
    return logger

def create_directory(directory_path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    else:
        print(f"Directory '{directory_path}' already exists.")

def save_to_file(content, file_path):
    """Save content to a file."""
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Content saved to '{file_path}'")

def read_from_file(file_path):
    """Read content from a file."""
    with open(file_path, 'r') as f:
        return f.read()

# Example usage (not included in the main script)
if __name__ == "__main__":
    # Setup logging
    logger = setup_logging()

    # Create a directory
    create_directory('../data/processed')

    # Save some content to a file
    content = "This is a test content."
    save_to_file(content, '../data/processed/test.txt')

    # Read the content from the file
    content = read_from_file('../data/processed/test.txt')
    print(content)
