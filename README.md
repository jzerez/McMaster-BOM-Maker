# McMaster BOM Maker
This project takes a list of McMaster part numbers and creates a CSV with the part name, the price per unit, and the number of items per unit.

## How to Use:
This project works on Windows only. First populate parts.txt with a list of McMaster part numbers. Each line should have its own part number like so.

```
95105A191
5537T962
5537T971
95105A119
95105A139
95105A175
```

Then simply run `McMasterSelenium.exe` in the `dist` directory.

The output file will automatically be saved to `parts.csv`
