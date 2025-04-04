def read_and_write_file():
    try:
        # Ask the user for a filename to read
        input_filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_filename, "r") as infile:
            content = infile.readlines()

        # Modify the content (example: convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Ask the user for an output filename
        output_filename = "modified_" + input_filename

        # Write to a new file
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Unable to read the file.")

# Run the function
read_and_write_file()
