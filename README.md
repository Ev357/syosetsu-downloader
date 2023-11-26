# Syosetu Downloader
A simple Python script to download manga chapters from syosetu.top

## Usage
```bash
python3 syosetsu-downloader.py [-h] [-d DIR] url
```

- `url`: The URL of the manga on syosetu.top.
- `-d DIR, --dir DIR`: (Optional) Sets the output directory for downloaded chapters. Default is `output`.

## Prerequisites
Make sure to install the required Python packages by running:

```bash
pip3 install -r requirements.txt
```

## Example
```bash
python3 syosetsu-downloader.py https://syosetu.top/yahari-ore-no-seishun-rabukome-wa-machigatte-iru-mougenroku-raw
```

This will download the chapters of the specified manga into the `output` directory.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
