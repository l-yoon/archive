---
title: 실무 Git 고급 명령어 & 브랜치 복구
tags:
  - cheatsheet
  - git
  - dev-tools
---

> [!NOTE] 용도
> 커밋 유실, 브랜치 충돌, 히스토리 재작성 시 필요한 비상 복구 및 실무 Git 테크닉입니다.

---

## 1. 비상 복구: 삭제된 커밋 및 브랜치 되살리기

```bash
# 1. 모든 HEAD 이동 기록 확인 (커밋 해시 추적)
git reflog

# 2. 원하는 시점(예: HEAD@{2})으로 강제 복구
git reset --hard HEAD@{2}

# 3. 실수로 지운 브랜치 부활
git checkout -b <복구할-브랜치명> <커밋해시>
```

---

## 2. 히스토리 다듬기 (Interactive Rebase)

```bash
# 최근 3개 커밋 합치기(Squash) 또는 수정
git rebase -i HEAD~3

# 특정 커밋 하나만 현재 브랜치로 가져오기
git cherry-pick <커밋해시>

# 특정 커밋의 변경사항을 취소하는 역커밋 생성
git revert <커밋해시>
```

---

## 3. 원격 동기화 & 충돌 해결

```bash
# 로컬 변경사항 임시 저장 및 복원
git stash push -m "작업중_임시저장"
git stash pop

# 원격 브랜치 변경사항을 깔끔하게 재정렬하여 가져오기
git pull --rebase origin main
```
