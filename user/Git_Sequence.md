# **`Git 순서도`**

## 1. $ git init
> git 저장소 생성
```
$ git init
```
## 2. $ git add <>
> 1통에서 2통으로 보냄
```
$ git add Git_Sequence.md
```
## 3. $ git status
> 1통, 2통 상태 보기
```
$ git status

On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Git_Sequence.md
```
## 4. git commit -m 'ver.1.0.0'
> 2통에서 3통으로 보냄
```
$ git commit -m 'ver.1.0.0'

[master 705f12a] ver.1.0.0
 1 file changed, 3 insertions(+)
 create mode 100644 Git_Sequence.md
 ```
## 5. git log
> 3통 상태 보기
```
$ git log

commit 705f12aa761e63aff2448474b8a970090b48622c (HEAD -> master)
Author: ParkJiHwan_22 <ParkjiHwan22@github.com>
Date:   Wed Dec 28 10:26:40 2022 +0900

    ver.1.0.0
```
## 6. git log --oneline
> 3통 상태 보기 (commit 하나당 한줄로 표현)
```
$ git log --oneline

705f12a (HEAD -> master) ver.1.0.0
73e9348 My Goals_Ver.1.0.0
302ff04 My_Goals
```
## 7. git reomote add origin `url`
> 원격저장소 추가
```
$ git remote add origin https://github.com/ParkJiHwan22/Test_1.git
```
## 8. git remote -v
> 원격저장소 정보 확인
```
$ git remote -v

origin  https://github.com/ParkJiHwan22/Test_1.git (fetch)
origin  https://github.com/ParkJiHwan22/Test_1.git (push)
```
## 9. $ git push origin master
> 원격저장소로 보내기
```
$ git push origin master

info: please complete authentication in your browser...
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 1017 bytes | 1017.00 KiB/s, done.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0       
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/ParkJiHwan22/Test_1.git
 * [new branch]      master -> master
 ```
## 10. git pull origin master
> 원격저장소에서 가져오기
```
$ git pull origin master

From https://github.com/kdt-live/TIL-2nd
 * branch            master     -> FETCH_HEAD
Already up to date.
```


## 11. git clone (url)
> 원격저장소 복제
```
$ git clone https://github.com/kdt-live/TIL-2nd.git

Cloning into 'TIL-2nd'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 0), reused 4 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
``