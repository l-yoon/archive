---
title: "Aside: 브라우저를 조종하는 AI와 실시간 미팅 커닝페이퍼"
date: 2026-10-20
tags:
  - aside
  - ai-browser
  - agent
  - meeting-copilot
  - mcp
  - tools
---

Aside([aside.com](https://aside.com) / [meetaside.com](https://meetaside.com))는 YC 출신 팀이 만든 프로덕트로, 핵심 축은 두 가지다:
1. **Aside Browser**: 내 브라우저 세션 그대로 써서 다단계 웹 업무를 대행하는 AI 브라우저
2. **Aside Copilot**: 화상 미팅이나 면접 중 질문을 듣고 실시간 큐카드를 띄워주는 코파일럿

---

### 1. Aside Browser ([aside.com](https://aside.com))
API 없는 어드민 페이지, 사내 인트라넷, 복잡한 SaaS 대시보드 조작을 사람처럼 대행한다.
- **내 로그인 세션 재사용**: 크롤러가 아니라 실제 Chromium 브라우저라 내가 로그인해 둔 쿠키와 세션을 그대로 쓴다.
- **내 구독 연동 (BYO Subscription)**: 비싼 전용 크레딧을 강제하지 않는다. 기존에 쓰던 Claude Pro나 ChatGPT Plus 계정을 브라우저에 그대로 꽂을 수 있다.
- **패스워드 안전 보장**: 비밀번호를 모델 프롬프트에 텍스트로 노출하지 않고 자체 키체인 매니저가 중개한다.
- **Claude Code / Cursor 연동 (MCP)**: 개발자 입장에서 가장 강력한 기능이다. 터미널에서 "방금 띄운 로컬 서버 회원가입 페이지 들어가서 UI 버그 재현하고 콘솔 로그 가져와" 하면 Aside 브라우저가 직접 실행해서 조작하고 결과를 리포트한다.

---

### 2. Aside Copilot ([meetaside.com](https://meetaside.com))
맥/윈도우 데스크톱 앱으로 구동되는 실시간 대화 보조 도구.
- 상대방이 질문을 던지는 순간 로컬 오디오를 인식해서 핵심 수치, 답변 힌트, 사전 메모를 화면 구석에 띄워준다.
- 기술 면접이나 클라이언트 세일즈 콜에서 기억 안 나는 세부 스펙을 즉시 확인할 때 효과적이다.

---

### 결론
웹 반복 노가다(어드민 수치 취합, E2E 화면 테스트)를 AI에게 통째로 위임하고 싶다면 Aside Browser는 현재 나온 도구 중 가장 실용적이다.
