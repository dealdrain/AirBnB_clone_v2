#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.27.14.242', '3.84.255.61']


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
