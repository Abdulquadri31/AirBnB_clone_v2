#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""
from fabric.api import env, local, run

# Define the web servers
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep. If 0 or 1.
    """
    try:
        number = int(number)
        if number < 1:
            number = 1

        # Delete local archives
        archives = sorted(local("ls -1 versions", capture=True).split("\n"))
        archives_to_delete = archives[:-number]
        for archive in archives_to_delete:
            local("rm -f versions/{}".format(archive))

        # Delete remote archives
        releases = run("ls -1t /data/web_static/releases").split("\n")
        releases = [r for r in releases if "web_static_" in r]
        releases_to_delete = releases[number:]
        for release in releases_to_delete:
            run("rm -rf /data/web_static/releases/{}".format(release))

    except Exception as e:
        print("An error occurred:", e)
