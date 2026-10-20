---
title: "Anarlog: 봇 없는 로컬 퍼스트 AI 회의록 & 지식 관리 도구"
date: 2026-10-20
tags:
  - anarlog
  - hyprnote
  - local-first
  - meeting-notes
  - mcp
---

> [!NOTE] 핵심 요약
> **Anarlog**(구 *Hyprnote*, [anarlog.so](https://anarlog.so))는 **화상회의에 어색한 AI 봇을 초대하지 않고, 데스크톱에서 직접 시스템 오디오와 마이크를 캡처하는 오픈소스 로컬 퍼스트(Local-First) AI 미팅 노트 도구**입니다. Granola, Otter.ai의 강력한 대안으로, 모든 회의록과 녹음 데이터를 로컬 SQLite 및 마크다운 파일로 온전히 소유할 수 있으며, 개발자를 위한 CLI와 MCP(Model Context Protocol) 연동을 지원합니다.

---

## 1. 문제의식: 기존 AI 회의록 서비스들의 피로감

대부분의 상용 AI 회의 도구(Otter, Fireflies, Fathom 등)는 다음과 같은 고질적인 문제점을 안고 있습니다:
1. **회의 참석자들의 거부감**: 회의실에 예고 없이 `Otter.ai Notetaker`라는 이름의 봇 계정이 입장하여 다른 참석자들에게 감시받는 듯한 불편함을 줌
2. **사내 보안 및 개인정보 유출**: 음성 데이터가 서드파티 클라우드 서버에 전송되고 저장되어 민감한 비즈니스 대화 유출 위험 상존
3. **데이터 종속성**: 작성된 회의록이 서비스 자체 플랫폼에 갇혀 있어, 기존 옵시디언(Obsidian)이나 노션 등 개인 지식 베이스로 자유롭게 가져오기 어려움

**Anarlog**는 이러한 피로감을 해소하기 위해 **"외부 봇 없이(No-Bot), 로컬에 저장하며(Local-First), 개발자 친화적인(Developer-Centric)"** 설계 원칙을 내세웠습니다.

---

## 2. 핵심 아키텍처 및 특징

### 1) 시스템 레벨 네이티브 오디오 캡처
- 별도의 가상 봇 계정을 미팅에 부르지 않습니다.
- 데스크톱 오디오 드라이버와 마이크 입력을 앱에서 직접 캡처하므로, Zoom, Google Meet, Slack Huddle, Discord, 심지어 오프라인 대면 회의에서도 동일하게 작동합니다.

### 2) 로컬 SQLite & Markdown 기반 데이터 소유권
- 녹음 파일과 텍스트 전사 데이터는 사용자 컴퓨터의 SQLite 데이터베이스와 순수 Markdown(`.md`) 파일로 저장됩니다.
- 클라우드 계정이 정지되거나 서비스가 종료되어도 내 모든 회의 자산은 그대로 유지됩니다.

### 3) 자유로운 AI 모델 선택 (BYO API & Local LLM)
- 사용자의 니즈와 보안 수준에 따라 음성 인식(STT)과 요약 모델을 자유롭게 교체할 수 있습니다:
  - 최고 품질: OpenAI Whisper API, Anthropic Claude 3.5 Sonnet
  - 완전한 로컬 오프라인: 로컬 Whisper.cpp, Ollama 기반 오픈소스 LLM

### 4) 개발자를 위한 확장성 (CLI, Webhook, MCP)
- **Model Context Protocol (MCP)**: Claude Code나 Cursor 같은 AI 코딩 에이전트가 "오늘 오전 아키텍처 회의에서 결정된 DB 스키마 내용 확인해줘"와 같은 명령으로 회의록 DB를 직접 조회 가능
- **Webhooks**: 회의 종료 시 사내 슬랙 채널이나 Notion DB로 마크다운 요약본 자동 전송

---

## 3. 대표적인 기능 비교

| 비교 항목 | 전통적 클라우드 도구 (Otter, Fireflies) | Granola | **Anarlog** |
| :--- | :--- | :--- | :--- |
| **봇 참여 여부** | 봇 계정이 회의방에 직접 입장 | 봇 없음 (로컬 캡처) | **봇 없음 (로컬 캡처)** |
| **데이터 저장소** | 공급업체 클라우드 서버 | 로컬/하이브리드 (독점 포맷) | **100% 로컬 (SQLite, Markdown)** |
| **소스코드 공개** | 비공개 (Closed-source) | 비공개 (Closed-source) | **오픈소스 (Open-source)** |
| **개발자 도구 (MCP/CLI)** | 제한적 API | 미지원 | **공식 지원 (MCP, CLI, Webhook)** |

---

## 4. 실무 활용 팁
- **옵시디언(Obsidian) 디지털 가든과 연동**: Anarlog의 저장 폴더를 Obsidian 볼트(`Vault`)로 지정하면, 회의가 끝나는 즉시 새로운 마크다운 회의록이 지식 그래프에 자동으로 통합됩니다.
- **에이전틱 워크플로우**: 코딩 에이전트(Claude Code)에게 Anarlog의 MCP 서버를 연결하여, 제품 기획 회의에서 나온 피드백을 기반으로 버그 티켓을 즉시 생성하도록 자동화할 수 있습니다.
