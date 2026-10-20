---
title: 실무 AI Tools 큐레이션 & 워크플로우
tags:
  - ai-tools
  - productivity
  - workflow
---

> [!NOTE] 큐레이션 원칙
> 단순한 유행성 서비스 나열이 아닌, **실제 업무와 개발에 유용한 생산성 향상을 검증한 AI 도구**들을 선별하여 기록하고 비교 분석하는 공간입니다.

---

## 🛠️ 주요 관심 도구 영역

```mermaid
graph TD
    Tools[AI Tools Hub] --> Coding[💻 코딩 & 에이전트]
    Tools --> Infra[⚡ LLM 서빙 & 인프라]
    Tools --> Research[🔬 리서치 & 지식 관리]
    Tools --> Prototyping[🎨 UI/UX 프로토타이핑]

    Coding --> C1[Claude Code / Cursor]
    Infra --> I1[OpenRouter / Langfuse]
    Research --> R1[Perplexity / NotebookLM]
    Prototyping --> P1[v0 / Bolt.new]

    classDef tool fill:#284b63,stroke:#fff,stroke-width:1px,color:#fff;
    class Tools,Coding,Infra,Research,Prototyping tool;
```

---

## ⚡ 추천 도구 퀵 매트릭스

| 도구명 | 카테고리 | 핵심 강점 | 추천 활용 시점 |
| :--- | :--- | :--- | :--- |
| **Claude Code** | 에이전틱 코딩 CLI | 터미널 기반 자동 코드 탐색 및 대규모 리팩토링 | 로컬 저장소 전체 분석, CLI 기반 빌드/테스트 루프 |
| **Cursor** | IDE 통합 코딩 | 프로젝트 전역 인덱싱 및 멀티 파일 수정 | 코드베이스 탐색, 인라인 자동완성 |
| **OpenRouter** | LLM 라우팅 | 단일 API 키로 수십 개 모델 스위칭 & 폴백 | 모델별 가성비 비교, 다운타임 없는 백업 |
| **Langfuse** | 옵저버빌리티 | LLM 호출 트레이싱, 토큰 비용 및 레이턴시 모니터링 | 프로덕션 API 비용 및 품질 추적 |

---

## 📌 주요 아티클 & 실무 가이드
* 📖 **[[ai-tools/claude-code-and-plugins|Claude Code와 Plugin 생태계 완벽 가이드]]**: 에이전틱 코딩 CLI의 원리와 Skills, MCP, Subagents, Hooks를 묶는 플러그인 아키텍처

---

## 📝 새 도구 리뷰 작성법
이 폴더(`content/ai-tools/`)에 도구 사용기 또는 비교 분석 마크다운 파일을 생성하면 탐색기 목록에 자동 추가됩니다.
