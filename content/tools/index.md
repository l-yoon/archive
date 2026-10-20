---
title: Tools
tags:
  - tools
  - ai-tools
  - productivity
  - dev-tools
---

> [!NOTE] 큐레이션 원칙
> 단순한 유행성 서비스 나열이 아닌, **실제 업무와 개발에 유의미한 생산성 향상을 검증한 AI 도구 및 개발 도구**들을 선별하여 기록하고 비교 분석하는 공간입니다.

---

## ⚡ 실무 검증 도구 퀵 매트릭스

| 도구명 | 카테고리 | 핵심 강점 | 추천 활용 시점 |
| :--- | :--- | :--- | :--- |
| **Claude Code** | 에이전틱 코딩 CLI | 터미널 기반 자동 코드 탐색 및 대규모 리팩토링 | 로컬 저장소 전체 분석, CLI 기반 빌드/테스트 루프 |
| **Cursor** | IDE 통합 코딩 | 프로젝트 전역 인덱싱 및 멀티 파일 수정 | 코드베이스 탐색, 인라인 자동완성 |
| **Google AI Edge Foresight** | 온디바이스 AI 미팅 | Gemma 4 기반 로컬 완전 오프라인 전사 & RAG | 기밀 회의, 네트워크 없는 비행기/이동 중 회의 요약 |
| **REA** | 리버스 엔지니어링 에이전트 | AI 에이전트 전용 Ghidra/IDA 바이너리 분석 MCP | 바이너리 리버스 엔지니어링, Electron 패키지 정밀 분석 |
| **OpenBot** | 오픈소스 멀티 에이전트 | 독립 워크스페이스 분리형 개인 맞춤 에이전트 동료 | 사내 팀 협업, 개인화된 자율 업무 대리 |
| **Anarlog** | 로컬 퍼스트 회의록 | 봇 없는 시스템 오디오 캡처 & 로컬 SQLite/MD 저장 | 외부 봇 거부감 있는 회의, 옵시디언/로컬 연동 |
| **Aside** | AI 브라우저 & 코파일럿 | 인간처럼 웹 세션 직접 조작 + 실시간 미팅 큐카드 | 다단계 웹 대시보드 자동화, 기술 면접/세일즈 실시간 보조 |
| **OpenRouter** | LLM 라우팅 | 단일 API 키로 수십 개 모델 스위칭 & 폴백 | 모델별 가성비 비교, 다운타임 없는 백업 |
| **Langfuse** | 옵저버빌리티 | LLM 호출 트레이싱, 토큰 비용 및 레이턴시 모니터링 | 프로덕션 API 비용 및 품질 추적 |

---

## 📌 주요 아티클 & 실무 가이드
* 📖 **[[tools/claude-code-and-plugins|Claude Code와 Plugin 생태계 완벽 가이드]]**: 에이전틱 코딩 CLI의 작동 원리와 Skills, MCP, Subagents, Hooks를 하나로 묶는 플러그인 아키텍처 심층 분석
* 📖 **[[tools/google-ai-edge-foresight|Google AI Edge Foresight: 온디바이스 로컬 AI 미팅 & 지식 베이스]]**: Apple Silicon Mac 위에서 Gemma 4와 EmbeddingGemma 2로 구동되는 오프라인 미팅 어시스턴트
* 📖 **[[tools/rea|REA: 리버스 엔지니어링 에이전트 도구 완벽 분석]]**: Ghidra와 IDA Pro를 Claude Code / Cursor에 연결하는 역공학 에이전트 MCP 프레임워크
* 📖 **[[tools/openbot|OpenBot: 로컬 퍼스트 오픈소스 멀티 에이전트 동료 플랫폼]]**: 내 컴퓨터에서 실행되는 오픈소스 자율형 멀티 에이전트 워크스페이스
* 📖 **[[tools/anarlog|Anarlog: 봇 없는 로컬 퍼스트 AI 회의록 & 지식 관리 도구]]**: 회의에 봇을 초대하지 않고 시스템 오디오로 직접 캡처하는 로컬 마크다운 회의록 도구 (구 Hyprnote)
* 📖 **[[tools/aside|Aside: AI 브라우저 에이전트와 실시간 미팅 코파일럿]]**: 다단계 웹 워크플로우를 대행하는 AI 전용 브라우저와 실시간 대화 지원 코파일럿
