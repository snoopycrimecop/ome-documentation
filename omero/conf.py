#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ome documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 22 20:24:38 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime
import sys
import os
import shutil
import re

# Append the top level directory of the docs, so we can import from the
# config dir.
#sys.path.insert(0, os.path.abspath('../common'))
sys.path.insert(1, os.path.abspath('../omero'))
import conf_autogen


linkcheck_ignore = []
extensions = ['sphinx.ext.extlinks']

# -- General configuration ----------------------------------------------------

# General information about the project.
project = u'OMERO'
title = project + u' Documentation'

# General information about the project.
author = u'The Open Microscopy Environment'
copyright = u'2000-%d, ' % datetime.datetime.now().year + author


def split_release(release):
    split_release = re.split(r"^([0-9]+)\.([0-9]+)\.([0-9]+)(.*?)$", release)
    return (int(split_release[1]), int(split_release[2]),
            int(split_release[3]))


def get_previous_version(majornumber, minornumber=0):
    # Return the previous version number for the first minor versions of a
    # major series i.e. x.0.y
    # Implemented as an hard-coded list until we work out an automated way to
    # upgrade the database without specifying version numbers e.g.
    # bin/omero db upgrade
    if minornumber == 0:
        if majornumber == 5:
            return "4.4"
        elif majornumber == 4:
            return "3.2"
        else:
            raise Exception("No previous version defined for %s.%s"
                            % (majornumber, minornumber))
    else:
        return "%s.%s" % (majornumber, minornumber - 1)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if "OMERO_RELEASE" in os.environ and len(os.environ.get('OMERO_RELEASE')) > 0:
    release = os.environ.get('OMERO_RELEASE')
    [majornumber, minornumber, patchnumber] = split_release(release)

    # Define Sphinx version and release variables and development branch
    version = ".".join(str(x) for x in (majornumber, minornumber))

    if patchnumber > 0:
        tags.add('point_release')
    previousversion = get_previous_version(majornumber, minornumber)
else:
    version = 'UNKNOWN'
    previousversion = 'UNKNOWN'
    release = 'UNKNOWN'

# Variables used to define Github extlinks
if "SOURCE_BRANCH" in os.environ and len(os.environ.get('SOURCE_BRANCH')) > 0:
    branch = os.environ.get('SOURCE_BRANCH')
else:
    branch = 'develop'

if "SOURCE_USER" in os.environ and len(os.environ.get('SOURCE_USER')) > 0:
    user = os.environ.get('SOURCE_USER')
else:
    user = 'ome'

github_root = 'https://github.com/'
omero_github_root = github_root + user + '/openmicroscopy/'
bf_github_root = github_root + user + '/bioformats/'
doc_github_root = github_root + user + '/ome-documentation/'

# Variables used to define Jenkins extlinks (ci-master)
jenkins_root = 'https://ci.openmicroscopy.org'
jenkins_job_root = jenkins_root + '/job'
jenkins_view_root = jenkins_root + '/view'

# Variables used to define Jenkins extlinks (merge-ci)
mergeci_root = 'https://merge-ci.openmicroscopy.org/jenkins'
mergeci_job_root = mergeci_root + '/job'
mergeci_view_root = mergeci_root + '/view'

# Variables used to define other extlinks
cvs_root = 'http://cvs.openmicroscopy.org.uk'
trac_root = 'https://trac.openmicroscopy.org/ome'
oo_root = 'https://www.openmicroscopy.org'
oo_site_root = oo_root + '/site'
lists_root = 'http://lists.openmicroscopy.org.uk'
downloads_root = 'https://downloads.openmicroscopy.org'
help_root = 'https://help.openmicroscopy.org'
docs_root = 'https://docs.openmicroscopy.org'
imagesc_root = 'https://forum.image.sc'

