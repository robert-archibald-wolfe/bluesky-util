"""
Utility functions for BlueSky data processing.
"""

from datetime import datetime
from typing import Optional


def format_date(date_string: Optional[str]) -> str:
    """
    Format an ISO date string to YYYY-MM-DD.
    
    Args:
        date_string: ISO date string or None
        
    Returns:
        Formatted date string or empty string if invalid
    """
    if not date_string:
        return ""
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except Exception:
        return date_string[:10] if len(date_string) >= 10 else date_string


def validate_username(username: str) -> str:
    """
    Validate and normalize BlueSky username format.
    
    With BlueSky now supporting custom domains, usernames must be fully qualified.
    This function validates that the username contains a domain and returns it as-is.
    
    Args:
        username: Raw username input (must include domain)
        
    Returns:
        The username as provided (if valid)
        
    Raises:
        ValueError: If username doesn't contain a domain
    """
    if '.' not in username:
        raise ValueError(
            f"Username '{username}' must include a domain (e.g., 'user.bsky.social' or 'user.example.com'). "
            "BlueSky now supports custom domains, so please provide the full username."
        )
    return username


def truncate_text(text: Optional[str], max_length: int = 32) -> str:
    """
    Truncate text to specified length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length before truncation
        
    Returns:
        Truncated text with "..." if needed
    """
    if not text:
        return ""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
