#!/usr/bin/env python3

__prog__ = "telegram-export-channel-links"
__version__ = "0.0.1"
__desc__ = "Export public channel and group links of telegram account."

import argparse

from telethon.sync import TelegramClient


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
    args = parser.parse_args()

    with TelegramClient(__prog__, args.app_id, args.app_hash) as client:
        def write_dialog(dialog):
            try:
                username = client.get_entity(dialog.id).username
                if username:
                    print(
                        "https://t.me/", client.get_entity(dialog.id).username, sep=""
                    )
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
