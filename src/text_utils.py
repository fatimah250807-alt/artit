"""Utility functions for cleaning and formatting text values."""

def clean_name(raw):
    """Return a cleaned-up name: collapse whitespace and convert to title case."""
    # Remove surrounding whitespace
    raw = raw.strip()

    # Collapse repeated inner whitespace
    raw = " ".join(raw.split())

    # Convert to title case
    return raw.title()
