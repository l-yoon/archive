---
publish: true
title: "REA: AI 에이전트에게 Ghidra와 IDA를 쥐어주는 리버스 엔지니어링 도구"
date: 2026-10-20
tags:
  - rea
  - reverse-engineering
  - mcp
  - agents
  - security
---

[morluto/rea](https://github.com/morluto/rea)는 Claude Code나 Cursor 같은 코딩 에이전트에게 바이너리 역공학 도구를 달아주는 오픈소스 MCP 프레임워크다.

---

### 무엇을 해결하는가?
LLM에게 컴파일된 바이너리(`.dylib`, `.exe`, ELF)나 Electron 앱을 분석하라고 하면 대부분 뇌피셜(할루시네이션)을 뱉는다.

REA는 에이전트가 직접 디컴파일러 엔진을 다루게 만든다:
- **Ghidra / IDA Pro 연동**: 에이전트가 C 의사코드 디컴파일, 메모리 주소 심볼, 교차 참조(Xref)를 MCP 도구로 직접 조회한다.
- **Electron 정적 분석**: `app.asar` 패키지를 뜯어서 난독화된 JS 번들과 숨겨진 내부 IPC 채널, 비공개 API 엔드포인트를 정적으로 역추적한다.
- **구조화된 증거 제공**: 단순 텍스트 덤프가 아니라 함수 호출 그래프와 데이터 타입을 JSON으로 넘겨 에이전트의 오판을 줄인다.

---

### 한 줄 사용법
```bash
npx rea-agents setup
```
설정하면 Claude Code에서 즉시 `rea_decompile_function`, `rea_inspect_asar` 같은 도구가 활성화된다.

---

### 결론
소스코드 유실된 레거시 바이너리 스펙을 복원하거나, 서드파티 데스크톱 앱의 내부 통신 규격을 까봐야 할 때 에이전트 손에 쥐여주기 가장 좋은 도구다.
