#!/usr/bin/env python3

__prog__ = "telegram-export-channel-links"
__version__ = "0.0.2"
__desc__ = "Export public channel and group links of telegram account."

import argparse
import os
import sys

from telethon.sync import TelegramClient
from telethon.utils import get_display_name


def main():
    parser = argparse.ArgumentParser(
        prog=__prog__,
        description=__desc__,
    )
    parser.add_argument(
        "--app-id",
        type=int,
        default=17349,
        help="Test credentials are used by default",
    )
    parser.add_argument(
        "--app-hash",
        type=str,
        default="344583e45741c457fe1862106095a5eb",
        help="Test credentials are used by default",
    )
    parser.add_argument(
        "--no-groups",
        action="store_true",
        help="Don't export group links",
    )
    parser.add_argument(
        "--no-channels",
        action="store_true",
        help="Don't export channel links",
    )
    parser.add_argument(
        "--names",
        action="store_true",
        help="Export channel names",
    )
    parser.add_argument(
        "file",
        metavar="FILE",
        type=str,
        nargs="?",
        help="File to export to (data is printed to stdout by default)",
    )
    args = parser.parse_args()

    try:
        import standardpaths

        standardpaths.configure(application_name=__prog__)
        data_dir = standardpaths.get_writable_path("data")
        os.makedirs(data_dir, exist_ok=True)
        session_file = os.path.join(data_dir, f"{__prog__}.session")
    except ImportError:
        session_file = None

    with TelegramClient(session_file or __prog__, args.app_id, args.app_hash) as client:

        if args.file:
            sys.stdout = open(args.file, "w")

        def write_dialog(dialog):
            try:
                entity = client.get_entity(dialog.id)
                if entity.username:
                    if args.names:
                        print(get_display_name(entity))
                    print("https://t.me/", entity.username, sep="")
            except AttributeError:
                pass

        if not args.no_groups:
            for dialog in client.iter_dialogs():
                if dialog.is_group:
                    write_dialog(dialog)

        if not args.no_channels:
            for dialog in client.iter_dialogs():
                if dialog.is_channel and not dialog.is_group:
                    write_dialog(dialog)


if __name__ == "__main__":
    main()
