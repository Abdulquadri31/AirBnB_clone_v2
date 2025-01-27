#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.
"""
from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define the web servers
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)
        if not os.path.exists("versions"):
            os.makedirs("versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        name_no_ext = file_name.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(name_no_ext)

        # Upload the archive to /tmp/
        put(archive_path, "/tmp/{}".format(file_name))

        # Create the release directory
        run("mkdir -p {}".format(release_path))

        # Extract the archive into the release directory
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))

        # Remove the archive from /tmp/
        run("rm /tmp/{}".format(file_name))

        # Move the files to the proper location
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))

        # Update the symbolic link
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Full deployment: Creates and distributes an archive to web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
