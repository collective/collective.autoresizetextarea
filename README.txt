Introduction
============

collective.autoresizetextarea is a jQuery textarea auto-resizer for Plone.

It is based on James Padolsey's jQuery `autoResize`_ plugin. Check this website for a demo.

.. _autoResize: http://james.padolsey.com/javascript/jquery-plugin-autoresize/

Buildout Installation
---------------------

Add the following code to your buildout.cfg:

[buildout]
...
eggs =
    ...
    collective.autoresizetextarea
    ...

...
[instance]
...
zcml =
    ...
    collective.autoresizetextarea
...

Usage
-----

To add the auto-resize feature to a textarea you can either add an
"autoresize" CSS class to a textarea:

    <textarea class="autoresize" />

or change the jQuery selector in the second line of the javascripts/autoresize.js file.

    ...
    jq('textarea.mycssclass').autoResize({
    ...
