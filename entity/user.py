"""
User entity class for MagicSquare project.

This module defines the User entity which represents a user in the system.
It contains domain data and rules specific to users, following the ECB pattern.
"""

import re
from datetime import datetime
from typing import Dict, Any
from entity.constants import (
    MIN_USERNAME_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_EMAIL_LENGTH,
    MAX_EMAIL_LENGTH,
    EMAIL_PATTERN,
    MIN_USER_ID,
    MAX_USER_ID,
)


class InvalidUserError(Exception):
    """Exception raised when user validation fails."""
    pass


class User:
    """
    Represents a user in the MagicSquare system.
    
    This entity class encapsulates user data and validation rules.
    Following the ECB (Entity-Control-Boundary) pattern, this class
    only handles domain data and business rules for users.
    
    Attributes:
        user_id: Unique identifier for the user.
        name: User's name or username.
        email: User's email address.
        created_at: Timestamp when the user was created.
    
    Raises:
        InvalidUserError: If user data fails validation.
    """

    def __init__(
        self,
        user_id: int,
        name: str,
        email: str,
        created_at: datetime | None = None,
    ) -> None:
        """
        Initialize a new User instance.
        
        Args:
            user_id: Unique identifier for the user (between MIN_USER_ID and MAX_USER_ID).
            name: User's name or username.
            email: User's email address.
            created_at: Timestamp when the user was created. If None, uses current datetime.
        
        Raises:
            InvalidUserError: If any parameter fails validation.
        """
        self._user_id: int = user_id
        self._name: str = name
        self._email: str = email
        self._created_at: datetime = created_at or datetime.now()
        
        self.validate()

    def validate(self) -> None:
        """
        Validate all user attributes according to domain rules.
        
        Checks:
        - user_id is within valid range
        - name length is within valid range
        - email length is within valid range
        - email format is valid
        
        Raises:
            InvalidUserError: If any validation check fails.
        """
        self._validate_user_id()
        self._validate_name()
        self._validate_email()

    def _validate_user_id(self) -> None:
        """
        Validate user ID is within acceptable range.
        
        Raises:
            InvalidUserError: If user_id is out of range.
        """
        if not isinstance(self._user_id, int):
            raise InvalidUserError("user_id must be an integer")
        
        if self._user_id < MIN_USER_ID or self._user_id > MAX_USER_ID:
            raise InvalidUserError(
                f"user_id must be between {MIN_USER_ID} and {MAX_USER_ID}, "
                f"got {self._user_id}"
            )

    def _validate_name(self) -> None:
        """
        Validate name length is within acceptable range.
        
        Raises:
            InvalidUserError: If name length is invalid.
        """
        if not isinstance(self._name, str):
            raise InvalidUserError("name must be a string")
        
        name_length = len(self._name)
        if name_length < MIN_USERNAME_LENGTH or name_length > MAX_USERNAME_LENGTH:
            raise InvalidUserError(
                f"name length must be between {MIN_USERNAME_LENGTH} and "
                f"{MAX_USERNAME_LENGTH}, got {name_length}"
            )

    def _validate_email(self) -> None:
        """
        Validate email format and length.
        
        Raises:
            InvalidUserError: If email format or length is invalid.
        """
        if not isinstance(self._email, str):
            raise InvalidUserError("email must be a string")
        
        email_length = len(self._email)
        if email_length < MIN_EMAIL_LENGTH or email_length > MAX_EMAIL_LENGTH:
            raise InvalidUserError(
                f"email length must be between {MIN_EMAIL_LENGTH} and "
                f"{MAX_EMAIL_LENGTH}, got {email_length}"
            )
        
        if not re.match(EMAIL_PATTERN, self._email):
            raise InvalidUserError(f"email format is invalid: {self._email}")

    @property
    def user_id(self) -> int:
        """
        Get the user's unique identifier.
        
        Returns:
            The user's ID.
        """
        return self._user_id

    @property
    def name(self) -> str:
        """
        Get the user's name.
        
        Returns:
            The user's name.
        """
        return self._name

    @property
    def email(self) -> str:
        """
        Get the user's email address.
        
        Returns:
            The user's email address.
        """
        return self._email

    @property
    def created_at(self) -> datetime:
        """
        Get the user's creation timestamp.
        
        Returns:
            The datetime when the user was created.
        """
        return self._created_at

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert user to dictionary representation.
        
        Returns:
            Dictionary containing all user attributes.
        """
        return {
            "user_id": self._user_id,
            "name": self._name,
            "email": self._email,
            "created_at": self._created_at.isoformat(),
        }

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another User instance.
        
        Args:
            other: Object to compare with.
        
        Returns:
            True if both users have the same user_id, False otherwise.
        """
        if not isinstance(other, User):
            return NotImplemented
        return self._user_id == other._user_id

    def __str__(self) -> str:
        """
        Get string representation of user.
        
        Returns:
            String containing user name and email.
        """
        return f"User(id={self._user_id}, name='{self._name}', email='{self._email}')"

    def __repr__(self) -> str:
        """
        Get detailed string representation of user.
        
        Returns:
            Detailed string representation for debugging.
        """
        return (
            f"User(user_id={self._user_id}, name='{self._name}', "
            f"email='{self._email}', created_at={self._created_at})"
        )
