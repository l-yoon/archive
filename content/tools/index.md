---
publish: true
title: Tools
tags:
  - tools
  - ai-tools
  - productivity
  - dev-tools
---

유행성 AI 도구 거르고, **실제 업무와 개발에 써보고 돈·시간 아낀 도구들만** 선별해둔 공간.

---

## ⚡ 실무 도구 퀵 매트릭스

| 도구 | 성격 | 핵심 한 줄 | 비고 |
| :--- | :--- | :--- | :--- |
| **Claude Code** | 코딩 CLI | 터미널에서 코드베이스 혼자 고치고 테스트 통과까지 자율 실행 | 필수 설치 |
| **Cursor** | 코딩 IDE | 코드베이스 전체 인덱싱 기반 멀티파일 수정 | VS Code 대안 |
| **Google Foresight** | 온디바이스 회의록 | 맥북 NPU로 100% 로컬 구동 (비행기 가능) | **한국어 미지원** |
| **Anarlog** | 로컬 회의록 | 봇 없이 컴퓨터 소리만 따서 마크다운/SQLite로 로컬 저장 | 구 Hyprnote |
| **Aside** | AI 브라우저/코파일럿 | 내 로그인 세션 그대로 웹 업무 대행 + 미팅 실시간 큐카드 | MCP 연동 |
| **REA** | 리버스 엔지니어링 | Claude Code에 Ghidra/IDA 붙여서 바이너리/Electron 분석 | MCP 프레임워크 |
| **OpenBot** | AI 동료 플랫폼 | 로컬 백그라운드에 띄워두고 모바일로 지시 내리는 동료봇 | 오픈소스 |
| **OpenRouter** | LLM 라우팅 | 단일 키로 모든 모델 스위칭 & 폴백 | 필수 게이트웨이 |
| **Langfuse** | 옵저버빌리티 | LLM 호출 트레이싱, 토큰 비용 및 레이턴시 모니터링 | 프로덕션 필수 |

---

## 📌 주요 도구 분석 노트
* 📖 **[[tools/claude-code-and-plugins|Claude Code와 Plugin]]**: 단순 자동완성을 넘어 자율 실행 CLI로 쓰는 법 & 플러그인 확장
* 📖 **[[tools/google-ai-edge-foresight|Google AI Edge Foresight]]**: 맥북 로컬 회의록. 아키텍처는 완벽하지만 한국어 지원이 안 되는 이유
* 📖 **[[tools/anarlog|Anarlog]]**: 화상회의에 어색한 봇 안 부르고 시스템 오디오 따는 로컬 마크다운 회의록
* 📖 **[[tools/aside|Aside]]**: 웹 로그인 세션 그대로 브라우저 조작하는 AI & 미팅 실시간 커닝페이퍼
* 📖 **[[tools/rea|REA]]**: AI 에이전트한테 Ghidra와 IDA를 쥐어주는 리버스 엔지니어링 툴킷
* 📖 **[[tools/openbot|OpenBot]]**: 웹 챗봇 창 닫으면 끝나는 게 아니라 로컬에서 계속 일하는 AI 동료
