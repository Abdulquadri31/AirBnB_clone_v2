#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the web_static folder.
    Returns:
        str: The archive path if successful, None otherwise.
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the archive name with timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{timestamp}.tgz"

        # Create the archive
        print(f"Packing web_static to {archive_name}")
        local(f"tar -cvzf {archive_name} web_static")

        # Check if the archive was created successfully
        if os.path.exists(archive_name):
            print(f"web_static packed: {archive_name}")
            return archive_name
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
