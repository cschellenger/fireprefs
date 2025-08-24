# Copy firefox user preferences

Simple python script to add [user.js](./user.js) to a firefox profile by name.

## Usage
```
usage: copy_prefs.py [-h] [--profile PROFILE] [--all]

Copy Firefox preferences to specified profile.

options:
  -h, --help         show this help message and exit
  --profile PROFILE  Name of the profile to copy preferences to. Defaults to 'default'.
  --all              Copy preferences to all profiles.
```