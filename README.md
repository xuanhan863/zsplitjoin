zsplitjoin
==========

Split and Join Files


USAGE
-----

```bash
$ md5sum BYTES.bz2
61a9b4dbc87d94446af63486e326cb4f  BYTES.bz2
$ ll BYTES.bz2 
-rw-r--r-- 1 usr usr 159M Ago 13 17:22 BYTES.bz2
$ ./zsplit.py BYTES.bz2 -n 3 -o splited -c 3K
$ ll splited.part*
-rw-r--r-- 1 usr usr 53M Ago 13 17:31 splited.part1
-rw-r--r-- 1 usr usr 53M Ago 13 17:31 splited.part2
-rw-r--r-- 1 usr usr 53M Ago 13 17:31 splited.part3
$ ./zjoin.py splited.part1 -c 2K -o joined.bz2
$ ll joined.bz2 
-rw-r--r-- 1 usr usr 159M Ago 13 17:31 joined.bz2
$ md5sum joined.bz2 
61a9b4dbc87d94446af63486e326cb4f  joined.bz2
$ rm splited.part*
$ rm joined.bz2
$
$
$ ./zsplit.py BYTES.bz2 -s 50M -o splited -c 2K
$ ll splited.part*
-rw-r--r-- 1 usr usr 50M Ago 13 17:31 splited.part1
-rw-r--r-- 1 usr usr 50M Ago 13 17:31 splited.part2
-rw-r--r-- 1 usr usr 59M Ago 13 17:31 splited.part3
$ ./zjoin.py splited.part1 -c 5K -o joined.bz2
$ ll joined.bz2
-rw-r--r-- 1 usr usr 159M Ago 13 17:32 joined.bz2
$ md5sum joined.bz2 
61a9b4dbc87d94446af63486e326cb4f  joined.bz2
$ rm splited.part*
$ rm joined.bz2
$
$
$ ./zsplit.py BYTES.bz2 -s 50M -o splited -c 2K -I
$ ll splited.part*
-rw-r--r-- 1 usr usr  50M Ago 13 17:32 splited.part1
-rw-r--r-- 1 usr usr  50M Ago 13 17:32 splited.part2
-rw-r--r-- 1 usr usr  50M Ago 13 17:32 splited.part3
-rw-r--r-- 1 usr usr 8,1M Ago 13 17:32 splited.part4
$ ./zjoin.py -c 1K -o joined.bz2 splited.part1
$ ll joined.bz2
-rw-r--r-- 1 usr usr 159M Ago 13 17:33 joined.bz2
$ md5sum joined.bz2
61a9b4dbc87d94446af63486e326cb4f  joined.bz2
$
$
$ rm splited.part*
$ rm joined.bz2
$ ./zsplit.py BYTES.bz2 -n 4 -o splited -c 3K
$ ll splited.part*
-rw-r--r-- 1 usr usr 40M Ago 13 17:33 splited.part1
-rw-r--r-- 1 usr usr 40M Ago 13 17:33 splited.part2
-rw-r--r-- 1 usr usr 40M Ago 13 17:33 splited.part3
-rw-r--r-- 1 usr usr 40M Ago 13 17:33 splited.part4
$ ./zjoin.py splited.part1 -c 2K -o joined.bz2
$ ll joined.bz2 
-rw-r--r-- 1 usr usr 159M Ago 13 17:33 joined.bz2
$ md5sum joined.bz2 
61a9b4dbc87d94446af63486e326cb4f  joined.bz2
$ 
```
