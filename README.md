# telegram-export-channel-links

Export public channel and group links of telegram account.

## Installation

``` sh
pip install telegram-export-channel-links
```

## Usage

```
usage: telegram-export-channel-links [-h] [--app-id APP_ID] [--app-hash APP_HASH] [--no-groups] [--no-channels] [--names] [FILE]

Export public channel and group links of telegram account.

positional arguments:
  FILE                 File to export to (data is printed to stdout by default)

options:
  -h, --help           show this help message and exit
  --app-id APP_ID      Test credentials are used by default
  --app-hash APP_HASH  Test credentials are used by default
  --no-groups          Don't export group links
  --no-channels        Don't export channel links
  --names              Export channel names
```
