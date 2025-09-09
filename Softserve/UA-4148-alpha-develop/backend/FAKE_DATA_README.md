# Database Population with Fake Data

This project includes a Django management command to populate the database with fake data using the [Faker](https://pypi.org/project/Faker/) library.

## Prerequisites

Make sure you have installed the Faker library:

```bash
pip install Faker==37.5.3
```

## Usage

### Django Management Command

You can use the Django management command to populate the database:

```bash
# Navigate to the backend directory
cd UA-4148-alpha/backend

# Run the management command with default settings (10 users)
python manage.py populate_fake_data

# Run with custom number of users
python manage.py populate_fake_data --users 100

# Specify exact number of investors and startups
python manage.py populate_fake_data --users 20 --investors 8 --startups 12

# Create specific number of projects and saved relationships
python manage.py populate_fake_data --users 10 --projects 15 --saved-startups 25

# Create investment subscriptions and project revisions
python manage.py populate_fake_data --users 10 --subscriptions 20 --revisions 15

# Create chat rooms and messages
python manage.py populate_fake_data --users 10 --chat-rooms 5 --chat-messages 50

# Clear existing data before populating
python manage.py populate_fake_data --clear

# Combine all options
python manage.py populate_fake_data --users 50 --investors 20 --startups 30 --projects 40 --saved-startups 60 --subscriptions 80 --revisions 30 --chat-rooms 10 --chat-messages 100 --clear

# Populate only specific models
python manage.py populate_fake_data --models users investors
python manage.py populate_fake_data --models startups projects subscriptions
python manage.py populate_fake_data --models users startups projects subscriptions revisions --users 20 --projects 10 --subscriptions 30 --revisions 15
```

## Command Line Options

The command supports the following options:

- `--users`: Number of fake users to create (default: 10)
- `--investors`: Number of investor profiles to create (default: half of users)
- `--startups`: Number of startup profiles to create (default: half of users)
- `--projects`: Number of startup projects to create (default: 1 per startup)
- `--saved-startups`: Number of saved project relationships to create (default: 1-3 per investor)
- `--subscriptions`: Number of investment subscriptions to create (default: 1-3 per project)
- `--revisions`: Number of project revisions to create (default: 1-2 per project)
- `--chat-rooms`: Number of chat rooms to create (default: 0)
- `--chat-messages`: Number of chat messages to create (default: 0)
- `--clear`: Clear existing data before populating (optional flag)
- `--models`: Specific models to populate (choices: users, investors, startups, projects, saved-projects, subscriptions, revisions, chat-rooms, chat-messages)

## Selective Model Population

The `--models` parameter allows you to populate only specific models instead of all models at once. This is more convenient than setting parameters to 0.

### Available Models:
- `users`: Create user accounts with roles
- `investors`: Create investor profiles (requires users)
- `startups`: Create startup profiles (requires users)
- `projects`: Create startup projects (requires startups)
- `saved-projects`: Create saved project relationships (requires projects and investors)
- `subscriptions`: Create investment subscriptions (requires projects and investors)
- `revisions`: Create project revisions (requires projects and users)
- `chat-rooms`: Create chat rooms (requires users)
- `chat-messages`: Create chat messages (requires chat rooms and users)

### Examples:

```bash
# Create only users and investors
python manage.py populate_fake_data --models users investors --users 10

# Create only startups and their projects
python manage.py populate_fake_data --models users startups projects --users 20 --projects 15

# Create investment subscriptions for existing projects
python manage.py populate_fake_data --models subscriptions --subscriptions 50

# Create project revisions for existing projects
python manage.py populate_fake_data --models revisions --revisions 20

# Create chat functionality
python manage.py populate_fake_data --models users chat-rooms chat-messages --users 10 --chat-rooms 3 --chat-messages 30

# Create everything except chat
python manage.py populate_fake_data --models users investors startups projects saved-projects subscriptions revisions --users 10
```

### Model Dependencies:
The command automatically validates dependencies:
- `investors` requires `users`
- `startups` requires `users`
- `projects` requires `startups`
- `saved-projects` requires both `projects` and `investors`
- `subscriptions` requires both `projects` and `investors`
- `revisions` requires both `projects` and `users`
- `chat-rooms` requires `users`
- `chat-messages` requires both `chat-rooms` and `users`

## Parameter Validation

The command includes intelligent validation to ensure your parameters make logical sense:

### User Distribution Validation
- If you specify both `--investors` and `--startups`, their sum must equal `--users`
- If you specify only one of them, the other will be calculated automatically
- You cannot create more investors or startups than the total number of users

### Project Validation
- Projects are distributed evenly among available startups
- You can create more projects than startups (they'll be distributed)

### Saved Relationships Validation
- You cannot create more saved relationships than possible (max 3 per investor)
- Saved relationships are distributed evenly among available investors

### Subscription Validation
- You cannot create more subscriptions than possible (max 5 per project)
- Subscriptions are distributed evenly among available projects
- Subscription amounts are realistic (1-50% of project funding goal)

### Chat Validation
- You cannot create chat messages without chat rooms
- Chat messages are distributed evenly among available rooms

### Model Dependency Validation
- Cannot create dependent models without their prerequisites
- Clear error messages explain what's missing

### Example Validation Errors
```bash
# This will fail: 10 users but 15 investors
python manage.py populate_fake_data --users 10 --investors 15

# This will fail: 2 investors but 10 saved relationships (max 6 possible)
python manage.py populate_fake_data --users 10 --investors 2 --saved-startups 10

# This will fail: trying to create investors without users
python manage.py populate_fake_data --models investors

# This will fail: trying to create subscriptions without projects
python manage.py populate_fake_data --models subscriptions

# This will fail: trying to create chat messages without rooms
python manage.py populate_fake_data --models chat-messages --chat-rooms 0 --chat-messages 10
```

## What Data is Created

### User Roles
The command ensures that the two required roles exist:
1. investor
2. startup

These roles are created if they don't exist, or reused if they already exist.

### Base Lookup Tables
The script creates predefined choices for:
1. **Industry**: "category 1" through "category 8"
2. **Location**: Ukrainian oblasts (Kyiv Oblast, Lviv Oblast, etc.)

### User Profiles
For each user, the script creates:
- **Username**: Unique username generated by Faker
- **Email**: Unique email address
- **First Name**: Random first name
- **Last Name**: Random last name
- **Password**: All users get the default password `password123` (hashed)
- **Role**: Assigned based on your investor/startup distribution
- **Staff Status**: Randomly assigned (True/False)
- **Active Status**: Always True
- **Superuser Status**: Always False

### Profile Extensions
Based on the user's role, additional profile data is created:

#### Startup Profiles
- **Company Name**: Random company name
- **Description**: Random paragraph describing the startup
- **Website**: Random URL
- **Views Count**: Random number (0-5000)
- **Industry**: Randomly assigned from predefined choices
- **Location**: Randomly assigned from predefined choices

#### Investor Profiles
- **Company Name**: Random company name
- **Website**: Random URL

### Startup Projects
For each startup profile, the script creates:
- **Subject**: Random catch phrase
- **Idea**: Random paragraph describing the project idea
- **Description**: Random paragraph with project details
- **Website**: Random URL
- **Investment Needed**: Random boolean
- **Views Count**: Random number (0-10000)
- **Status**: Randomly assigned from "PENDING" or "FUNDED"
- **Investor**: Randomly assigned investor (50% chance)
- **Funding Goal**: Random amount between $10,000 and $1,000,000 (70% chance)

### Saved Projects
The script creates bookmark relationships:
- Each investor saves 0-3 random projects (or specified number)
- Prevents duplicate saves for the same investor-project pair

### Investment Subscriptions
The script creates investment subscriptions:
- Each project can have multiple investor subscriptions
- Subscription amounts are realistic (1-50% of project funding goal)
- Prevents duplicate subscriptions for the same investor-project pair
- Subscription amounts range from $1,000 to $100,000

### Project Revisions
The script creates project revision history:
- Tracks changes to project fields (subject, description, idea, website, funding_goal)
- Records who made the changes and when
- Includes realistic change reasons and values
- Useful for auditing and tracking project evolution

### Chat Rooms and Messages
The script creates chat functionality (MongoDB):
- **Chat Rooms**: Named rooms with 2-5 random participants
- **Chat Messages**: Messages sent by room participants
- **Message Properties**: Text content, sender info, read status, timestamps
- **Realistic Data**: Natural conversation flow and participant interactions

## Database Models Populated

The scripts populate the following models:

### Users App
1. **UserRole**: Contains role names for user categorization
2. **UserProfile**: Contains user account information (extends Django's AbstractUser)

### Profiles App
3. **Industry**: Predefined industry categories
4. **Location**: Predefined Ukrainian oblasts
5. **StartupProfile**: Extended profile for startup users
6. **InvestorProfile**: Extended profile for investor users

### Projects App
7. **StartupProject**: Projects created by startups (with embedded Status enum)
8. **SavedProject**: Bookmark relationships between investors and projects
9. **Subscription**: Investment subscriptions with amounts
10. **ProjectRevision**: Project change history and audit trail

### Communications App (MongoDB)
11. **Room**: Chat rooms with participants
12. **Message**: Chat messages within rooms

## Usage Examples

### Basic Usage
```bash
# Create 10 users with all related data (default distribution)
python manage.py populate_fake_data
```

### Custom User Distribution
```bash
# Create 20 users: 8 investors, 12 startups
python manage.py populate_fake_data --users 20 --investors 8 --startups 12

# Create 15 users: 10 investors, 5 startups
python manage.py populate_fake_data --users 15 --investors 10 --startups 5
```

### Custom Project and Relationship Counts
```bash
# Create 10 users with 20 projects and 30 saved relationships
python manage.py populate_fake_data --users 10 --projects 20 --saved-startups 30

# Create 50 users with 100 projects
python manage.py populate_fake_data --users 50 --projects 100
```

### Investment and Revision Data
```bash
# Create investment subscriptions
python manage.py populate_fake_data --users 10 --projects 15 --subscriptions 50

# Create project revisions
python manage.py populate_fake_data --users 10 --projects 15 --revisions 30

# Create both subscriptions and revisions
python manage.py populate_fake_data --users 10 --projects 15 --subscriptions 50 --revisions 30
```

### Chat Functionality
```bash
# Create chat rooms only
python manage.py populate_fake_data --users 10 --chat-rooms 5

# Create chat rooms and messages
python manage.py populate_fake_data --users 10 --chat-rooms 5 --chat-messages 100

# Create comprehensive chat data
python manage.py populate_fake_data --users 20 --chat-rooms 10 --chat-messages 200
```

### Selective Model Population
```bash
# Create only users and investors
python manage.py populate_fake_data --models users investors --users 10

# Create only startups and projects
python manage.py populate_fake_data --models users startups projects --users 20 --projects 15

# Create investment data for existing projects
python manage.py populate_fake_data --models subscriptions --subscriptions 50

# Create revision history for existing projects
python manage.py populate_fake_data --models revisions --revisions 20

# Create chat functionality
python manage.py populate_fake_data --models users chat-rooms chat-messages --users 10 --chat-rooms 3 --chat-messages 30
```

### Development Environment
```bash
# Create 200 users for testing
python manage.py populate_fake_data --users 200
```

### Reset and Repopulate
```bash
# Clear all existing data and create fresh fake data
python manage.py populate_fake_data --clear
```

### Production-like Data
```bash
# Create a large dataset for performance testing
python manage.py populate_fake_data --users 1000 --projects 2000 --saved-startups 3000 --subscriptions 5000 --revisions 1000 --chat-rooms 50 --chat-messages 5000
```

## Data Relationships

The script maintains proper relationships between all models:
- Users are assigned roles (investor/startup) based on your specifications
- Startup users get StartupProfile with Industry and Location
- Investor users get InvestorProfile
- StartupProjects are linked to StartupProfile and optionally InvestorProfile
- SavedProject creates many-to-many relationships between investors and projects
- Subscription creates investment relationships with amounts
- ProjectRevision tracks changes made by users to projects
- Chat rooms contain multiple participants and messages
- Projects and saved relationships are distributed evenly among available entities

## Smart Distribution

The script intelligently distributes data:
- **Projects**: If you specify more projects than startups, they're distributed evenly
- **Saved Relationships**: If you specify more saved relationships than possible, they're distributed among investors
- **Subscriptions**: If you specify more subscriptions than possible, they're distributed among projects
- **Revisions**: If you specify more revisions than possible, they're distributed among projects
- **Chat Messages**: If you specify more messages than possible, they're distributed among rooms
- **Validation**: Prevents impossible combinations and provides clear error messages

## Code Structure

The command is well-structured with the following functions:

### Core Functions:
- `validate_parameters()`: Validates all input parameters and dependencies
- `clear_existing_data()`: Safely clears existing data in correct order
- `setup_roles()`: Creates or gets existing user roles
- `setup_lookup_tables()`: Seeds base lookup tables with predefined choices

### Data Creation Functions:
- `create_users()`: Creates users with specified distribution
- `create_investor_profiles()`: Creates investor profiles for users
- `create_startup_profiles()`: Creates startup profiles for users
- `create_projects()`: Creates projects distributed among startups
- `create_saved_projects()`: Creates saved project relationships
- `create_subscriptions()`: Creates investment subscriptions
- `create_project_revisions()`: Creates project revision history
- `create_chat_rooms_and_messages()`: Creates chat functionality

### Helper Functions:
- `_create_single_user()`: Creates a single user with fake data
- `should_create_model()`: Determines if a model should be created based on selection
- `print_summary()`: Prints a summary of all created data

### Main Function:
- `handle()`: Orchestrates the entire process

This modular structure makes the code:
- **Maintainable**: Each function has a single responsibility
- **Testable**: Individual functions can be tested in isolation
- **Readable**: Clear function names and documentation
- **Extensible**: Easy to add new models or modify existing ones

## Notes

- All users have the password `password123` for easy testing
- Email addresses and usernames are guaranteed to be unique
- The command provides progress indicators and configuration summary
- Error handling is included to continue processing even if individual creation fails
- The command is safe to run multiple times (unless using `--clear`)
- Roles and lookup tables are automatically created if they don't exist, or reused if they already exist
- The `--clear` option safely deletes data in the correct order to avoid foreign key constraint violations
- Parameter validation prevents logical errors and provides helpful error messages
- Project status is now handled via an embedded enum (PENDING/FUNDED) instead of a separate model
- Saved relationships now link investors to projects instead of startups
- The `--models` parameter provides a convenient way to populate only specific models
- Model dependencies are automatically validated to prevent errors
- Subscription amounts are realistic and based on project funding goals
- Project revisions include realistic change tracking and audit information
- Chat functionality uses MongoDB models for better performance
- All new models include comprehensive validation and error handling

## Troubleshooting

If you encounter issues:

1. Make sure Django is properly configured and the database is accessible
2. Verify that all apps (`users`, `profiles`, `projects`, `communications`) are in `INSTALLED_APPS` in your Django settings
3. Ensure all migrations have been applied: `python manage.py migrate`
4. Check that the Faker library is installed: `pip install Faker==37.5.3`
5. For Docker environments, use: `docker-compose run --rm web python manage.py populate_fake_data`
6. If you get validation errors, check that your parameter combinations make logical sense
7. When using `--models`, ensure all required dependencies are included
8. For chat functionality, ensure MongoDB is running and accessible
9. For subscription creation, ensure projects have funding goals set
10. For revision creation, ensure both projects and users exist

