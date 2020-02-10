# Telegram Bot for Prometheus

#### Config file example
/etc/telegram-alert-bot/config.yml
```yaml
---
token: 980053000:AAEqe7N337bLfGYG_5pnusW-QOtHLU7XxLo
chat_id: -336668500
proxies:
  all: "http://user:password@proxy.domain.com:3128"
```

#### telegram bot
##### Create bot
On phone

@BotFather<br/>
/newbot<br/>
add bot to chat

get chat_id
```bash
curl https://api.telegram.org/bot<Bot token>/getUpdates
```

#### docker-compose.yml

```yaml
  telegram-alert-bot:
    image: zaratik/telegram-alert-bot
    ports:
      - 8075:8075
    volumes:
      - ./telegram-alert-bot/config.yml:/etc/telegram-alert-bot/config.yml
    networks:
      - back-tier
    restart: always
```

#### Alertmanager Configuration
```yml
route:
  group_wait: 20s
  group_interval: 20s
  repeat_interval: 60s
  receiver: telegram-alert-bot
receivers:
- name: telegram-alert-bot
  webhook_configs:
  - send_resolved: true
    url: 'http://telegram-alert-bot:8075'

```