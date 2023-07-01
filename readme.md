# Termiddit
A simple TUI application for reading Reddit in the terminal.  

## Requirements
See `requirements.txt` for installation instructions.
- json
- requests
## Setup and running
1. Clone the repository into a directory: `git clone https://github.com/pixdoet/termiddit.git`
2. Make `main.py` executable (if not yet): `chmod +ux main.py`
3. (Optional) Edit `subreddits.json` to match your subreddit selections. View the guidelines at [json.md](/docs/json.md)
4. Launch termiddit with `./main.py`!

## Options
- `-s <subreddit>` view a single subreddit. Multireddit feature broken rn.
- `-l <json file>`: use a custom JSON feed.
- `-h`: print help

## License
Apache 2.0