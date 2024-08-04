#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers

execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run, sudo
from datetime import datetime
from os.path import exists, isdir

# Define the remote servers
env.hosts = ['54.209.26.149', '54.175.243.246']


def do_pack():
    """Generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(f"Error packing: {e}")
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
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
    except Exception as e:
        print(f"Error deploying: {e}")
        return False


def do_local_deploy(archive_path):
    """Deploys the archive locally"""
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        # Create a directory for the new release
        local('mkdir -p {}{}/'.format(path, no_ext))

        # Uncompress the archive into the newly created directory
        local('tar -xzf {} -C {}{}/'.format(archive_path, path, no_ext))

        # Move the content of the web_static folder to its parent directory
        local('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        # Remove the now empty web_static folder
        local('rm -rf {}{}/web_static'.format(path, no_ext))

        # Remove the existing symbolic link
        local('rm -rf /data/web_static/current')

        # Create a new symbolic link pointing to the new release
        local('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        return True
    except Exception as e:
        print(f"Error deploying locally: {e}")
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    
    # Check if it's running on a remote server or locally
    if 'localhost' in env.hosts or '127.0.0.1' in env.hosts:
        return do_local_deploy(archive_path)
    else:
        return do_deploy(archive_path)

