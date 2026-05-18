"""
Test suite for User entity class.

This module contains comprehensive tests for the User entity following
the TDD (Test-Driven Development) approach with AAA pattern (Arrange-Act-Assert).
"""

import pytest
from datetime import datetime
from entity.user import User, InvalidUserError
from entity.constants import (
    MIN_USERNAME_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_EMAIL_LENGTH,
    MAX_EMAIL_LENGTH,
    MIN_USER_ID,
    MAX_USER_ID,
)


class TestUserInitialization:
    """Tests for User initialization."""

    def test_user_creation_with_valid_data(self) -> None:
        """
        Test creating a user with valid data.
        
        Arrange: Prepare valid user data
        Act: Create a User instance
        Assert: User is created successfully with correct attributes
        """
        # Arrange
        user_id = 1
        name = "John Doe"
        email = "john@example.com"
        
        # Act
        user = User(user_id=user_id, name=name, email=email)
        
        # Assert
        assert user.user_id == user_id
        assert user.name == name
        assert user.email == email
        assert isinstance(user.created_at, datetime)

    def test_user_creation_with_custom_created_at(self) -> None:
        """
        Test creating a user with custom created_at timestamp.
        
        Arrange: Prepare user data with specific timestamp
        Act: Create a User instance with created_at
        Assert: User creation time matches the provided timestamp
        """
        # Arrange
        user_id = 1
        name = "Jane Doe"
        email = "jane@example.com"
        custom_time = datetime(2023, 1, 1, 12, 0, 0)
        
        # Act
        user = User(
            user_id=user_id,
            name=name,
            email=email,
            created_at=custom_time,
        )
        
        # Assert
        assert user.created_at == custom_time


class TestUserValidationUserID:
    """Tests for user_id validation."""

    def test_user_id_below_minimum(self) -> None:
        """
        Test that InvalidUserError is raised when user_id is below minimum.
        
        Arrange: Prepare user data with user_id below MIN_USER_ID
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_user_id = MIN_USER_ID - 1
        
        # Act & Assert
        with pytest.raises(
            InvalidUserError,
            match=f"user_id must be between {MIN_USER_ID} and {MAX_USER_ID}",
        ):
            User(user_id=invalid_user_id, name="Test", email="test@example.com")

    def test_user_id_above_maximum(self) -> None:
        """
        Test that InvalidUserError is raised when user_id is above maximum.
        
        Arrange: Prepare user data with user_id above MAX_USER_ID
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_user_id = MAX_USER_ID + 1
        
        # Act & Assert
        with pytest.raises(
            InvalidUserError,
            match=f"user_id must be between {MIN_USER_ID} and {MAX_USER_ID}",
        ):
            User(user_id=invalid_user_id, name="Test", email="test@example.com")

    def test_user_id_not_integer(self) -> None:
        """
        Test that InvalidUserError is raised when user_id is not an integer.
        
        Arrange: Prepare user data with non-integer user_id
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange & Act & Assert
        with pytest.raises(InvalidUserError, match="user_id must be an integer"):
            User(user_id="1", name="Test", email="test@example.com")  # type: ignore


class TestUserValidationName:
    """Tests for name validation."""

    def test_name_too_short(self) -> None:
        """
        Test that InvalidUserError is raised when name is too short.
        
        Arrange: Prepare user data with empty name
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_name = ""
        
        # Act & Assert
        with pytest.raises(
            InvalidUserError,
            match=f"name length must be between {MIN_USERNAME_LENGTH} and "
                  f"{MAX_USERNAME_LENGTH}",
        ):
            User(user_id=1, name=invalid_name, email="test@example.com")

    def test_name_too_long(self) -> None:
        """
        Test that InvalidUserError is raised when name exceeds maximum length.
        
        Arrange: Prepare user data with name longer than MAX_USERNAME_LENGTH
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_name = "a" * (MAX_USERNAME_LENGTH + 1)
        
        # Act & Assert
        with pytest.raises(
            InvalidUserError,
            match=f"name length must be between {MIN_USERNAME_LENGTH} and "
                  f"{MAX_USERNAME_LENGTH}",
        ):
            User(user_id=1, name=invalid_name, email="test@example.com")

    def test_name_not_string(self) -> None:
        """
        Test that InvalidUserError is raised when name is not a string.
        
        Arrange: Prepare user data with non-string name
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange & Act & Assert
        with pytest.raises(InvalidUserError, match="name must be a string"):
            User(user_id=1, name=123, email="test@example.com")  # type: ignore


