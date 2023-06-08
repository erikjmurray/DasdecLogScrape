# DASDEC Log Downloader

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Description

The project is a scraper built using Playwright to extract logs from DASDEC units.

## Installation

<details>
 
<summary>Getting started</summary>
 
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
</details>
 
## Configuration

<details>
<summary>Parameter Definitions for Creds file</summary> 
 
- `ip_addr`: The IP address of the DASDEC unit.
- `username`: The username for accessing the DASDEC unit.
- `password`: The password for accessing the DASDEC unit.
- `name`: A name or identifier for the DASDEC unit.
- `timeframe`: The timeframe for which you want to scrape the logs (e.g., "7days", "30days"). 
   - This parameter is optional, and if not provided, the default value is set to "7days".
   -  |           |           | Options  |          |        |   
      | :-------: | :-------: | :------: | :------: | :----: |
      | today     | 2days     | 7days    | 14days   | 28days |
      | 60days    | 120days   | thisweek | lastweek | 2weeks |
      | thismonth | lastmonth | 2months  | thisyear | random |
 
</details>
<details>
 
<summary>Example Creds File</summary>
 
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
 
</details>
 
## Usage

<details>
 
<summary>Running the Script</summary>
 
To use the scraper, follow these steps:
 
1. Make sure you have provided a valid credentials json file as detailed above.
 
2. Run the scrape script.

```shell
python scrape.py
```
 
3. The logs will be stored in a folder called ScrapedLogs in root directory of the project.
 
4. 
</details>

## LICENSE

Feel free to customize the configuration and adapt the code to your specific requirements.

[MIT License](LICENSE)

---
