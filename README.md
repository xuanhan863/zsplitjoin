zsplitjoin
==========

Split and Join Files


USAGE
-----

```bash
$ ll BYTES.bz2 
-rw-r--r-- 1 user user 159M Ago 13 17:02 BYTES.bz2
$ ./zsplit.py BYTES.bz2 -n 3 -o splited -c 3K
$ ll splited.part*
-rw-r--r-- 1 user user 53M Ago 13 17:03 splited.part1
-rw-r--r-- 1 user user 53M Ago 13 17:03 splited.part2
-rw-r--r-- 1 user user 53M Ago 13 17:03 splited.part3
$ ./zjoin.py splited.part1 -c 2K -o joined.bz2
$ ll joined.bz2 
-rw-r--r-- 1 user user 159M Ago 13 17:03 joined.bz2
$ md5sum joined.bz2 
61a9b4dbc87d94446af63486e326cb4f  joined.bz2
$ md5sum BYTES.bz2 
61a9b4dbc87d94446af63486e326cb4f  BYTES.bz2
$ rm splited.part*
$ rm joined.bz2 
$ ./zsplit.py BYTES.bz2 -s 50M -o splited -c 2K
$ ll splited.part*
-rw-r--r-- 1 user user 50M Ago 13 17:05 splited.part1
-rw-r--r-- 1 user user 50M Ago 13 17:05 splited.part2
-rw-r--r-- 1 user user 59M Ago 13 17:05 splited.part3
$ ./zjoin.py splited.part1 -c 5K -o joined.bz2
$ ll joined.bz2
-rw-r--r-- 1 user user 159M Ago 13 17:05 joined.bz2
$ md5sum joined.bz2
61a9b4dbc87d94446af63486e326cb4f  joined.bz2
$ md5sum BYTES.bz2
61a9b4dbc87d94446af63486e326cb4f  BYTES.bz2
$
```
