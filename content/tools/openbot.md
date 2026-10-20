---
title: "OpenBot: 로컬 퍼스트 AI 코워커 & 자율 에이전트 워크스페이스"
date: 2026-10-20
tags:
  - openbot
  - agents
  - local-first
  - coworker
  - tools
---

> [!NOTE] 핵심 요약
> **OpenBot**([openbot.run](https://openbot.run/))은 **지속형 AI 에이전트(AI Coworkers)를 로컬 환경에서 구동하고 협업할 수 있도록 설계된 오픈소스 로컬 퍼스트 데스크톱/모바일 플랫폼**입니다. Claude, Gemini, Grok, Codex 등 다양한 상용 및 오픈소스 LLM을 자체 구독 계정(BYO)으로 연결하여, 전용 컴퓨터 권한(쉘 실행, 파일 시스템, 브라우저 자동화)을 갖춘 AI 동료들과 팀 단위로 협업할 수 있습니다.

---

## 1. OpenBot이 해결하는 문제

단순한 일회성 대화형 챗봇(ChatGPT 웹 UI 등)은 브라우저 탭을 닫으면 세션 맥락이 단절되고, 로컬 개발 환경이나 실제 파일 시스템에 직접 접근하지 못합니다. 반대로 CLI 전용 코딩 에이전트는 일반 팀원이나 모바일 환경에서의 접근성이 떨어집니다.

**OpenBot**은 이 두 세계의 장점을 결합하여:
1. **지속성(Persistence)**: 백그라운드에서 프로젝트 상태를 기억하고 작업을 이어가는 에이전트
2. **실제 실행력(Execution)**: 쉘 스크립트 실행, 파일 입출력, 브라우저 제어 권한을 가진 전용 워크스페이스
3. **멀티플랫폼 협업(Multiplayer & Companion App)**: 데스크톱 앱뿐만 아니라 iOS/Android 모바일 앱을 통해 언제 어디서나 에이전트에게 업무를 위임하고 모니터링할 수 있는 통합 환경을 제공합니다.

---

## 2. 주요 아키텍처 및 핵심 기능

### 1) BYO(Bring Your Own) 구독 모델
- 플랫폼 자체의 과도한 중간 마진 없이, 사용자가 이미 결제하고 있는 Anthropic Claude Pro, OpenAI ChatGPT Plus, Google Gemini Advanced 계정이나 개인 API 키를 직접 연동하여 사용합니다.

### 2) 독립된 에이전트 컴퓨터(Dedicated Agent Workspaces)
- 각 에이전트에게 전용 역할(Role), 시스템 프롬프트, 작업 디렉토리, 샌드박스 권한을 부여할 수 있습니다.
- 예: 프론트엔드 빌드 전담 에이전트, 백엔드 테스트 에이전트, 리서치 & 브라우징 전담 에이전트.

### 3) 거버넌스 및 보안 정책(Policy Controls & Audit Log)
- 에이전트가 위험한 쉘 명령어(`rm -rf`, 외부 네트워크 요청 등)를 실행하기 전에 사용자 승인을 요구하는 가드레일과 전체 작업 감사 로그(Audit Trail)를 로컬에 기록합니다.

### 4) 모바일 컴패니언 앱 연동
- 데스크톱에서 돌아가고 있는 에이전트의 작업 진행 상황을 스마트폰(iOS/Android)에서 실시간 푸시 알림으로 확인하고, 이동 중에도 추가 지시를 내릴 수 있습니다.

---

## 3. 대표적인 활용 시나리오

| 역할 | 업무 내용 | 연동 도구 |
| :--- | :--- | :--- |
| **자동화 QA 엔지니어** | 저장소 커밋 감지 시 E2E 테스트 실행 및 실패 스크린샷 보고 | Bash, Playwright, Git |
| **시장/기술 리서처** | 매일 아침 특정 기술 트렌드 웹사이트 크롤링 및 요약 마크다운 생성 | Headless Browser, RAG |
| **코드 리팩토링 동료** | 대규모 레거시 코드의 타입스크립트 마이그레이션 작업 분할 수행 | Node.js, Git Worktree |

---

## 4. 공식 리소스 및 링크
- 🌐 **공식 웹사이트**: [https://openbot.run/](https://openbot.run/)
- 📱 **지원 플랫폼**: macOS, Windows, Linux, iOS(TestFlight), Android
- 📦 **라이선스**: 오픈소스 (Open-Source)
