=========
 OTE-IDE
=========

-------------------------------------------------
 Python IDE services for any editor or no editor
-------------------------------------------------

Introduction
============

OTE stands for One True Editor, and we pronounce it as 'Oat'.  It is a
Python IDE without an editor - you have to bring your own.


Motivation
==========

Many of the popular programmers' text editors have features which
allow for an IDE style development environment.  However getting these
features working together correctly for Python can be extremely
challenging.

The process involves configuring your editor to be aware of the
various tools you might be using on your project: test runners,
linters, application frameworks, virtualenvs, and so on; and due to
the combinatorial explosion of the options, it's possible for your
environment to be practically unique.  Managing the resulting glue and
configuration code is a development effort in its own right.  We
believe very few Python programmers have managed to harness the full
power of their editors.

The aim of OTE is to provide a middleware service external to the text
editor where Python development tools can be integrated.  It then
exposes some lowest common denominator interfaces which editor
integration can be written.  This should allow for editor integrations
to be written just once and utilised on any Python project.  It should
also be able to use many or all of the features through command line
tools, so you can work with an editor which has no integration at all.

We hope that by creating a project where Python programmers can work
together to improve all of their development environments, leaving
editor wars for the pub, we can make better progress than any
one-editor project could.


Design
======

See the Github wiki (also available as a git repository of rst files)
for some notes on design: https://github.com/OTE-IDE/OTE-IDE/wiki/Design-Notes


Licensing
=========

For now this project is licensed under the GPL v3, as a sensibly
restrictive default, and because I think it may be useful to include
some (L)GPL code in the project.

If you have a good reason why it should be under a more permissive (or
more restrictive) license, contact the authors and make your case.
