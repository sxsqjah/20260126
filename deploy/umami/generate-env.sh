#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [[ -e .env ]]; then
  echo "Refusing to overwrite existing .env" >&2
  exit 1
fi

umask 077
db_password="$(openssl rand -hex 24)"
app_secret="$(openssl rand -hex 32)"
admin_password="$(openssl rand -hex 18)"

sed \
  -e "s/replace-with-a-random-password/${db_password}/" \
  -e "s/replace-with-a-random-secret/${app_secret}/" \
  -e "s/replace-with-a-random-admin-password/${admin_password}/" \
  .env.example > .env

chmod 600 .env
echo "Created root-only Umami environment file."
