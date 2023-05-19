# DASDEC Log Downloader

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Description

The project is a scraper built using Playwright to extract logs from DASDEC units.

## Installation

1. Clone the repository.

```shell
git clone https://github.com/erikjmurray/DasdecLogScrape
```

2. Change into the project directory.

```shell
cd your_project_directory
```

3. Install dependencies.

```shell
pip install -r requirement.txt
```

Note that you may need to use a variation of the following command if you have not properly added Python to your environment path.
```shell
python -m pip ...
```

## Usage

To use the scraper, follow these steps:

1. Prepare the `creds.json` file with the credentials for the DASDEC units.

```json
 [
     {
       "ip_addr": "192.168.0.1",
       "username": "admin",
       "password": "password",
       "name": "DASDEC 1",
       "timeframe": "7days"
     },
     {
       "ip_addr": "192.168.0.2",
       "username": "admin",
       "password": "password",
       "name": "DASDEC 2",
       "timeframe": "30days"
     }
 ]
```

2. Run the main script.

```shell
python main.py
```

## Configuration

- `ip_addr`: The IP address of the DASDEC unit.
- `username`: The username for accessing the DASDEC unit.
- `password`: The password for accessing the DASDEC unit.
- `name`: A name or identifier for the DASDEC unit.
- `timeframe`: The timeframe for which you want to scrape the logs (e.g., "7days", "30days"). 
  This parameter is optional, and if not provided, the default value is set to "7days".
  
## LICENSE

Feel free to customize the configuration and adapt the code to your specific requirements.

[MIT License](LICENSE)

---

Feel free to modify the sections, add more details, or customize the `README.md` file further according to your project's specific needs.


