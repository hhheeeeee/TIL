# git

1. commit 작성자 설정
   
   ```
    git config --global user.name 장상호
   
    git config --global user.email sangho.jang@mincoding.co.kr
   
    # 설정 취소
    git config --global --unset user.email
   ```

2. commit 작성자 확인
   
   ```
    git config --global -l
   ```

3. git 실행(git 저장소 생성) , git 실행 취소
   
   ```
   git init
   ```

rm -rf .git

```
4. git ignore
```

echo b.txt >> .gitignore

```
5. git add
```

git add .

```
6. commit 준비가 되었는지 확인
```

git status

```
7. add 취소(staging area에서 working directory로)
```

git reset

```
8. commit
```

git commit -m 'add a.txt'

```
9. commit 확인
```

git log

```
10. 원격저장소와 로컬저장소 연결
```

git remote add origin url

```
- 원격저장소의 별칭 : origin
- 로컬저장소에 origin이라는 이름의 원격 저장소 주소를 추가

12. 원격 저장소에 commit 목록을 업로드
```

# 해당 브랜치를 origin 저장소의 기본 동기화 브랜치로 설정

# 최초 1회 진행하여 기본 동기화 브랜치를 설정할 때 사용

git push -u origin master

# 그 다음에는 git push로 해도 됨

# master 앞에 +를 붙이면 강제로 push 하겠다는 의미

git push origin +master

```
- push 해줘, origin이라는 이름의 원격저장소에  master 브랜치를

12. 연결되어 있는 현재 프로젝트에 등록된 리모트 저장소를 확인
```

git remote -v

```
13. 연결 해제
```

git remote remove origin

```
14. git 삭제
```

rm -rf .git
```