=============
Plex-ZA Tech Show
=============

A simple Plex_ plugin for zatechshow.co.za_, audio podcasts. Video is coming
when Plex decides it actually can understand what an mp4 file is (I'm not
bitter).

By Dominic White singe-plex(*)singe.za.net

Installation
============

Assuming you already have a working Plex installation, grab the latest release
from `the downloads`_ and double-click to install.

Building From Source
====================

The Plex-ZA Tech Show_ plugin bundle is built from files in the ``bundle/`` and
``templates/`` directories. To build the bundle you'll need:

- Git_
- Ruby_ & Rake_ (Both are bundled with OS X)

With those tools installed, get a copy of the source and install the plugin::

    $ git clone git://github.com/singe/plex-zatechshow.git
    $ cd plex-zatechshow
    $ rake install

If you'd like to remove the plugin later, use::

    $ rake uninstall

Or, ``rake uninstall:hard`` to uninstall the plugin *and* it's preferences and data.

If you wish to package your own double-clickable plugin installer, you'll need
two additional build dependencies:

- The `Plex App Maker`_
- The rb-appscript_ RubyGem (``gem install rb-appscript``)

Then, just run ``rake package`` and check the ``dist`` directory.

License
=======

Under the same terms as Plex, GPLv2.

Thanks
======

This is my first Plex plugin. Plex documentation is uber-crap, and was more
painful than it needed to be.

- I cloned this from Ches Martin's `Vimcasts plugin`_.
- He in-turn cloned David Leatherman's `Railscasts plugin`_.
- Rake build script cribbed from Rick Fletcher's `MLB plugin`_.

.. _Plex: http://plexapp.com/
.. _zatechshow.co.za: http://zatechshow.co.za/
.. _the downloads: http://github.com/ches/plex-vimcasts/downloads
.. _Git: http://code.google.com/p/git-osx-installer/downloads/list?can=3
.. _Ruby: http://www.ruby-lang.org/
.. _Rake: http://rake.rubyforge.org/
.. _Plex App Maker: http://forums.plexapp.com/index.php?/topic/10180-plex-app-maker/
.. _rb-appscript: http://appscript.sourceforge.net/rb-appscript/index.html
.. _Vimcasts plugin: http://github.com/ches/plex-vimcasts
.. _Railscasts plugin: http://github.com/leathekd/plex_railscasts_plugin
.. _MLB plugin: http://github.com/rfletcher/plex-mlb

