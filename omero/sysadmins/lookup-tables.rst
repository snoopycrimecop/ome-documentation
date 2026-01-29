Look-up tables
==============

The OMERO.server ships with a number of look-up tables (LUTs) for use in rendering
images. These are stored under ``$(OMERODIR)/lib/scripts/luts`` in the OMERO.server and
are managed in a similar manner to server scripts.

Admins can add new LUTs to the server by placing them in the
``$(OMERODIR)/lib/scripts/luts`` directory. These LUTs will be included in the list of LUTs
available to clients via the API and can be chosen for rendering images.

The omero-web package includes a copy of the LUTs that are shipped with the
OMERO.server in order to provide a "preview" image of each LUT. If you add
new LUTs to the server, you can also update a cache of the preview images
as described in the 
`omero-web LUTs <https://github.com/ome/omero-web?tab=readme-ov-file#luts-caching>`_ documentation.
