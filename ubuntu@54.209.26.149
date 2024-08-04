#!/usr/bin/python3
"""
Fabric script to generate a tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    """

    # Get the current time
    time = datetime.now()
    # Create the archive name using the current timestamp
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    
    # Create the versions directory if it doesn't exist
    local('mkdir -p versions')
    
    # Create the .tgz archive
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    
    # Check if the archive was created successfully
    if create.succeeded:
        return 'versions/' + archive
    else:
        return None

