#!/usr/bin/env bash
# Helper shortcut untuk mengelola agent skills via skills.sh
# Penggunaan:
#   ./skills.sh list
#   ./skills.sh find <keyword>
#   ./skills.sh add <owner/repo@skill> -y --copy

npx skills "$@"
