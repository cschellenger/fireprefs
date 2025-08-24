# Copy firefox user preferences

Simple python script to add [user.js](./user.js) to a firefox profile by name.

## Usage
```
usage: copy_prefs.py [-h] [--all] profile

Copy Firefox preferences to specified profile.

positional arguments:
  profile     Name of the Firefox profile to copy preferences to. Consider using 'default' for the default profile.

options:
  -h, --help  show this help message and exit
  --all       Copy preferences to all profiles.
```