Calibre with Python3
====================

Debian plans to remove Python2 support in the development course for Bullseye.

Calibre currently allows building and running under Python3, the experimental
branch of the git repository contains the necessary changes.

We still keep Calibre running under Python2, mostly due to the fact that all
the plugins out there and often used do **not** work with Python3.

We hope that Calibre will switch to Python3 before the release of Bullseye,
which would trigger an update of the plugins, too, and thus would allow
switching to Python3 also in Debian.

If this does not work out, we have to discuss with the Python Team about options.

Norbert Preining, 2019-09-04