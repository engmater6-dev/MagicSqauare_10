"""
Constants for MagicSquare entity layer.

This module defines all constants used in the entity layer to avoid hardcoding.
"""

# User entity constraints
MIN_USERNAME_LENGTH: int = 1
MAX_USERNAME_LENGTH: int = 50
MIN_EMAIL_LENGTH: int = 5
MAX_EMAIL_LENGTH: int = 100

# Email pattern for validation
EMAIL_PATTERN: str = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# User ID constraints
MIN_USER_ID: int = 1
MAX_USER_ID: int = 999999999