rst_prolog = """
"""
rst_epilog = """
.. _Hibernate: http://www.hibernate.org
.. _ZeroC: https://zeroc.com
.. _Ice: https://zeroc.com
.. _Jenkins: https://jenkins.io
.. _roadmap: https://trac.openmicroscopy.org/ome/roadmap
.. _OME artifactory: https://artifacts.openmicroscopy.org
.. _Open Microscopy Environment: https://www.openmicroscopy.org
.. _Glencoe Software, Inc.: https://www.glencoesoftware.com/
.. _Pillow: https://pillow.readthedocs.org
.. _Matplotlib: https://matplotlib.org/
.. _Django 1.8: https://docs.djangoproject.com/en/1.8/releases/1.8/
.. _Django 1.6: https://docs.djangoproject.com/en/1.6/releases/1.6/
.. _Python: https://www.python.org
.. _Libjpeg: http://libjpeg.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _PyPI: https://pypi.org
.. _Conda: https://docs.conda.io/en/latest/
.. _PyTables: http://pytables.org
.. |SSH| replace:: :abbr:`SSH (Secure Shell)`
.. |VM| replace:: :abbr:`VM (Virtual Machine)`
.. |OS| replace:: :abbr:`OS (Operating System)`
.. |SSL| replace:: :abbr:`SSL (Secure Socket Layer)`
.. |JDK| replace:: :abbr:`JDK (Java Development Kit)`
.. |JMX| replace:: :abbr:`JMX (Java Management Extensions)`
.. |JRE| replace:: :abbr:`JRE (Java Runtime Environment)`
.. |JVM| replace:: :abbr:`JVM (Java Virtual Machine)`
.. |PID| replace:: :abbr:`PID (process ID)`
.. |HDD| replace:: :abbr:`HDD (Hard Disk Drive)`
.. |CLI| replace:: :abbr:`CLI (Command Line Interface)`
.. |OME| replace:: `Open Microscopy Environment`_
.. |Glencoe| replace:: `Glencoe Software, Inc.`_
"""

rst_epilog += """
.. |OmeroPy| replace:: :doc:`/developers/Python`
.. |OmeroCpp| replace:: :doc:`/developers/Cpp`
.. |OmeroJava| replace:: :doc:`/developers/Java`
.. |OmeroMatlab| replace:: :doc:`/developers/Matlab`
.. |OmeroApi| replace:: :doc:`/developers/Modules/Api`
.. |OmeroWeb| replace:: :doc:`/developers/Web`
.. |OmeroClients| replace:: :doc:`/developers/GettingStarted`
.. |OmeroGrid| replace:: :doc:`/sysadmins/grid`
.. |OmeroSessions| replace:: :doc:`/developers/Server/Sessions`
.. |OmeroModel| replace:: :doc:`/developers/Model`
.. |ExtendingOmero| replace:: :doc:`/developers/Server/ExtendingOmero`
.. |BlitzGateway| replace:: :doc:`/developers/Python`
.. |DevelopingOmeroClients| replace:: :doc:`/developers/GettingStarted/AdvancedClientDevelopment`
.. _Spring: https://spring.io
.. |previousversion| replace:: %s
.. |current_dbver|  replace:: %s
.. |previous_dbver|  replace:: %s
.. |version_py|  replace:: %s
.. |version_web|  replace:: %s
.. |iceversion| replace:: 3.6.5
.. |postgresversion| replace:: 11
.. |javaversion| replace:: 11
.. |version_dropbox|  replace:: %s

.. |Broken| image:: /images/broken.png
             :alt: Broken
.. |Deprecated| image:: /images/deprecated.png
                 :alt: Deprecated
.. |Dropped| image:: /images/dropped.png
              :alt: Dropped
.. |Recommended| image:: /images/recommended.png
                  :alt: Recommended
.. |Supported| image:: /images/supported.png
                :alt: Supported
.. |Unsupported| image:: /images/unsupported.png
                  :alt: Unsupported
.. |Upcoming| image:: /images/upcoming.png
               :alt: Upcoming
""" % (previousversion, conf_autogen.current_dbver,
       conf_autogen.previous_dbver,
       conf_autogen.version_py,
       conf_autogen.version_web,
       conf_autogen.version_dropbox)

