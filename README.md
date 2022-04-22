# Magic Hash Finder

This is a simple Python script that will search the input of a specific hash pattern.

For example, the input of a MD5 hash ending with `001` could be:
```bash
$ ./magic_hash_finder.py --algorithm md5 --end --pattern 001
[+] Looking for a matching hash...
[+] md5('5265') = f127a3f714240273e254d740ed23f001

$ echo -n 5265 |md5sum
f127a3f714240273e254d740ed23f001  -
```

The input of a SHA-1 hash starting with `0e` could be (check **PHP type Juggling** [here](https://book.hacktricks.xyz/pentesting/pentesting-web/php-tricks-esp#loose-comparisons-type-juggling) or [here](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf)):
```bash
./magic_hash_finder.py --algorithm md5 --start --pattern 0e
[+] Looking for a matching hash...
[+] md5('198') = 0e65972dce68dad4d52d063967f0a705
```

This tool can also match a pattern as a binary (particularly useful for SQL injections for example, when [`binary` is set to true](https://www.php.net/manual/en/function.md5.php)):
```bash
$ ./magic_hash_finder.py --algorithm md5 --start --binary --pattern "'"
[+] Looking for a matching hash...
[+] md5('109') = 2723d092b63885e0d7c260cc007e8b9d
```

> The first 2 hexadecimals `27` would be converted into the ASCII character `'`.