class TestUserValidationEmail:
    """Tests for email validation."""

    def test_email_invalid_format(self) -> None:
        """
        Test that InvalidUserError is raised for invalid email format.
        
        Arrange: Prepare user data with invalid email format
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_email = "notanemail"
        
        # Act & Assert
        with pytest.raises(InvalidUserError, match="email format is invalid"):
            User(user_id=1, name="Test", email=invalid_email)

    def test_email_too_short(self) -> None:
        """
        Test that InvalidUserError is raised when email is too short.
        
        Arrange: Prepare user data with very short email
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_email = "a@b"
        
        # Act & Assert
        with pytest.raises(
            InvalidUserError,
            match=f"email length must be between {MIN_EMAIL_LENGTH} and "
                  f"{MAX_EMAIL_LENGTH}",
        ):
            User(user_id=1, name="Test", email=invalid_email)

    def test_email_too_long(self) -> None:
        """
        Test that InvalidUserError is raised when email exceeds maximum length.
        
        Arrange: Prepare user data with email longer than MAX_EMAIL_LENGTH
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange
        invalid_email = "a" * (MAX_EMAIL_LENGTH - 10) + "@example.com"
        
        # Act & Assert
        with pytest.raises(
            InvalidUserError,
            match=f"email length must be between {MIN_EMAIL_LENGTH} and "
                  f"{MAX_EMAIL_LENGTH}",
        ):
            User(user_id=1, name="Test", email=invalid_email)

    def test_email_not_string(self) -> None:
        """
        Test that InvalidUserError is raised when email is not a string.
        
        Arrange: Prepare user data with non-string email
        Act: Attempt to create a User
        Assert: InvalidUserError is raised with appropriate message
        """
        # Arrange & Act & Assert
        with pytest.raises(InvalidUserError, match="email must be a string"):
            User(user_id=1, name="Test", email=12345)  # type: ignore


class TestUserProperties:
    """Tests for User property accessors."""

    @pytest.fixture
    def valid_user(self) -> User:
        """Fixture providing a valid User instance."""
        return User(user_id=1, name="Test User", email="test@example.com")

    def test_user_id_property(self, valid_user: User) -> None:
        """
        Test that user_id property returns correct value.
        
        Arrange: Create a valid user
        Act: Access user_id property
        Assert: Returned value matches the user's ID
        """
        # Act & Assert
        assert valid_user.user_id == 1

    def test_name_property(self, valid_user: User) -> None:
        """
        Test that name property returns correct value.
        
        Arrange: Create a valid user
        Act: Access name property
        Assert: Returned value matches the user's name
        """
        # Act & Assert
        assert valid_user.name == "Test User"

    def test_email_property(self, valid_user: User) -> None:
        """
        Test that email property returns correct value.
        
        Arrange: Create a valid user
        Act: Access email property
        Assert: Returned value matches the user's email
        """
        # Act & Assert
        assert valid_user.email == "test@example.com"

    def test_created_at_property(self, valid_user: User) -> None:
        """
        Test that created_at property returns datetime instance.
        
        Arrange: Create a valid user
        Act: Access created_at property
        Assert: Returned value is a datetime instance
        """
        # Act & Assert
        assert isinstance(valid_user.created_at, datetime)


class TestUserToDict:
    """Tests for User.to_dict() method."""

    def test_to_dict_returns_all_fields(self) -> None:
        """
        Test that to_dict() returns all user fields.
        
        Arrange: Create a valid user
        Act: Call to_dict() method
        Assert: Returned dictionary contains all expected fields
        """
        # Arrange
        user = User(user_id=42, name="John", email="john@example.com")
        
        # Act
        user_dict = user.to_dict()
        
        # Assert
        assert "user_id" in user_dict
        assert "name" in user_dict
        assert "email" in user_dict
        assert "created_at" in user_dict
        assert user_dict["user_id"] == 42
        assert user_dict["name"] == "John"
        assert user_dict["email"] == "john@example.com"

    def test_to_dict_created_at_format(self) -> None:
        """
        Test that to_dict() returns created_at in ISO format.
        
        Arrange: Create a valid user
        Act: Call to_dict() method
        Assert: created_at is in ISO format string
        """
        # Arrange
        user = User(user_id=1, name="Test", email="test@example.com")
        
        # Act
        user_dict = user.to_dict()
        
        # Assert
        assert isinstance(user_dict["created_at"], str)
        # Verify ISO format by parsing it back
        datetime.fromisoformat(user_dict["created_at"])


class TestUserEquality:
    """Tests for User equality comparison."""

    def test_users_with_same_id_are_equal(self) -> None:
        """
        Test that users with same ID are considered equal.
        
        Arrange: Create two users with same ID but different names
        Act: Compare users with ==
        Assert: Users are equal
        """
        # Arrange
        user1 = User(user_id=1, name="John", email="john@example.com")
        user2 = User(user_id=1, name="Jane", email="jane@example.com")
        
        # Act & Assert
        assert user1 == user2

    def test_users_with_different_id_are_not_equal(self) -> None:
        """
        Test that users with different IDs are not equal.
        
        Arrange: Create two users with different IDs
        Act: Compare users with !=
        Assert: Users are not equal
        """
        # Arrange
        user1 = User(user_id=1, name="John", email="john@example.com")
        user2 = User(user_id=2, name="John", email="john@example.com")
        
        # Act & Assert
        assert user1 != user2

    def test_user_not_equal_to_non_user(self) -> None:
        """
        Test that User is not equal to non-User objects.
        
        Arrange: Create a user and non-user object
        Act: Compare user with non-user object
        Assert: They are not equal
        """
        # Arrange
        user = User(user_id=1, name="John", email="john@example.com")
        other = "not a user"
        
        # Act & Assert
        assert user != other


class TestUserStringRepresentation:
    """Tests for User string representations."""

    def test_str_representation(self) -> None:
        """
        Test __str__ returns user-friendly representation.
        
        Arrange: Create a valid user
        Act: Convert to string using str()
        Assert: String contains user info in readable format
        """
        # Arrange
        user = User(user_id=1, name="John", email="john@example.com")
        
        # Act
        result = str(user)
        
        # Assert
        assert "1" in result
        assert "John" in result
        assert "john@example.com" in result

    def test_repr_representation(self) -> None:
        """
        Test __repr__ returns detailed representation.
        
        Arrange: Create a valid user
        Act: Convert to repr string
        Assert: String contains all user attributes
        """
        # Arrange
        user = User(user_id=42, name="Jane", email="jane@example.com")
        
        # Act
        result = repr(user)
        
        # Assert
        assert "user_id=42" in result
        assert "name='Jane'" in result
        assert "email='jane@example.com'" in result
