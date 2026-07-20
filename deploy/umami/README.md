# CKQPRO Analytics Deployment

This directory contains the self-hosted Umami and PostgreSQL deployment used
by the CKQPRO website.

## Architecture

- The website loads `https://stats.ckqpro.com/ck.js`.
- Umami listens only on `127.0.0.1:3000`.
- PostgreSQL is available only inside the Docker network.
- Nginx proxies the analytics hostname to Umami.
- Cloudflare Tunnel publishes the hostname without opening inbound ports.
- Docker and cloudflared are configured to recover after a server restart.

## Initial deployment

```bash
cd /root/Ckqpro-GW/deploy/umami
./generate-env.sh
docker compose up -d
node bootstrap.mjs
```

Install `deploy/nginx/stats.ckqpro.com.conf` as an enabled Nginx site. Copy
`deploy/cloudflared/config.yml.example` to `/etc/cloudflared/config.yml`, then
replace the Tunnel placeholders with the credentials created by cloudflared.

## Administrator access

Open <https://stats.ckqpro.com> and sign in as `admin`. The generated admin
password is stored in the root-only `.env` file:

```bash
sed -n 's/^UMAMI_ADMIN_PASSWORD=//p' /root/Ckqpro-GW/deploy/umami/.env
```

Umami includes Simplified Chinese. Select `admin` → `Language` → `中文` in the
dashboard; the preference is saved in that browser.

## Operations

```bash
cd /root/Ckqpro-GW/deploy/umami
docker compose ps
docker compose logs --tail=100 umami
docker compose restart umami
```

Never commit `.env`, administrator/database passwords, `cert.pem`, or the
Cloudflare Tunnel credentials JSON file.
