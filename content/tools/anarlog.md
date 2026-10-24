---
publish: true
title: "Anarlog: 봇 없는 로컬 퍼스트 AI 회의록 (구 Hyprnote)"
date: 2026-10-20
tags:
  - anarlog
  - hyprnote
  - local-first
  - meeting-notes
  - mcp
---

화상회의에 어색하게 "Otter Notetaker 봇" 초대하지 않고, 맥/PC 시스템 오디오를 직접 캡처하는 오픈소스 회의록 도구 ([anarlog.so](https://anarlog.so)).

---

### 왜 쓰는가?
1. **봇이 없다**: Zoom, Google Meet, Slack Huddle 어디든 눈치 안 보고 내 컴퓨터 소리만 조용히 딴다. 상대방에게 불필요한 감시 피로감을 주지 않는다.
2. **데이터가 내 컴퓨터에 남는다**: 녹음과 요약본이 SQLite와 마크다운(`.md`) 파일로 로컬 저장된다. 회의 끝나면 내 옵시디언(Obsidian) 볼트에 바로 꽂힌다.
3. **내 API 키 연동 (BYOK)**: Whisper API나 Claude 3.5 Sonnet을 직접 붙여 퀄리티를 최대로 뽑거나, 완전 무료/오프라인으로 Whisper.cpp를 돌릴 수 있다.
4. **개발자 친화적 (MCP 지원)**: MCP 서버가 기본 제공된다. Claude Code나 Cursor에서 "오늘 회의록에서 결정된 DB 스키마 찾아줘" 하면 바로 읽어온다.

---

### 한 줄 평
Granola의 폐쇄적인 저장 방식과 Otter의 봇 초대가 둘 다 질렸다면, 개발자 기준 가장 깔끔한 로컬 대안이다.
