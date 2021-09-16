# Discord-Logging apt packages upgrader
This simple python script serves as an upgrader for apt packages.

It then logs all the upgraded packages to a discord server via webhooks.
## Installation
Install requirements:

`pip3 install requirements.txt`

Then create a .env file containing the discord webhook URL, which is retrievable under the _"Integrations"_ tab on any discord server (if you have appropriate permissions):

`echo "URL=your-webhook-url" >> .env`
## Usage
This script is designed to be run as **superuser**, the reason being apt requiring sudo to run upgrades.

`sudo python3 updater.py`
### Automation (Optional)
The script is designed for Debian-like distributions, as such this small tutorial uses [cron](https://linux.die.net/man/8/crond) to execute the script automatically every day.

Let's start by opening the cron configuration file, you want to execute the command to do that as **superuser**:

`sudo crontab -e`

Then add the following line at the end of the configuration file, with appropriate modifications (specify minute and hour of execution, e.g. 0 15 * * * : every day at 3 p.m.):

`min hour * * * sudo python3 /path/to/script/updater.py`

For more advanced time configurations visit [crontab guru](https://crontab.guru/).