omero_subs_github_root = github_root + 'ome/{}/{}/{}/%s'

extlinks = {
    # image.sc
    'imagesc': (imagesc_root + '/%s', '#'),
    # Trac links
    'ticket': (trac_root + '/ticket/%s', '#'),
    'milestone': (trac_root + '/milestone/%s', ''),
    'report': (trac_root + '/report/%s', ''),
    # Jenkins links (ci-master)
    'jenkins': (jenkins_root + '/%s', ''),
    'jenkinsjob': (jenkins_job_root + '/%s', ''),
    'jenkinsview': (jenkins_view_root + '/%s', ''),
    # Jenkins links (merge-ci)
    'mergeci': (mergeci_root + '/%s', ''),
    'mergecijob': (mergeci_job_root + '/%s', ''),
    # Mailing list/forum links
    'ome-users': (lists_root + '/pipermail/ome-users/%s', ''),
    'ome-devel': (lists_root + '/pipermail/ome-devel/%s', ''),
    'forum': (oo_root + '/community/%s', ''),
    # Website links
    'community': (oo_root + '/support/%s', ''),
    'omero': (oo_root + '/omero/%s', ''),
    'bf': (oo_root + '/bio-formats/%s', ''),
    'secvuln': (oo_root + '/security/advisories/%s', ''),
    'security': (oo_root + '/security/%s', ''),
    'presentations': (downloads_root + '/presentations/%s', ''),
    # Doc links
    'model_doc': (docs_root + '/latest/ome-model/%s', ''),
    'devs_doc': (docs_root + '/contributing/%s', ''),
    'schema': (oo_root + '/Schemas/%s', ''),
    # Help links
    'help': (help_root + '/%s', ''),
    # Miscellaneous links
    'snapshot': (cvs_root + '/snapshots/%s', ''),
    'zeroc': ('https://zeroc.com/%s', ''),
    'zerocforum': ('https://forums.zeroc.com/discussion/%s', ''),
    'zerocdoc': ('https://doc.zeroc.com/%s', ''),
    'djangodoc': ('https://docs.djangoproject.com/en/1.11/%s', ''),
    'doi': ('https://dx.doi.org/%s', ''),
    'pypi': ('https://pypi.org/project/%s', ''),
    }

