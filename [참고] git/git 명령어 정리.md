```bash

// first 브랜치 생성하기
$ git branch first

// 현재 브랜치를 first 브랜치로 이동
$ git switch first

// 현재 브랜치를 master 브랜치로 이동
$ git switch master

// first 브랜치를 현재 브랜치에 병합
$ git merge first

----------------------------------------------------

두 브랜치 병합하기

1. 정상적인 상황 눈으로 보기
  - first 브랜치에서 test1.txt 생성 후 커밋까지
  - second 브랜치에서 test2.txt 생성 후 커밋까지
  - master 브랜치에서 둘 다 병합
  - $ git branch -D first second

2. 충돌 발생 상황 눈으로 보기
  - first 브랜치에서 test3.txt 생성 후 커밋까지
  - second 브랜치에서 test3.txt 생성 후 커밋까지
  - master 브랜치에서 둘 다 병합

3. 충돌 해결
  - vi 에디터 or vscode 에서 개발자가 직접 해결해야 합니다.
  - 해결 후 add, commit
  - $ git branch -D first second

----------------------------------------------------

최신 commit 메세지 수정하기
  - $ git commit --amend
  - 명령어 입력 시 vi 에디터가 열립니다.
  - 커밋 메세지 수정 후 저장 및 종료(:wq) 입력하면 가장 최근 커밋 메세지가 수정됩니다.
```

[참고] vi 에디터 명령어

> i - 현재 커서 위치에서 insert 모드로 전환
> ESC: insert 모드나 명령 모드에서 나와서 Normal 모드로 전환
> :w - 현재 파일 저장
> :q - Vim 종료
> :wq - 파일 저장 후 Vim 종료
> u - 이전 명령 취소 (undo)
> yy - 현재 줄 복사
> p - 현재 줄 아래에 복사한 내용 붙여넣기
> dd - 현재 줄 삭제
> /검색어 - 검색어를 찾아 이동
> :set nu - 라인 넘버 보이기
> :set nonu - 라인 넘버 숨기기


