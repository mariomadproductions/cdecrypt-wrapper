# cdecrypt-wrapper
Wrapper for cdecrypt that enables the user to pass a titlekey rather than a ticket file.

It works by creating a temporary dummy file containing the title key at the right offset, in the same folder as the title contents, and then passing that file as a ticket to `cdecrypt` in the PATH.
