"""
Entity layer module for MagicSquare project.

This module exports all entity classes and exceptions.
"""

from entity.user import User, InvalidUserError

__all__ = ["User", "InvalidUserError"]
