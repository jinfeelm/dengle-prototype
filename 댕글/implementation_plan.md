# Dengle Platform - Diagnostic Hub & Admin Separation Plan

This plan details the implementation of a dedicated "Diagnostic Test Hub" (separating it from the learning problem bank) and the separation of Admin Input screens for Diagnostic tests vs. Problem Bank questions, with a cross-insertion feature.

## Proposed Changes

### 1. B2C Diagnostic Test Hub
#### [NEW] `diagnostic_hub.html`
- A dedicated landing/hub page for all Diagnostic Tests (진단테스트).
- **Hero Section**: Strong KNS messaging ("데이터로 입시 전략의 기준을 세우다!").
- **Test Categories**:
  - 예비고1 특목고 배치고사 (지원 전 최종점검)
  - 예비중1 Hello 내신 ("안녕 내신, 안녕 100점!")
  - 예비중3 Real 특목 ("리얼한 출제 논리, 리얼한 실전 감각!")
- **Process Overview**: KNS만의 5-STEP 정밀 평가 시스템 시각화.
- *Note:* This page is completely separate from the `test_prep.html` (Problem Bank / Training Hub) that we planned previously.

### 2. Admin Separation & Cross-Insertion
#### [MODIFY] [admin_input.html](file:///c:/Users/SsoHot/Desktop/%EB%8C%95%EA%B8%80/admin_input.html)
- Update the sidebar to clearly distinguish: "문제은행(학습용) 입력기" vs "진단테스트(평가용) 빌더".
- Add a new section in the form: **배포 설정 (Distribution Settings)**.
  - Checkbox: `[x] 진단테스트용 문항으로 등록`
  - Checkbox: `[x] 일반 문제은행(학습용)에도 동시 등록 (크로스 인서션)`
- This fulfills the requirement that the two systems are separate, but a question created for a diagnostic test can easily be copied/inserted into the general Problem Bank for later sale/training.

### 3. GVR Report Clarification
- The new [report_gvr.html](file:///c:/Users/SsoHot/Desktop/%EB%8C%95%EA%B8%80/report_gvr.html) is already separate from any diagnostic test results. We will ensure the styling and navigation clearly mark it as a "Homework/Training Report" (GVR) rather than a "Diagnostic Evaluation Report".

## Verification Plan
1. Open `diagnostic_hub.html` and verify the three main test types are prominently displayed inspired by the KNS brochure.
2. Open [admin_input.html](file:///c:/Users/SsoHot/Desktop/%EB%8C%95%EA%B8%80/admin_input.html) and verify the new checkboxes for "Distribution Settings" allow for cross-insertion into both the Diagnostic pool and the Problem Bank pool.
