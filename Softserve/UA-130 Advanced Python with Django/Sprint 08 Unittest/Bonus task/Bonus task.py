# 1. Create users and subjects data from files

# get_subjects_from_json(subjects_json) -> List[Subject]

# get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]

# 2. Simulate working with the application

# method User.create_user(username, password, role) creates user

# method user.add_score_for_subject(subject:Subject, score: Score) adds score for subject

# function add_user(user, users) adds user to users (in case of uniqueness username)

# function add_subject(subject, subjects) adds subject to subjects (in case of uniqueness title)

# function get_grades_for_user(username:str, user:User, users:list) returns all grades for the user with username (only own grades or for mentor)

# 3. Rewrite the old json-files with new ones

# users_to_json(users, json_file)

# subjects_to_json(subjects, json_file)

# grades_to_json(users, subjects, json_file)