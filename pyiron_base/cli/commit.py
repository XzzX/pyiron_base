# Copyright (c) Max-Planck-Institut für Eisenforschung GmbH - Computational Materials Design (CM) Department
# Distributed under the terms of "New BSD License", see the LICENSE file.
"""
Remove jobs from pyiron project or whole project.
"""

import os
from pyiron_base.project.generic import Project



def register(parser):
    parser.add_argument(
        "project", default=".", nargs="?", help="path to pyiron project"
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="recurse into subprojects"
    )


def main(args):
    pr = Project(args.project)
    staging_project = Project(pr.state.staging_path + pr.name)
    pr.move_to(staging_project)
