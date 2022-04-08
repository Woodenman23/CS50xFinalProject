import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

## Lifted from cs50 finance code, take time to understand
def error(message, code=400):
    """Render message as user error."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("error.html", top=code, bottom=escape(message)), code