=================
kotti_rstdocument
=================

This is an extension to the Kotti CMS that allows you to add
reStructuredText documents to your Kotti site.

It uses the `Docutils library`_ to render reStructuredText to
HTML.

`Find out more about Kotti`_

Setup
=====

To activate the kotti_rstdocument add-on in your Kotti site, you need to
add an entry to the ``kotti.configurators`` setting in your Paste
Deploy config.  If you don't have a ``kotti.configurators`` option,
add one.  The line in your ``[app:Kotti]`` section could then look
like this::

  kotti.configurators = kotti_rstdocument.kotti_configure

  With this, you'll be able to add calendar and event items in your site.


  .. _Docutils library: http://docutils.sourceforge.net
  .. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

