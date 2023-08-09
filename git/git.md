About git

 - 버전 관리 시스템 : 파일 변화를 시간의 흐름에 따라 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템. 파일의 이름을 수정하지 않아도 언제 무엇을 수정했는지 관리할 수 있다.

 - 버전 - 백업 - 협업의 3단계
   - 이 중 '버전'이 가장 중요

 - 리눅스를 만든 리누스 토르발스가 git을 만들었다.

git 기본 사용법

 - "버전 관리는 디버깅을 위해서 하는 것이다"
    따라서 단위 작업별로 진행된다

 - vs code Initialize repository : 초기화를 통해 .git 파일 생성, 깃을 관리하라고 지정

 - "커밋은 버전을 만든다"

 - 첫 사용 : 
   git config --global user.eamil "you@example.com"
   git config --global user.name "your name"

 - Terminal에서 git bash 사용

 - "add는 커밋 대기 상태를 만든다"

 - "커밋 대기 상태는 stage area, 혹은 index 등으로 불린다"

 - 명령어
   git log : 현재까지 만들어진 버전을 확인한다. 히스토리를 시간 순으로 보여준다. 식별자, 작성자, 작성 날짜, 커밋 메세지를 확인할 수 있다.

 - 프로젝트 폴더 안에 생기는 .git 폴더는 repository
   repository를 제외한 나머지는 working directory
   add를 하면 working directory에 있는 코드가 stage area에 등록. 커밋 대기 상태가 됨
   commit을 하면 .git 폴더에 version 생성

 - 이전에 있었던 모든 스테이징한 내용들은 모두 '누적'된다.

 - "각각의 버전은 그 버전이 만들어진 시점에 stage area의 스냅샷이다"

 - "Head는 현재 버전(현재 사용자의 working dir와 stage area)을 가리키고, main은 마지막 버전(최신 버전)을 가리킨다"

 - "head가 가리키는 버전이 부모"

 - "checkout은 head를 옮기고, reset은 main을 옮긴다"

 - 만약 head가 main을 가리키고 있지 않는 상태에서 커밋을 하면, main은 기존에 있던 버전에 그대로 있고 head만 새로 생성된 버전으로 이동한다.

Branch

 - git branch [이름] : head가 가리키고 있는 버전에 branch 생성

 - branch를 사용하면 안정적으로 코드를 관리할 수 있고, 기존의 안정적인 코드와 개발 중인 코드를 구분하여 관리할 수 있다. 따라서 버전 관리 뿐 아니라 팀 프로젝트 등 협업에서도 유용하다.


merge
 - main이 branch를 병합할 때, main이 주체가 되어 움직이고 병합당하는 branch는 움직이지 않는다.

 - 병합된 commit의 부모는 main과 branch의 커밋이다. 즉, 2개의 부모를 가지고 있다.

 - git merge branch : branch를 main에 병합

 - git merge --abort : 병합하기 전으로 되돌린다

 - 병합 시 base(main과 branch에 있는 두 버전의 공통된 부모)를 찾아서 수정된 부분들을 확인
   -> both modify 된 경우만 알림, 그 외에는 자동으로 git이 병합함

 - 병합이 순조롭게 완료되면 자동으로 stage area에 add 된다.

 - add의 3대 의미
   1. 커밋 대기
   2. untracked -> tracked
   3. 충돌 해결됨

 
push

 - 원격 저장소(remote repository)에 코드 변경분을 업로드하기 위해서 사용

 - push 후 생기는 orgin/main 표시는 'remote tracking branch'라고 부르며, 이 표시를 보고 어디까지 동기화했는지 확인 가능

 - orgin과 main이 같은 버전을 가리키면 더이상 동기화 할 것이 없음을 의미함

 - push를 하기 위해선 github의 repository에 연결해야 함


clone

 - 원격 저장소와 똑같은 폴더, 파일을 로컬에 생성한다


pull

 - 로컬과 원격에 저장되어 있는 버전이 맞지 않으면(orgin/main이 다른 곳을 가리키면) pull을 하기 전엔 push를 할 수 없다.

 - sync = push + pull
 - pull = fecth + merge
 - fecth = 원격 저장소의 내용을 로컬 저장소로 가져오는 것
 - merge = 두 버전을 하나로 합치는 것

 - "작업하기 전에는 pull 하고 commit하고 push한다"

 
충돌

 - merge나 pull을 하는 도중 같은 파일의 같은 위치의 내용이 서로 다른 경우 충돌이 발생할 수 있다.

 - 충돌이 발생하면 두 코드를 비교해 더 나은 코드로 수정해야 한다.