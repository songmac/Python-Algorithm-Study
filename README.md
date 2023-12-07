# 2023-Study-Coding-Test

## 폴더에 대한 설명
📁Algorithm
- 목적 : 파이썬 문법을 통하여 알고리즘, 자료구조의 기본 개념을 이해하고 프로그램에 바로 적용할 수 있도록 함
- 내용 : 각 알고리즘을 비교하며 다양하게 변형하여 개념을 깊이있게 이해
- 효과 : 프로그래밍 할 때 알고리즘과 자료구조과 왜 필요한지 알게되고, 여러 가지 알고리즘을 통해 스스로 문제를 해결할 수 있는 방식을 터득
📁Coding Test
- 코딩 실력을 향상시키고, 유지하기 위해 1일 1문제 풀이를 진행


## 스터디 방식
- 매주 월요일마다 스터디(2시간)
	- 미리 준비할 필요 없이, 스터디 시간에 책을 읽음
	- 타이머 시간 설정을 한 후 각자 읽어봄(Default : 15분)
	- 코드도 눈으로 보고 넘김
- 각자 읽은 부분 중
	- 중요하게 생각하는 것
	- 나에게 특히 영감을 준 부분
	- 의문점이 드는 것 등을 공유
- 분량이 너무 많은 경우 타이머 시작하기 전에 섹션을 나눈 후 읽고 담당 섹션에 대해 이야기
- XGBoost, LightGBM의 경우 논문에 대해 읽어보기
	- 우리가 속한 분야는 새로운 아이디어가 계속 나오는 분야
	- 논문을 접하는 것이 중요하기 때문에, 논문 읽는 것에 대한 습관을 위해 진행 (모두 이해하지 못해도 괜찮음)
	- [XGBoost Paper](https://arxiv.org/abs/1603.02754)
	- [LightGBM Paper](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf)
	- 논문 이해가 잘 안되는 경우 부가 자료도 함께 읽어보며 학습
        - (아이디어) 논문을 바로 읽으면 어려울 수 있으므로, API Document를 본 후 진행하는 방법
        - 이 경우, 공식 Document를 (일부분만) 번역해서 Socar Repo에 공유하면 어떨까? => 스터디 + 대외적 홍보 효과
        - [XGBoost Document](https://xgboost.readthedocs.io/en/latest/index.html)
        - [LightGBM Document](https://lightgbm.readthedocs.io/en/latest/)

<details><summary>XGBoost, LightGBM 부가 자료</summary>
<p>
	
- [XGBoost 관련 글](https://brunch.co.kr/@snobberys/137)
- [LightGBM 번역 글](https://aldente0630.github.io/data-science/2018/06/29/highly-efficient-gbdt.html)
- [XGBoost, LightGBM 파라미터 설명 글](https://sites.google.com/view/lauraepp/parameters)
- [Introduction to Boosted Trees PPT](https://homes.cs.washington.edu/~tqchen/pdf/BoostedTree.pdf?fbclid=IwAR0gGntURg4U24l6Fit-DLpVNBb_BtgMjzlSg3NYdb8jI44JLHLH-0Zluis)
- [CatBoost vs LightGBM vs XGBoost 비교 글](https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db)
	
</p>
</details> 


## Algorithm 책의 목차
- 1) 파이썬 기반의 머신러닝과 생태계 이해 (86p)
	- Numpy, Pandas 
- 2) 사이킷런으로 시작하는 머신러닝 (55p)
	- sklearn Estimator, Model Selection, 데이터 전처리 
- 3) 평가 (34p)
	- Accuracy, Precision, Recall, Confusion Matrix, F1 Score, ROC Curve, AUC 
- 4) 분류 (105p)
	- Decision Tree, Ensemble, Random Forest, Gradient Boosting Machine, XGBoost, LightGBM, Under Sampling/Over Sampling, Stacking 
- 5) 회귀 (85p)
	- Linear Regression, Lidge, Rasso, ElasticNet, Logistic Regression 
- 6) 차원 축소 (30p)
	- PCA, LDA, SVD, NMF 
- 7) 군집화 (54p)
	- K-means, Cluster Evaluation, Mean Shift, GMM, DBSCAN 
- 여기까지 449p
- 8) 텍스트 분석 (94p)
- 9) 추천 시스템 (63p)
	- 8), 9)는 다루지 않을 예정

## 공부 규칙
- 마음가짐 : 매일 30분씩만 꾸준히 해나가자. 아침에 일어나면 가장 먼저 잔디를 심자 !
- Algorithm : 책의 개념을 이해하기 어렵다면 추가 자료조사해서 정리하기 
- Coding Test : 다른 사람의 풀이 확인


## 커밋 규칙
  - 1. 내용의 제목과 본문을 한 줄 띄워 구분한다.
    2. 제목은 50 characters 이하로 제한한다.
    3. 제목의 첫 번째 문자는 대문자로 작성한다.
    4. 제목의 마지막에는 마침표를 사용하지 않는다.
    5. 제목은 명령문으로 작성한다.
    6. 본문은 72 character마다 줄을 바꾼다.
    7. 본문의 내용은 "어떻게" 보다 "무엇을" "왜" 인지에 대해 설명한다.

	
### Reference
- 이지스퍼블리싱 [Do it 자료구조와 함께 배우는 알고리즘 입문 : 파이썬 편](https://github.com/easysIT/doit_dsalgo_with_python)
- [Programmers](https://school.programmers.co.kr/)
