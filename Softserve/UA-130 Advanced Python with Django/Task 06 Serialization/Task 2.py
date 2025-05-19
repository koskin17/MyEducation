# Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name") by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it). Use pretty printing for writing users to json-file.


# If the function cannot find input files we need to log information with error level  

# root - ERROR - File <file name> doesn't exist

# For example:
# user1.json : 
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# ]

# user2.json : 
# [{"name": "Bob1", "rate": 25, “languages": ["French"]},
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]