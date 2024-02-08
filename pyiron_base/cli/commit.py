# Copyright (c) Max-Planck-Institut für Eisenforschung GmbH - Computational Materials Design (CM) Department
# Distributed under the terms of "New BSD License", see the LICENSE file.
"""
Remove jobs from pyiron project or whole project.
"""

import os
from pyiron_base.project.generic import Project



def register(parser):
    parser.add_argument(
        "project", help="path to pyiron project"
    )

def main(args):
    pr = Project(args.project)
    for job in pr.iter_jobs():
        dst = Project(f'{pr.state.staging_path}/{job.db_entry()["username"]}/{job.db_entry()["project"]}'.replace('//', '/'))
        job.move_to(dst)
