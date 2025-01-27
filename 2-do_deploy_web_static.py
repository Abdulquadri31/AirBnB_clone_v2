#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers.
"""

from fabric.api import env, put, run
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Args:
        archive_path (str): The path to the archive to deploy.
    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get the archive file name without the directory path
        archive_file = archive_path.split("/")[-1]
        # Remove the extension to get the folder name
        archive_name = archive_file.split(".")[0]
        release_path = f"/data/web_static/releases/{archive_name}/"

        # Upload the archive to the /tmp/ directory
        put(archive_path, f"/tmp/{archive_file}")

        # Create the release directory
        run(f"mkdir -p {release_path}")

        # Uncompress the archive to the release directory
        run(f"tar -xzf /tmp/{archive_file} -C {release_path}")

        # Remove the uploaded archive from /tmp/
        run(f"rm /tmp/{archive_file}")

        # Move the extracted content to the proper release folder
        run(f"mv {release_path}web_static/* {release_path}")
        run(f"rm -rf {release_path}web_static")

        # Remove the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_path} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
