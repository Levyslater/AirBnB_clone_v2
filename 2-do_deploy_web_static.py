#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

# Define the remote servers
env.hosts = ['54.209.26.149', '54.175.243.246']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    # Check if the archive exists
    if not exists(archive_path):
        return False
    try:
        # Extract file name and name without extension
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the /tmp/ directory on the remote servers
        put(archive_path, '/tmp/')
        
        # Create a directory for the new release
        run('mkdir -p {}{}/'.format(path, no_ext))
        
        # Uncompress the archive into the newly created directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        
        # Remove the archive from the /tmp/ directory
        run('rm /tmp/{}'.format(file_n))
        
        # Move the content of the web_static folder to its parent directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        
        # Remove the now empty web_static folder
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        
        # Remove the existing symbolic link
        run('rm -rf /data/web_static/current')
        
        # Create a new symbolic link pointing to the new release
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        
        return True
    except:
        return False

