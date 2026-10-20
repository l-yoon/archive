---
title: "REA (Reverse Engineer Anything): AI 에이전트를 위한 리버스 엔지니어링 툴킷"
date: 2026-10-20
tags:
  - rea
  - reverse-engineering
  - mcp
  - agents
  - security
---

> [!NOTE] 핵심 요약
> **REA(Reverse Engineer Anything with Agents)**는 [morluto/rea](https://github.com/morluto/rea)에서 개발한 오픈소스 툴킷으로, **Claude Code, Cursor, Codex 등 자율 코딩 에이전트에게 바이너리 분석 및 소프트웨어 리버스 엔지니어링 능력을 부여하는 MCP(Model Context Protocol) 기반 프레임워크**입니다. LLM의 추측성 답변(할루시네이션)을 배제하고, 실제 디컴파일러와 바이너리 분석 도구의 정밀한 구조화 데이터를 에이전트에 공급합니다.

---

## 1. 등장 배경: AI 에이전트와 리버스 엔지니어링의 한계

기존 AI 모델에게 컴파일된 실행 파일(`.exe`, `.dylib`, ELF)이나 패키징된 Electron 애플리케이션의 내부 로직을 질문하면, 모델은 과거 학습 데이터나 텍스트 확률에 의존해 부정확한 가설을 내놓기 일쑤였습니다.

**REA**는 AI 에이전트에게 '코드베이스 분석 도구'가 아닌 **'소프트웨어 고고학 발굴 도구'**를 쥐어주는 접근 방식을 취합니다. 에이전트가 터미널에서 바이너리를 열고, 함수 호출 그래프를 추적하며, 디컴파일된 의사 코드(Pseudocode)를 스스로 읽고 해석할 수 있도록 프로토콜 수준에서 연결합니다.

---

## 2. 주요 아키텍처 및 지원 엔진

### 1) 네이티브 바이너리 분석 엔진 연동
- **Ghidra / IDA Pro / Hopper**: 에이전트가 로컬 디컴파일러 엔진에 질의하여 특정 함수의 어셈블리, 크로스 레퍼런스(Xref), 문자열 테이블을 탐색합니다.
- **구조화된 증거 기반 전달**: 단순 텍스트 덤프가 아니라, 함수 호출 관계 그래프, 데이터 구조체 정의, 파라미터 타입 정보를 구조화된 JSON 데이터로 에이전트에게 반환합니다.

### 2) 웹 & Electron 애플리케이션 정적 분석
- 난독화된 자바스크립트 번들과 Electron의 `app.asar` 아카이브를 실행 없이 정적으로 언팩하고 AST(추상 구문 트리)를 분석합니다.
- 비공개 IPC 채널, 내부 API 엔드포인트, 클라이언트 사이드 검증 로직을 신속히 역추적합니다.

### 3) MCP(Model Context Protocol) 서버 기반 아키텍처
- Anthropic의 MCP 표준을 준수하므로, Claude Code, Cursor 등의 도구에서 설정 한 줄로 즉시 REA의 분석 도구들을 도구 호출(Tool Calling)로 사용할 수 있습니다.

---

## 3. 핵심 도구 및 명령어 인터페이스

```bash
# REA 에이전트 환경 원클릭 설치 및 MCP 연동
npx rea-agents setup
```

에이전트가 REA를 통해 사용하는 주요 내부 도구:
- `rea_decompile_function`: 특정 메모리 주소나 함수 심볼의 C 의사 코드 추출
- `rea_find_references`: 특정 문자열이나 전역 변수를 참조하는 호출 지점 검색
- `rea_inspect_asar`: Electron 패키지 내부 리소스 및 백엔드 핸들러 목록 분석
- `rea_trace_callgraph`: A 함수에서 B 함수로 도달하는 실행 경로 트레이싱

---

## 4. 실무 활용 사례

1. **레거시 비공개 시스템 분석**: 소스코드가 유실된 사내 C/C++ 레거시 라이브러리의 동작 스펙 복원
2. **보안 취약점 및 비밀 키 감사**: 상용 클라이언트 앱 내 하드코딩된 API 키, 취약한 암호화 알고리즘 역추적
3. **서드파티 소프트웨어 상호운용성 구축**: 공식 API 문서가 부실한 데스크톱 앱의 내부 통신 프로토콜을 분석하여 연동 커넥터 개발

---

## 5. 참고 링크
- 🐙 **GitHub Repository**: [morluto/rea](https://github.com/morluto/rea)
- 🔌 **연동 인터페이스**: Model Context Protocol (MCP) 표준 호환
