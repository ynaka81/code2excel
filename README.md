code2excel
========

インフラコードで環境を構築すると同時に環境定義書を作成するツール．

Description
-----------
環境と環境定義書が乖離することはしばしばある．

puppet，chef，ansible等のツールの利用によって環境と設計との乖離は生じにくくなってきている．
しかし，コードだけではコミュニケーションに支障をきたす場合もある．
やはり，お客様であったり，マネージャー層とのコミュニケーションには古き良き環境定義書が好まれる場合が多い．

そんな理由からインフラコードによって，
* 環境
* 環境定義書

を同時に変更するツールを作成した．

Design Priciples
----------------
* **ドキュメントはコードの副産物**  
    インフラコードを正として，コードからドキュメントを自動生成する．
* **変換の完全性**  
    ドキュメント生成から人手の作業を排除する．

Demo
----
以下のansibleのコード(gist/test_data/demo.yml)から環境定義書を自動生成するデモである．

    ---
    - hosts: node1
      sudo: yes
      remote_user: vagrant
      tasks:
              - name: create data root directory
                file: path=/data state=directory owner=vagrant group=vagrant mode=0755
    
              - name: create data sirectory for node1
                file: path=/data/data1 state=directory owner=vagrant group=vagrant mode=0700
    
    - hosts: node2
      sudo: yes
      remote_user: vagrant
      tasks:
              - name: create data root directory
                file: path=/data state=directory owner=vagrant group=vagrant mode=0755
    
              - name: create data directory for node2
                file: path=/data/data2 state=directory owner=vagrant group=vagrant mode=0750

Vagrantで仮想マシンと起動し，デモ用シェル(gist/demo.sh)を実行することで，以下のexcelファイル(gist/test_data/directory_template.xlsx)をテンプレートにして環境定義書が自動生成される．

![simple_demo_template](https://github.com/ynaka81/code2excel/wiki/simple_demo_template.png)

    $ cd gist
    $ vagrant up
    Bringing machine 'master' up with 'virtualbox' provider...
    Bringing machine 'node1' up with 'virtualbox' provider...
    Bringing machine 'node2' up with 'virtualbox' provider...
    ==> master: Importing base box 'opscode-centos-7.1'...
                           (省略)
    $ vagrant ssh master
    [vagrant@master ~]$ cd /vagrant/gist
    [vagrant@master gist]$ ./demo.sh

    PLAY [node1] ****************************************************************** 
    
    GATHERING FACTS *************************************************************** 
    ok: [node1]
                           (省略)
    [vagrant@master gist]$ ログアウト
    Connection to 127.0.0.1 closed.
    $ ls output
    directory.xlsx  directory.yml

![simple_demo_result](https://github.com/ynaka81/code2excel/wiki/images/simple_demo_result.png)