# OMERO-specific extlinks
omero_extlinks = {
    # GitHub links
    'source': (omero_github_root + 'blob/'+ branch + '/%s', ''),
    'sourcedir': (omero_github_root + 'tree/' + branch + '/%s', ''),
    'commit': (omero_github_root + 'commit/%s', ''),
    'omedocs': (doc_github_root + '%s', ''),
    # GitHub decoupled subcomponents
    'omero_subs_github_repo_root': (github_root + 'ome/%s', ''),
    'dsl_plugin_source': (omero_subs_github_root.format('omero-dsl-plugin', 'blob', 'v' + conf_autogen.version_dsl_plugin), ''),
    'dsl_plugin_sourcedir': (omero_subs_github_root.format('omero-dsl-plugin', 'tree', 'v' + conf_autogen.version_dsl_plugin), ''),
    'blitz_plugin_source': (omero_subs_github_root.format('omero-blitz-plugin', 'blob', 'v' + conf_autogen.version_blitz_plugin), ''),
    'blitz_plugin_sourcedir': (omero_subs_github_root.format('omero-blitz-plugin', 'tree', 'v' + conf_autogen.version_blitz_plugin), ''),
    'ice_builder_source': (omero_subs_github_root.format('ice-builder-gradle', 'blob', 'v' + conf_autogen.version_ice_builder), ''),
    'ice_builder_sourcedir': (omero_subs_github_root.format('ice-builder-gradle', 'tree', 'v' + conf_autogen.version_ice_builder), ''),
    'model_source': (omero_subs_github_root.format('omero-model', 'blob', 'v' + conf_autogen.version_model), ''),
    'model_sourcedir': (omero_subs_github_root.format('omero-model', 'tree', 'v' + conf_autogen.version_model), ''),
    'common_source': (omero_subs_github_root.format('omero-common', 'blob', 'v' + conf_autogen.version_common), ''),
    'common_sourcedir': (omero_subs_github_root.format('omero-common', 'tree', 'v' + conf_autogen.version_common), ''),
    'romio_source': (omero_subs_github_root.format('omero-romio', 'blob', 'v' + conf_autogen.version_romio), ''),
    'romio_sourcedir': (omero_subs_github_root.format('omero-romio', 'tree', 'v' + conf_autogen.version_romio), ''),
    'renderer_source': (omero_subs_github_root.format('omero-renderer', 'blob', 'v' + conf_autogen.version_renderer), ''),
    'renderer_sourcedir': (omero_subs_github_root.format('omero-renderer', 'tree', 'v' + conf_autogen.version_renderer), ''),
    'server_source': (omero_subs_github_root.format('omero-server', 'blob', 'v' + conf_autogen.version_server), ''),
    'server_sourcedir': (omero_subs_github_root.format('omero-server', 'tree', 'v' + conf_autogen.version_server), ''),
    'blitz_source': (omero_subs_github_root.format('omero-blitz', 'blob', 'v' + conf_autogen.version_blitz), ''),
    'blitz_sourcedir': (omero_subs_github_root.format('omero-blitz', 'tree', 'v' + conf_autogen.version_blitz), ''),
    'java_gateway_source': (omero_subs_github_root.format('omero-gateway-java', 'blob', 'v' + conf_autogen.version_gateway), ''),
    'java_gateway_sourcedir': (omero_subs_github_root.format('omero-gateway-java', 'tree', 'v' + conf_autogen.version_gateway), ''),
    'matlab_source': (omero_subs_github_root.format('omero-matlab', 'blob', 'v' + conf_autogen.version_matlab), ''),
    'matlab_sourcedir': (omero_subs_github_root.format('omero-matlab', 'tree', 'v' + conf_autogen.version_matlab), ''),
    'insight_source': (omero_subs_github_root.format('omero-insight', 'blob', 'master'), ''),
    'insight_sourcedir': (omero_subs_github_root.format('omero-insight', 'tree', 'master'), ''),
    'web_source': (omero_subs_github_root.format('omero-web', 'blob', 'v' + conf_autogen.version_web), ''),
    'web_sourcedir': (omero_subs_github_root.format('omero-web', 'tree', 'v' + conf_autogen.version_web), ''),
    'py_source': (omero_subs_github_root.format('omero-py', 'blob', 'v' + conf_autogen.version_py), ''),
    'py_sourcedir': (omero_subs_github_root.format('omero-py', 'tree', 'v' + conf_autogen.version_py), ''),
    'dropbox_source': (omero_subs_github_root.format('omero-dropbox', 'blob', 'v' + conf_autogen.version_dropbox), ''),
    'dropbox_sourcedir': (omero_subs_github_root.format('omero-dropbox', 'tree', 'v' + conf_autogen.version_dropbox), ''),
    # API links
    'javadoc': (downloads_root + '/latest/omero5.5/api/%s', ''),
    'javadoc_gateway_java': (docs_root + '/omero-gateway/' + conf_autogen.version_gateway + '/javadoc/%s', ''),
    'javadoc_blitz': (docs_root + '/omero-blitz/' + conf_autogen.version_blitz + '/javadoc/%s', ''),
    'javadoc_server': (docs_root + '/omero-server/' + conf_autogen.version_server + '/javadoc/%s', ''),
    'javadoc_renderer': (docs_root + '/omero-renderer/' + conf_autogen.version_renderer + '/javadoc/%s', ''),
    'javadoc_romio': (docs_root + '/omero-romio/' + conf_autogen.version_romio + '/javadoc/%s', ''),
    'javadoc_common': (docs_root + '/omero-common/' + conf_autogen.version_common + '/javadoc/%s', ''),
    'javadoc_model': (docs_root + '/omero-model/' + conf_autogen.version_model + '/javadoc/%s', ''),
    'slicedoc_blitz': (docs_root + '/omero-blitz/' +
                       conf_autogen.version_blitz + '/slice2html/%s', ''),
    'pythondoc': (downloads_root + '/latest/omero5.5/api/python/%s', ''),
    # Downloads
    'downloads': (downloads_root + '/latest/omero5.5/%s', ''),
    # Versioned Bio-Formats doc link
    'bf_v_doc': (docs_root + '/bio-formats/' + conf_autogen.version_bioformats + '/' + '%s', ''),
    # Miscellaneous links
    'springdoc': ('https://docs.spring.io/spring/docs/%s', ''),
    'ivydoc': ('https://ant.apache.org/ivy/history/2.3.0/%s', ''),
    }
