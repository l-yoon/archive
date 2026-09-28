---
title: 엔지니어링 관점의 프롬프트 패턴 & Structured Outputs
tags:
  - ai
  - prompt-engineering
  - structured-outputs
  - json-schema
---

> [!NOTE] 핵심
> 프로덕션 레벨의 LLM 파이프라인에서 "자연어 프롬프트 깎기"는 지양되어야 합니다. **명확한 스키마(JSON Schema), 엄격한 제약조건, 그리고 검증 루프**를 코드화하는 것이 결정론적 시스템 구축의 핵심입니다.

---

## 1. Structured Outputs (구조화된 출력 보장)

최신 LLM(OpenAI Structured Outputs, Anthropic Tool Use, Gemini Controlled Generation)은 JSON Schema를 기반으로 토큰 생성 시점에 마스킹을 적용해 100% 문법 유효성을 보장합니다.

### Pydantic 모델 정의 예시
```python
from pydantic import BaseModel, Field
from typing import List, Literal

class ActionItem(BaseModel):
    priority: Literal["P0", "P1", "P2"]
    task: str = Field(description="구체적이고 측정 가능한 단일 실행 과제")
    estimated_hours: float

class PRDAnalysisResult(BaseModel):
    summary: str
    risk_factors: List[str]
    action_items: List[ActionItem]
    confidence_score: float = Field(ge=0.0, le=1.0)
```

---

## 2. 4대 실무 프롬프트 패턴

### ① Chain-of-Thought (생각의 사슬) 분리
* 최종 답변을 바로 생성하게 하지 않고, `<thinking>` 또는 `reasoning` 필드를 강제하여 중간 추론 단계를 명시하도록 구성.
* 논리 오류 및 할루시네이션(환각) 발생률을 크게 억제.

### ② Few-Shot 가이드라인 (엣지 케이스 중심)
* 정상 케이스만 예시로 주면 실패함. 모델이 흔히 헷갈려하는 **경계 조건(Boundary Cases)** 2~3개를 명시해야 함.

### ③ XML Tagging 기반 프롬프트 구조화
* 시스템 지침, 배경 컨텍스트, 사용자 입력, 출력 포맷을 XML 태그로 엄격히 분리:
```markdown
<instruction>
너는 시니어 B2B SaaS 테크 PM이다. 아래 제공된 [raw_logs]를 분석하여 장애 원인을 규명하라.
</instruction>

<context>
- 대상 시스템: 결제 게이트웨이 연동 서비스
- 허용 에러 임계치: 0.1%
</context>

<raw_logs>
{{LOGS}}
</raw_logs>

<output_format>
JSON Schema에 맞춰 출력하라.
</output_format>
```

---

## 3. 회귀 테스트 (Prompt Regression Testing)

프롬프트를 수정할 때마다 전체 벤치마크 데이터셋에 대해 자동 평가를 수행해야 합니다:
* **LLM-as-a-Judge**: 상위 모델(GPT-4o / Claude 3.5 Sonnet)을 통해 기준 정답과 생성물의 일치도 평가.
* **Exact Match & Schema Validity**: 필수 키 누락 여부, 값의 유효 범위 검사.
