#!/usr/bin/env bash
# Forward all options to the shared Python 3.8+ counter.
set -eu

case "$0" in
    */*) script_dir=${0%/*} ;;
    *) script_dir=. ;;
esac
script_dir=$(CDPATH= cd -- "$script_dir" && pwd)
for python_command in python3 python; do
    if command -v "$python_command" >/dev/null 2>&1 &&
       "$python_command" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' >/dev/null 2>&1; then
        exec "$python_command" "$script_dir/count-software.py" "$@"
    fi
done
printf '%s\n' 'Python 3.8 or newer is required. Install Python and make it available on PATH.' >&2
exit 2
