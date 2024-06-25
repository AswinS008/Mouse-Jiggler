def modify_splunk_query(query, start_time, end_time):
    # Convert multiline string to single line by replacing newlines with spaces
    single_line_query = query.replace("\n", " ").replace("\r", " ")
    
    # Replace each single backslash with double backslashes
    modified_query = single_line_query.replace("\\", "\\\\")
    
    # The string to insert
    insert_str = f"earliest={start_time} Latest={end_time} "
    
    # Find the index of the first occurrence of "|"
    pipe_index = modified_query.find("|")
    
    # If there is a "|" in the string, insert the insert_str before it
    if pipe_index != -1:
        modified_query = modified_query[:pipe_index] + insert_str + modified_query[pipe_index:]
    
    return modified_query

# Define start_time and end_time
start_time = "2023-01-01T00:00:00"
end_time = "2023-01-01T23:59:59"

# Read input from the user until newline is encountered
print("Enter your Splunk query (press Enter to start processing):")
user_input = ""
while True:
    line = input()
    if line.strip() == "":
        break
    user_input += line + "\n"

# Modify the Splunk query
final_query = modify_splunk_query(user_input.strip(), start_time, end_time)
