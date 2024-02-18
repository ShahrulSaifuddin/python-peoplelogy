def count_words(file_path):
    try:
        # Open the input file for reading
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Count the number of words
            word_count = len(content.split())

            # Open a new file for writing the word count
            with open('word_count.txt', 'w') as output_file:
                # Write the word count to the new file
                output_file.write(str(word_count))

            print(f"Word count: {word_count} words. Result saved to 'word_count.txt'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Replace 'input.txt' with the actual path to your input file
count_words('./helloworld.txt')
