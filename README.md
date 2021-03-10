# assembler

To simply see the result without writing anything to disk, `--stdout` can be used. 
Since the binary data will not look pretty being printed, it is recommended to pipe
the output to a hexdump tool, such as `xxd`:

```bash
$ python3 main.py test.asm --stdout | xxd
```

`-b` for binary view
