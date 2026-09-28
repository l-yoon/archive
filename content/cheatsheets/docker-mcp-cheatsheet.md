---
title: Docker & MCP 서버 실무 운영 치트시트
tags:
  - cheatsheet
  - docker
  - mcp
  - devops
---

> [!NOTE] 용도
> AI 에이전트 구동 및 로컬 MCP 서버 격리를 위한 핵심 명령어 및 설정 템플릿입니다.

---

## 1. Docker 핵심 운영 명령어

### 컨테이너 및 이미지 정리
```bash
# 중지된 모든 컨테이너, 미사용 네트워크, 댕글링 이미지 일괄 정리
docker system prune -f

# 미사용 볼륨까지 완전 정리 (주의: 데이터 삭제)
docker system prune -a --volumes -f

# 특정 컨테이너 리소스 사용량(CPU/Memory) 실시간 모니터링
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
```

---

## 2. MCP 서버용 Dockerfile 템플릿

```dockerfile
# Node.js 22 LTS Alpine 경량 이미지
FROM node:22-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

COPY package*.json ./
RUN npm ci --only=production

COPY --from=builder /app/dist ./dist

# Non-root 사용자 격리
USER node

# Stdio 표준 입출력 프로세스 실행
CMD ["node", "dist/index.js"]
```

---

## 3. Claude Code / AI IDE용 MCP 설정 JSON (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/chanminyoon/Documents"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..."
      }
    }
  }
}
```
