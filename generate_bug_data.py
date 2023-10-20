import random
from faker import Faker
from bug_hub.models import Bug

# Create a Faker instance
fake = Faker()

# Define choices for bug_type and status fields
BUG_TYPE_CHOICES = [
    ("error", "Error"),
    ("feature", "Feature Request"),
    ("enhancement", "Enhancement"),
    ("documentation", "Documentation"),
]

STATUS_CHOICES = [
    ("todo", "To Do"),
    ("in_progress", "In Progress"),
    ("done", "Done"),
    ("under_review", "Under Review"),
    ("wont_fix", "Won't Fix"),
]


def generate_realistic_bug_data():
    description = fake.paragraphs(nb=3)
    bug_type, _ = random.choice(BUG_TYPE_CHOICES)
    status, _ = random.choice(STATUS_CHOICES)
    title = f"{bug_type.capitalize()} {status.replace('_', ' ')} Issue"

    bug = Bug(
        title=title,
        description=description,
        bug_type=bug_type,
        status=status,
    )
    bug.save()


def generate_realistic_bug_records(num_records):
    for _ in range(num_records):
        generate_realistic_bug_data()


generate_realistic_bug_records(10)
