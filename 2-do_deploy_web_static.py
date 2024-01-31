#!/usr/bin/python3
"""
a Fabric script that distributes an archive to your web servers
based on the file 1-pack_web_static.py
"""
from fabric.api import local, put, run, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.27.14.242', '3.84.255.61']


def do_deploy(archive_path):
    """
    implements archive to servers
    """
    if not os.path.exists(archive_path):
        return False

    results = []

    res = put(archive_path, "/tmp")
    results.append(res.succeeded)

    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + basename + " -C " + newdir)

    run("rm /tmp/" + basename)
    run("mv " + newdir + "/web_static/* " + newdir)
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")

    return True
