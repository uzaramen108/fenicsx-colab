# fenicsx-colab

FEniCSx + micromamba 환경을 Google Colab에서
**Drive 캐시 기반으로 빠르게 재사용**하기 위한 설정입니다.

---

## 1. Google Drive 마운트 (필수)

```python
from google.colab import drive
drive.mount('/content/drive')
```

## 2. 원클릭 설치

```python
%run setup_fenicsx.py
```

## 3. 옵션

- 강제 재설치

```python
%run setup_fenicsx.py --force
```

- 완전 초기화

```python
%run setup_fenicsx.py --clean
```

## 4. 테스트

```python
%%fenicsx --info
```
