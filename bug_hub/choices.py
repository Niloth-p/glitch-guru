"""
Choice Sets for Bug Types and Statuses

This module fixes predefined options for specifying bug types and statuses used in the Bug model.

Choice Sets:
***********

- `BUG_TYPE_CHOICES` (list of tuple): Choice set for bug types.
    - "error": Error
    - "feature": Feature Request
    - "enhancement": Enhancement
    - "documentation": Documentation

- `STATUS_CHOICES` (list of tuple): Choice set for bug statuses.
    - "todo": To Do
    - "in_progress": In Progress
    - "under_review": Under Review
    - "done": Done
    - "wont_fix": Won't Fix
"""

BUG_TYPE_CHOICES = [
    ("error", "Error"),
    ("feature", "Feature Request"),
    ("enhancement", "Enhancement"),
    ("documentation", "Documentation"),
]

STATUS_CHOICES = [
    ("todo", "To Do"),
    ("in_progress", "In Progress"),
    ("under_review", "Under Review"),
    ("done", "Done"),
    ("wont_fix", "Won't Fix"),
]
