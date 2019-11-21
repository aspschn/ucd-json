ucd-json
=============

ucd-json is a tool for convert various text Unicode UCD data files to JSON format.

UCD data files
----------------
ucd-json downloads it's data from online during usage. If first run or other version requested, network connection should needed.

Files will downloaded under directory `data/{version}/`, `data/emoji/{version}/` which version is Unicode/Emoji version.

Usage
---------------

To list all available files,
```sh
$ ./ucd-json -l
```

then transform file to json by
```sh
$ ./ucd-json PropertyAliases.txt
```

You can also redirect the output to write result as file.
```sh
$ ./ucd-json PropertyValueAliases.txt > PropertyValueAliases.json
```

License
---------
ucd-json is available under the MIT license. For details, see the LICENSE file.
