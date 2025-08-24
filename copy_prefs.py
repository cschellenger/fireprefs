#!/usr/bin/env python3
import argparse
from configparser import ConfigParser
import os

def read_prefs(file_path):
    config = ConfigParser()
    config.read(file_path)
    return config

def main(profile_name=None):
    profiles_file = os.path.expanduser('~/.mozilla/firefox/profiles.ini')
    profiles_conf = ConfigParser()
    profiles_conf.read(profiles_file)

    with open("user.js", "r") as input_file:
        prefs_content = input_file.read()

    for section in profiles_conf.sections():
        name = profiles_conf.get(section, 'Name', fallback=None)
        if profile_name and name != profile_name:
            continue
        path = profiles_conf.get(section, 'Path', fallback=None)
        if path:
            prefs_file = os.path.join(os.path.expanduser('~/.mozilla/firefox'), path, 'user.js')
            with open(prefs_file, "w") as output_file:
                output_file.write(prefs_content)
            print(f"Copied preferences to {prefs_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy Firefox preferences to specified profile.")
    parser.add_argument('--profile', type=str, help='Name of the profile to copy preferences to. Defaults to \'default\'.', default='default')
    parser.add_argument('--all', action='store_true', help='Copy preferences to all profiles.')
    args = parser.parse_args()
    profile_arg = None if args.all else args.profile
    main(profile_arg)
