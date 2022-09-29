# TextMate Grammar for Scenic

This repository provides a [TextMate-format](https://macromates.com/manual/en/language_grammars) grammar for the [Scenic](https://scenic-lang.readthedocs.io/) scenario description language, suitable for use with Sublime Text, Atom, and Visual Studio Code.
The grammar is based on the [MagicPython grammar](https://github.com/MagicStack/MagicPython) by MagicStack Inc., which is also available under the MIT license (see `LICENSE`).
The rest of this README is adapted from parts of the MagicPython README.

## Installation Instructions

In **Atom**, install the `Scenic` package.

In **Sublime Text**, install `Scenic` package via "Package Control".

In **VSCode**, starting with version 0.10.1, install `Scenic` with
`Install Extension` command.

Alternatively, the package can be installed manually in all editors, by copying the Scenic package into the Sublime/Atom/VSCode user packages directory.

## Development

You need `npm` and `node.js` to work on this grammar.

- clone the repository
- run `make` to build the local development environment
- run `make release` to build the syntax packages for Sublime Text and Atom

## Color Scheme

If you want to write your own color scheme you can
find a list of all the scopes that we use in
[misc/scopes](misc/scopes). The file is automatically generated based
on the syntax grammar, so it is always up-to-date and exhaustive.