extlinks.update(omero_extlinks)

# Edit on GitHub prefix
#edit_on_github_prefix = 'omero'

# -- Options for HTML output --------------------------------------------------

# Custom sidebar templates, maps document names to template names.
#html_sidebars['**'].insert(1, 'globalomerotoc.html')

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path.extend(['themes'])

# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
# target = project + '-' + release + '.tex'
# latex_documents = [
#  (master_doc, target, title, author, 'manual'),
# ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = 'images/omero-logo.pdf'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a
# linkcheck build
linkcheck_ignore += [
    r'http://localhost:\d+/?', 'http://localhost/',
    'http://www.hibernate.org',
    'https://www.jboss.org',
    'https://code.google.com/archive/p/luke/',
    'https://www.youtube.com/channel/UCyySB9ZzNi8aBGYqcxSrauQ',
    'https://httpd.apache.org/docs/current/mod/mod_proxy.html',
    'https://access.redhat.com/articles/3078',
    r'.*[.]sourceforge.net',
    r'https?://www\.openmicroscopy\.org/site/team/.*',
    r'.*[.]?example\.com/.*',
    r'https://spreadsheets.google.com/.*',
    r'https://msdn.microsoft.com/en-us/library/aa362244\(v=vs.85\).aspx',
    'https://testng.org/',
    'https://packages.ubuntu.com/search',
    # Those below may start working with Sphinx 2.1, see sphinx-doc #6381.
    'https://www.cloudflare.com/',
    'https://www.zenoss.com/',
    # Timeouts which may be fixed in a newer version
    'https://micronoxford.com/',
    github_root + 'ome/',
    r'https://help.openmicroscopy.org/.*#.*']

exclude_patterns = ['sysadmins/unix/walkthrough/requirements*',
                    'downloads/inplace', 'downloads/cli',
                    'changelog.rst']


def copy_legacy_redirects(app, exception):
    """
    see: https://tech.signavio.com/2017/managing-sphinx-redirects
    """
    print("Adding redirects:")
    redirect_files = [
        'sysadmins/server-overview.html',
        'sysadmins/server-tables.html',
        'sysadmins/omero-home-prefix.html',
        'sysadmins/install-web.html',
        'developers/Insight/Architecture.html',
        'developers/Insight/Configuration.html',
        'developers/Insight/DirectoryContents.html',
        'developers/Insight/EventBus.html',
        'developers/Insight/HowTo/BuildAgent.html',
        'developers/Insight/HowTo/BuildAgentView.html',
        'developers/Insight/HowTo/RetrieveData.html',
        'developers/Insight/ImplementationView.html',
        'developers/Insight/TaskBar.html',

    ]
    if app.builder.name == 'html':
        for html_src_path in redirect_files:
            target_path = app.outdir + '/' + html_src_path
            src_path = app.srcdir + '/' + html_src_path
            if os.path.isfile(src_path):
                target_dir = os.path.dirname(target_path)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.copyfile(src_path, target_path)
                print("  %s" % html_src_path)


def setup(app):
    app.connect('build-finished', copy_legacy_redirects)
    app.add_crossref_type(
        directivename = "property",
        rolename      = "property",
        indextemplate = "%s",
    )
