# 230908 관통프로젝트

- 느낀점 및 알게된 점
  
  - 특히 이미지를 다룰 때 이미지 크기를 마음대로 조절하는 것도 너무 까다로웠고 이미지 위치를 마음대로 움직이는 것도 너무 까다롭다고 느꼈다.
  
  - 처음에 이미지 크기를 줄이고 싶어서 width:300px; 이런식으로 했었는데 화면 크기를 줄이니 이미지 크기는 동일한데 상위 div의 너비는 줄어들어서 배치가 이상하게 변하는 문제를 알게 되었다. 따라서 이미지 너비를 무조건 고정값으로 조정하면 안되고 width:100% 라던지 width:auto;와 같이 상대적인 값을 주어야 화면 크기를 바꾸었을 때 레이아웃이 완전히 이상해지는 문제를 덜 겪을 수 있다.
  
  - 그냥 눈 앞에 닥친 상황만 해결하기에 급급하다보니 이번주에 배웠던 OOCSS를 적용하는 것이 너무 어렵다고 느꼈다. 모든 요소마다 다른 css를 주어서 최종적으로 완성된 css파일의 크기가 너무 크고 가독성이 떨어진다고 느껴졌다. 
  
  - 디자인을 미리 구체적으로 생각하지 않고 만들다 보니 밑부분으로 갈수록 디자인이 조잡해지는 것 같은 느낌을 받았다. 무조건 만들기부터 시작하는 것이 아니라 신중하게 고민하여 디자인을 최대한 구체적으로 정하고 어떤 방식으로 구현할지 미리 계획을 세우면 앞으로 더 수월하게 프로젝트를 진행할 수 있을 것 같다.