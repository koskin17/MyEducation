import random

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from faker import Faker

from profiles.models import Industry, InvestorProfile, Location, StartupProfile
from projects.models import ProjectRevision, SavedProject, StartupProject, Subscription
from users.models import UserProfile, UserRole


class Command(BaseCommand):
    help = "Populate database with fake data using Faker"

    def add_arguments(self, parser):
        parser.add_argument(
            "--users",
            type=int,
            default=10,
            help="Number of fake users to create (default: 10)",
        )
        parser.add_argument(
            "--investors",
            type=int,
            help="Number of investor profiles to create (default: half of users)",
        )
        parser.add_argument(
            "--startups",
            type=int,
            help="Number of startup profiles to create (default: half of users)",
        )
        parser.add_argument(
            "--projects",
            type=int,
            help="Number of startup projects to create (default: 1 per startup)",
        )
        parser.add_argument(
            "--saved-startups",
            type=int,
            help="Number of saved startup relationships to create (default: 1-3 per investor)",
        )
        parser.add_argument(
            "--subscriptions",
            type=int,
            help="Number of investment subscriptions to create (default: 1-3 per project)",
        )
        parser.add_argument(
            "--revisions",
            type=int,
            help="Number of project revisions to create (default: 1-2 per project)",
        )
        parser.add_argument(
            "--chat-rooms",
            type=int,
            help="Number of chat rooms to create (default: 0)",
        )
        parser.add_argument(
            "--chat-messages",
            type=int,
            help="Number of chat messages to create (default: 0)",
        )
        parser.add_argument(
            "--clear", action="store_true", help="Clear existing data before populating"
        )
        parser.add_argument(
            "--models",
            nargs="+",
            choices=[
                "users",
                "investors",
                "startups",
                "projects",
                "saved-projects",
                "subscriptions",
                "revisions",
                "chat-rooms",
                "chat-messages",
            ],
            help="Specific models to populate (default: all models)",
        )

    def validate_parameters(self, options):
        """Validate that the provided parameters make logical sense."""
        num_users = options["users"]
        num_investors = options.get("investors")
        num_startups = options.get("startups")
        num_projects = options.get("projects")
        num_saved = options.get("saved_startups")
        num_subscriptions = options.get("subscriptions")
        num_revisions = options.get("revisions")
        num_chat_rooms = options.get("chat_rooms")
        num_chat_messages = options.get("chat_messages")
        selected_models = options.get("models", [])

        errors = []

        # Validate investor/startup counts
        if num_investors is not None and num_startups is not None:
            if num_investors + num_startups != num_users:
                errors.append(
                    f"Total users ({num_users}) must equal investors ({num_investors}) + startups ({num_startups})"
                )
        elif num_investors is not None:
            if num_investors > num_users:
                errors.append(
                    f"Cannot create {num_investors} investors with only {num_users} users"
                )
        elif num_startups is not None:
            if num_startups > num_users:
                errors.append(
                    f"Cannot create {num_startups} startups with only {num_users} users"
                )

        # Note: Projects can be more than startups since they're distributed among startups

        # Validate saved startups count
        if num_saved is not None:
            max_possible_saved = (
                num_investors if num_investors is not None else num_users // 2
            )
            max_saved_per_investor = 3  # Each investor can save up to 3 startups
            max_possible_saved_total = max_possible_saved * max_saved_per_investor
            if num_saved > max_possible_saved_total:
                errors.append(
                    f"Cannot create {num_saved} saved relationships with only {max_possible_saved} investors "
                    f"(max {max_possible_saved_total} possible)"
                )

        # Validate subscriptions count
        if num_subscriptions is not None:
            max_possible_projects = (
                num_projects
                if num_projects is not None
                else num_startups if num_startups is not None else num_users // 2
            )
            max_subscriptions_per_project = (
                5  # Each project can have up to 5 subscriptions
            )
            max_possible_subscriptions = (
                max_possible_projects * max_subscriptions_per_project
            )
            if num_subscriptions > max_possible_subscriptions:
                errors.append(
                    f"Cannot create {num_subscriptions} subscriptions with only {max_possible_projects} projects "
                    f"(max {max_possible_subscriptions} possible)"
                )

        # Validate chat messages count
        if num_chat_messages is not None and num_chat_rooms is not None:
            if num_chat_rooms == 0 and num_chat_messages > 0:
                errors.append(
                    f"Cannot create {num_chat_messages} chat messages with 0 chat rooms"
                )

        # Validate model dependencies
        if selected_models:
            if "investors" in selected_models and "users" not in selected_models:
                errors.append("Cannot create investors without creating users first")
            if "startups" in selected_models and "users" not in selected_models:
                errors.append("Cannot create startups without creating users first")
            if "projects" in selected_models and "startups" not in selected_models:
                errors.append("Cannot create projects without creating startups first")
            if (
                "saved-projects" in selected_models
                and "projects" not in selected_models
            ):
                errors.append(
                    "Cannot create saved projects without creating projects first"
                )
            if (
                "saved-projects" in selected_models
                and "investors" not in selected_models
            ):
                errors.append(
                    "Cannot create saved projects without creating investors first"
                )
            if "subscriptions" in selected_models and "projects" not in selected_models:
                errors.append(
                    "Cannot create subscriptions without creating projects first"
                )
            if (
                "subscriptions" in selected_models
                and "investors" not in selected_models
            ):
                errors.append(
                    "Cannot create subscriptions without creating investors first"
                )
            if "revisions" in selected_models and "projects" not in selected_models:
                errors.append("Cannot create revisions without creating projects first")
            if "revisions" in selected_models and "users" not in selected_models:
                errors.append("Cannot create revisions without creating users first")
            if (
                "chat-messages" in selected_models
                and "chat-rooms" not in selected_models
            ):
                errors.append(
                    "Cannot create chat messages without creating chat rooms first"
                )
            if "chat-messages" in selected_models and "users" not in selected_models:
                errors.append(
                    "Cannot create chat messages without creating users first"
                )

        if errors:
            self.stdout.write(self.style.ERROR("Parameter validation errors:"))
            for error in errors:
                self.stdout.write(self.style.ERROR(f"  - {error}"))
            return False

        return True

    def clear_existing_data(self):
        """Clear all existing data in the correct order to avoid foreign key violations."""
        self.stdout.write("Clearing existing data...")
        try:
            # Delete dependent data in safe order
            ProjectRevision.objects.all().delete()
            Subscription.objects.all().delete()
            SavedProject.objects.all().delete()
            StartupProject.objects.all().delete()
            StartupProfile.objects.all().delete()
            InvestorProfile.objects.all().delete()
            # Clear users and roles
            UserProfile.objects.all().delete()
            UserRole.objects.all().delete()
            # Base lookup tables
            Industry.objects.all().delete()
            Location.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Existing data cleared."))
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(
                    f"Warning: Could not clear all existing data: {str(e)}"
                )
            )
            self.stdout.write(self.style.WARNING("Continuing with existing data..."))

    def setup_roles(self):
        """Create or get existing user roles."""
        self.stdout.write("Creating roles (investor and startup)...")
        roles = []
        role_names = ["investor", "startup"]

        for role_name in role_names:
            role, created = UserRole.objects.get_or_create(role=role_name)
            roles.append(role)
            if created:
                self.stdout.write(f"Created role: {role_name}")
            else:
                self.stdout.write(f"Role already exists: {role_name}")

        self.stdout.write(
            self.style.SUCCESS(f"Roles ready: {len(roles)} roles available.")
        )
        return roles

    def setup_lookup_tables(self):
        """Seed base lookup tables with predefined choices."""
        self.stdout.write("Seeding base lookup tables...")
        industry_values = [value for value, _ in Industry.INDUSTRY_CHOICES]
        location_values = [value for value, _ in Location.LOCATION_CHOICES]

        for name in industry_values:
            Industry.objects.get_or_create(name=name)
        for name in location_values:
            Location.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS("Base lookup tables are ready."))

    def create_users(self, num_users, num_investors, num_startups, roles):
        """Create users with specified distribution."""
        self.stdout.write(f"Creating {num_users} fake users...")
        fake = Faker()
        users_created = 0
        role_map = {r.role: r for r in roles}
        investor_users = []
        startup_users = []

        # Create investor users first
        for i in range(num_investors):
            try:
                user = self._create_single_user(fake, role_map["investor"])
                investor_users.append(user)
                users_created += 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating investor user {i+1}: {str(e)}")
                )

        # Create startup users
        for i in range(num_startups):
            try:
                user = self._create_single_user(fake, role_map["startup"])
                startup_users.append(user)
                users_created += 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating startup user {i+1}: {str(e)}")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {users_created} users!")
        )
        return investor_users, startup_users

    def _create_single_user(self, fake, role):
        """Create a single user with fake data."""
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        username = fake.unique.user_name()

        return UserProfile.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password("password123"),
            role=role,
            is_active=True,
            is_staff=random.choice([True, False]),
            is_superuser=False,
        )

    def create_investor_profiles(self, investor_users):
        """Create investor profiles for the given users."""
        if not investor_users:
            return []

        self.stdout.write(f"Creating {len(investor_users)} investor profiles...")
        fake = Faker()
        investor_profiles = []

        for user in investor_users:
            try:
                profile = InvestorProfile.objects.create(
                    user=user,
                    company_name=fake.company(),
                    website=fake.url(),
                )
                investor_profiles.append(profile)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error creating investor profile for {user.email}: {str(e)}"
                    )
                )

        return investor_profiles

    def create_startup_profiles(self, startup_users):
        """Create startup profiles for the given users."""
        if not startup_users:
            return []

        self.stdout.write(f"Creating {len(startup_users)} startup profiles...")
        fake = Faker()
        startup_profiles = []

        for user in startup_users:
            try:
                profile = StartupProfile.objects.create(
                    user=user,
                    company_name=fake.company(),
                    description=fake.paragraph(nb_sentences=3),
                    website=fake.url(),
                    views_count=random.randint(0, 5000),
                    industry=Industry.objects.order_by("?").first(),
                    location=Location.objects.order_by("?").first(),
                )
                startup_profiles.append(profile)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error creating startup profile for {user.email}: {str(e)}"
                    )
                )

        return startup_profiles

    def create_projects(self, startup_profiles, num_projects):
        """Create startup projects distributed among startups."""
        if not startup_profiles:
            return 0

        if num_projects:
            self.stdout.write(f"Creating {num_projects} startup projects...")
        else:
            self.stdout.write("Creating startup projects (1 per startup)...")
            num_projects = len(startup_profiles)

        fake = Faker()
        projects_created = 0

        # Distribute projects among startups
        projects_per_startup = num_projects // len(startup_profiles)
        extra_projects = num_projects % len(startup_profiles)

        for i, startup in enumerate(startup_profiles):
            projects_for_this_startup = projects_per_startup + (
                1 if i < extra_projects else 0
            )

            for _ in range(projects_for_this_startup):
                try:
                    project = StartupProject.objects.create(
                        subject=fake.catch_phrase(),
                        idea=fake.paragraph(nb_sentences=4),
                        description=fake.paragraph(nb_sentences=6),
                        website=fake.url(),
                        investment_needed=random.choice([True, False]),
                        views_count=random.randint(0, 10000),
                        status=random.choice(
                            [
                                StartupProject.Status.PENDING,
                                StartupProject.Status.FUNDED,
                            ]
                        ),
                        startup=startup,
                        investor=(
                            random.choice(InvestorProfile.objects.all())
                            if InvestorProfile.objects.exists()
                            and random.random() < 0.5
                            else None
                        ),
                        funding_goal=(
                            random.randint(10000, 1000000)
                            if random.random() < 0.7
                            else None
                        ),
                    )
                    projects_created += 1
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Could not create project for {startup.company_name}: {e}"
                        )
                    )

        self.stdout.write(self.style.SUCCESS(f"Created {projects_created} projects."))
        return projects_created

    def create_saved_projects(self, investor_profiles, num_saved):
        """Create saved project relationships."""
        if not investor_profiles:
            return 0

        if num_saved:
            self.stdout.write(f"Creating {num_saved} saved project relationships...")
        else:
            self.stdout.write("Creating saved projects (1-3 per investor)...")

        # Get all created projects
        all_projects = list(StartupProject.objects.all())
        if not all_projects:
            self.stdout.write(self.style.WARNING("No projects available to save."))
            return 0

        saved_created = 0

        if num_saved:
            # Distribute saved relationships among investors
            saved_per_investor = num_saved // len(investor_profiles)
            extra_saved = num_saved % len(investor_profiles)

            for i, investor in enumerate(investor_profiles):
                saved_for_this_investor = saved_per_investor + (
                    1 if i < extra_saved else 0
                )

                # Get random projects for this investor
                available_projects = list(all_projects)
                random.shuffle(available_projects)

                for project in available_projects[:saved_for_this_investor]:
                    if not SavedProject.objects.filter(
                        investor=investor, project=project
                    ).exists():
                        SavedProject.objects.create(investor=investor, project=project)
                        saved_created += 1

                        if saved_created >= num_saved:
                            break

                if saved_created >= num_saved:
                    break
        else:
            # Default behavior: each investor saves 0-3 random projects
            for investor in investor_profiles:
                if all_projects:
                    projects_to_save = random.sample(
                        all_projects, k=min(len(all_projects), random.randint(0, 3))
                    )
                    for project in projects_to_save:
                        if not SavedProject.objects.filter(
                            investor=investor, project=project
                        ).exists():
                            SavedProject.objects.create(
                                investor=investor, project=project
                            )
                            saved_created += 1

        self.stdout.write(
            self.style.SUCCESS(f"Created {saved_created} saved projects.")
        )
        return saved_created

    def create_subscriptions(self, num_subscriptions):
        """Create investment subscriptions for projects."""
        if not num_subscriptions:
            return 0

        self.stdout.write(f"Creating {num_subscriptions} investment subscriptions...")

        # Get all projects and investors
        all_projects = list(StartupProject.objects.all())
        all_investors = list(InvestorProfile.objects.all())

        if not all_projects:
            self.stdout.write(
                self.style.WARNING("No projects available for subscriptions.")
            )
            return 0

        if not all_investors:
            self.stdout.write(
                self.style.WARNING("No investors available for subscriptions.")
            )
            return 0

        subscriptions_created = 0

        # Distribute subscriptions among projects
        subscriptions_per_project = num_subscriptions // len(all_projects)
        extra_subscriptions = num_subscriptions % len(all_projects)

        for i, project in enumerate(all_projects):
            subscriptions_for_this_project = subscriptions_per_project + (
                1 if i < extra_subscriptions else 0
            )

            # Get random investors for this project
            available_investors = list(all_investors)
            random.shuffle(available_investors)

            for investor in available_investors[:subscriptions_for_this_project]:
                if not Subscription.objects.filter(
                    investor=investor, project=project
                ).exists():
                    # Generate realistic subscription amount (1-50% of funding goal)
                    if project.funding_goal:
                        max_share = min(
                            float(project.funding_goal) * 0.5, 100000
                        )  # Max 50% or 100k
                        share = random.randint(1000, int(max_share))
                    else:
                        share = random.randint(1000, 50000)

                    Subscription.objects.create(
                        investor=investor,
                        project=project,
                        share=share,
                    )
                    subscriptions_created += 1

                    if subscriptions_created >= num_subscriptions:
                        break

            if subscriptions_created >= num_subscriptions:
                break

        self.stdout.write(
            self.style.SUCCESS(f"Created {subscriptions_created} subscriptions.")
        )
        return subscriptions_created

    def create_project_revisions(self, num_revisions):
        """Create project revisions to track changes."""
        if not num_revisions:
            return 0

        self.stdout.write(f"Creating {num_revisions} project revisions...")

        # Get all projects and users
        all_projects = list(StartupProject.objects.all())
        all_users = list(UserProfile.objects.all())

        if not all_projects:
            self.stdout.write(
                self.style.WARNING("No projects available for revisions.")
            )
            return 0

        if not all_users:
            self.stdout.write(self.style.WARNING("No users available for revisions."))
            return 0

        revisions_created = 0

        # Distribute revisions among projects
        revisions_per_project = num_revisions // len(all_projects)
        extra_revisions = num_revisions % len(all_projects)

        for i, project in enumerate(all_projects):
            revisions_for_this_project = revisions_per_project + (
                1 if i < extra_revisions else 0
            )

            for _ in range(revisions_for_this_project):
                try:
                    # Generate fake revision changes
                    changes = {
                        "field": random.choice(
                            [
                                "subject",
                                "description",
                                "idea",
                                "website",
                                "funding_goal",
                            ]
                        ),
                        "old_value": f"Old {random.choice(['value', 'text', 'amount'])}",
                        "new_value": f"New {random.choice(['value', 'text', 'amount'])}",
                        "reason": random.choice(
                            [
                                "Updated project details",
                                "Corrected information",
                                "Added more details",
                                "Fixed typo",
                                "Updated funding goal",
                            ]
                        ),
                    }

                    ProjectRevision.objects.create(
                        project=project,
                        updated_by=random.choice(all_users),
                        changes=changes,
                    )
                    revisions_created += 1
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Could not create revision for {project.subject}: {e}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(f"Created {revisions_created} project revisions.")
        )
        return revisions_created

    def create_chat_rooms_and_messages(self, num_chat_rooms, num_chat_messages):
        """Create chat rooms and messages using MongoDB models."""
        if not num_chat_rooms and not num_chat_messages:
            return 0, 0

        try:
            from communications.mongo_models import Room, Message
        except ImportError:
            self.stdout.write(
                self.style.WARNING(
                    "MongoDB models not available. Skipping chat data creation."
                )
            )
            return 0, 0

        rooms_created = 0
        messages_created = 0
        fake = Faker()

        # Get all users
        all_users = list(UserProfile.objects.all())
        if not all_users:
            self.stdout.write(self.style.WARNING("No users available for chat rooms."))
            return 0, 0

        # Create chat rooms
        if num_chat_rooms:
            self.stdout.write(f"Creating {num_chat_rooms} chat rooms...")

            for i in range(num_chat_rooms):
                try:
                    # Create room with random participants
                    room_name = f"Room {fake.word().title()} {i+1}"
                    room = Room(name=room_name)

                    # Add 2-5 random participants
                    num_participants = random.randint(2, min(5, len(all_users)))
                    selected_users = random.sample(all_users, num_participants)

                    for user in selected_users:
                        room.add_participant(
                            user.id, user.username, user.first_name, user.last_name
                        )

                    room.save()
                    rooms_created += 1
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"Could not create chat room {i+1}: {e}")
                    )

            self.stdout.write(
                self.style.SUCCESS(f"Created {rooms_created} chat rooms.")
            )

        # Create chat messages
        if num_chat_messages and rooms_created > 0:
            self.stdout.write(f"Creating {num_chat_messages} chat messages...")

            all_rooms = list(Room.objects.all())
            if not all_rooms:
                self.stdout.write(
                    self.style.WARNING("No chat rooms available for messages.")
                )
                return rooms_created, 0

            # Distribute messages among rooms
            messages_per_room = num_chat_messages // len(all_rooms)
            extra_messages = num_chat_messages % len(all_rooms)

            for i, room in enumerate(all_rooms):
                messages_for_this_room = messages_per_room + (
                    1 if i < extra_messages else 0
                )

                for _ in range(messages_for_this_room):
                    try:
                        # Select a random participant from the room
                        if room.participants:
                            participant = random.choice(room.participants)

                            message = Message(
                                room=room,
                                sender_id=participant["id"],
                                sender_first_name=participant["first_name"],
                                sender_last_name=participant["last_name"],
                                text=fake.sentence(),
                                is_read=random.choice([True, False]),
                            )
                            message.save()
                            messages_created += 1
                    except Exception as e:
                        self.stdout.write(
                            self.style.WARNING(f"Could not create chat message: {e}")
                        )

            self.stdout.write(
                self.style.SUCCESS(f"Created {messages_created} chat messages.")
            )

        return rooms_created, messages_created

    def print_summary(self):
        """Print a summary of all created data."""
        total_users = UserProfile.objects.count()
        total_roles = UserRole.objects.count()
        total_investors = InvestorProfile.objects.count()
        total_startups = StartupProfile.objects.count()
        total_projects = StartupProject.objects.count()
        total_saved = SavedProject.objects.count()
        total_subscriptions = Subscription.objects.count()
        total_revisions = ProjectRevision.objects.count()

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDatabase population complete!\n"
                f"Total users: {total_users}\n"
                f"Total roles: {total_roles}\n"
                f"Investor profiles: {total_investors}\n"
                f"Startup profiles: {total_startups}\n"
                f"Projects: {total_projects}\n"
                f"Saved projects: {total_saved}\n"
                f"Subscriptions: {total_subscriptions}\n"
                f"Project revisions: {total_revisions}"
            )
        )

    def should_create_model(self, model_name, selected_models):
        """Check if a specific model should be created based on selected models."""
        if not selected_models:  # If no models specified, create all
            return True
        return model_name in selected_models

    def handle(self, *args, **options):
        # Validate parameters first
        if not self.validate_parameters(options):
            return

        num_users = options["users"]
        num_investors = options.get("investors")
        num_startups = options.get("startups")
        num_projects = options.get("projects")
        num_saved = options.get("saved_startups")
        num_subscriptions = options.get("subscriptions")
        num_revisions = options.get("revisions")
        num_chat_rooms = options.get("chat_rooms")
        num_chat_messages = options.get("chat_messages")
        clear_existing = options["clear"]
        selected_models = options.get("models", [])

        # Set defaults if not specified
        if num_investors is None and num_startups is None:
            num_investors = num_users // 2
            num_startups = num_users - num_investors
        elif num_investors is None:
            num_investors = num_users - num_startups
        elif num_startups is None:
            num_startups = num_users - num_investors

        self.stdout.write(
            self.style.SUCCESS(f"Starting to populate database with fake data...")
        )
        self.stdout.write(
            f"Configuration: {num_users} users ({num_investors} investors, {num_startups} startups)"
        )
        if num_projects:
            self.stdout.write(f"Projects: {num_projects}")
        if num_saved:
            self.stdout.write(f"Saved startups: {num_saved}")
        if num_subscriptions:
            self.stdout.write(f"Subscriptions: {num_subscriptions}")
        if num_revisions:
            self.stdout.write(f"Revisions: {num_revisions}")
        if num_chat_rooms:
            self.stdout.write(f"Chat rooms: {num_chat_rooms}")
        if num_chat_messages:
            self.stdout.write(f"Chat messages: {num_chat_messages}")
        if selected_models:
            self.stdout.write(f"Selected models: {', '.join(selected_models)}")

        # Clear existing data if requested
        if clear_existing:
            self.clear_existing_data()

        # Setup roles and lookup tables (always needed)
        roles = self.setup_roles()
        self.setup_lookup_tables()

        # Create users if requested
        investor_users = []
        startup_users = []
        if self.should_create_model("users", selected_models):
            investor_users, startup_users = self.create_users(
                num_users, num_investors, num_startups, roles
            )

        # Create investor profiles if requested
        investor_profiles = []
        if self.should_create_model("investors", selected_models):
            investor_profiles = self.create_investor_profiles(investor_users)

        # Create startup profiles if requested
        startup_profiles = []
        if self.should_create_model("startups", selected_models):
            startup_profiles = self.create_startup_profiles(startup_users)

        # Create projects if requested
        if self.should_create_model("projects", selected_models):
            self.create_projects(startup_profiles, num_projects)

        # Create saved projects if requested
        if self.should_create_model("saved-projects", selected_models):
            self.create_saved_projects(investor_profiles, num_saved)

        # Create subscriptions if requested
        if self.should_create_model("subscriptions", selected_models):
            self.create_subscriptions(num_subscriptions)

        # Create project revisions if requested
        if self.should_create_model("revisions", selected_models):
            self.create_project_revisions(num_revisions)

        # Create chat rooms and messages if requested
        if self.should_create_model(
            "chat-rooms", selected_models
        ) or self.should_create_model("chat-messages", selected_models):
            self.create_chat_rooms_and_messages(num_chat_rooms, num_chat_messages)

        # Print summary
        self.print_summary()
