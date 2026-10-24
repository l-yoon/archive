---
publish: true
title: "Claude Code와 Plugin: 터미널 코딩 에이전트 완벽 정리"
date: 2026-10-20
tags:
  - claude-code
  - ai-tools
  - plugins
  - agentic-coding
  - mcp
---

에디터 옆에서 몇 줄 자동완성해 주는 Copilot 시대는 끝났다.  
**Claude Code**는 터미널에서 코드베이스 전체를 혼자 탐색하고, 파일을 수정하고, `npm test`를 돌려 에러가 안 날 때까지 스스로 고치는 자율형 코딩 CLI다.

---

### Plugin은 왜 필요한가?
Claude Code가 아무리 똑똑해도 우리 팀의 DB, 사내 API, 배포 규칙은 모른다.  
예전에는 이걸 쓰려면 MCP JSON을 손으로 고치고, 프롬프트 복사하고, 쉘 스크립트를 따로 짰다.

**Plugin은 이 모든 걸 패키지 하나로 묶어 `/plugin install` 한 줄로 끝내는 확장 규격이다:**

1. **Skills**: 특정 프레임워크나 사내 코딩 컨벤션 지침
2. **MCP Connectors**: PostgreSQL DB, Playwright 브라우저, GitHub 이슈 등 외부 도구 연동
3. **Subagents**: 메인 대화창 컨텍스트를 망치지 않고 백그라운드에서 보안 검사나 테스트만 전담하는 서브 에이전트
4. **Hooks**: `git commit` 직전에 API 키 유출을 막는 등의 이벤트 트리거

---

### 수동 설정 vs 플러그인
- **수동 설정**: 팀원마다 `claude_desktop_config.json` 복사-붙여넣기하다 경로 깨지고 버전 꼬임.
- **플러그인**: `marketplace.json`에 등록해두고 명령어 한 줄로 전사 개발 환경 통일.

```bash
# 마켓플레이스 등록 및 설치
claude plugin marketplace add <owner/repo>
claude plugin install <plugin-name>
```

---

### 결론
Claude Code를 단순 챗봇으로 쓰지 말고, **MCP + Skills + Subagents가 묶인 플러그인을 붙여 우리 팀에 맞는 전용 주니어 개발자로 커스텀해서 쓰는 것**이 핵심이다.
