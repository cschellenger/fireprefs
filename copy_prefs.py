#!/usr/bin/env python3
import argparse
from configparser import ConfigParser
from pathlib import Path
import platform

def read_prefs(file_path):
    config = ConfigParser()
    config.read(file_path)
    return config

def main(profile_name=None):
    if platform.system() == 'Darwin':
        # macOS
        config_dir = Path.home() / 'Library' / 'Application Support' / 'Firefox'
    else:
        # Linux, etc
        config_dir = Path.home() / '.mozilla' / 'firefox'
        
    if not config_dir.exists():
        config_dir = Path.home() / '.config' / 'mozilla' / 'firefox'

    profiles_file = config_dir /  'profiles.ini'
    print(f"Attempting to load {profiles_file}")
    
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
            prefs_file = config_dir / path / 'user.js'
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
