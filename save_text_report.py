def save_text_report(content, filepath):
    """
    Save the provided text content into a file.
    """

    file = open(filepath, "w") # This opens the file in write mode , it also creates it if it doesnt alrady exist
    file.write(content) # writes the content string into the file
    file.close() # this will close the file and save all changes
