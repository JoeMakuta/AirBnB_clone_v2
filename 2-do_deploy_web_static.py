#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['52.91.165.160', '35.153.98.133']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/'


def do_deploy(archive_path):
    """Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False
        # upload archive
        put(archive_path, '/tmp/')
        # create target dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
release/webstatic_{}/'.format(timestamp))
        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/wb_sttic/releases/web_static_{}/'
            .format(timestamp, timestamp))
        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))
        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/wb_sttic/releases/web_static_{}/'.format(timestamp, timestamp))
        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/\
web_staic_{/web_static'
            .format(timestamp))
        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')
        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/\
web_staic_{/ /data/web_static/current'.format(timestamp))
    except (Exception):
        return False

    # return True on success
    return True
