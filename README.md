code2excel
========

$B%$%s%U%i%3!<%I$G4D6-$r9=C[$9$k$HF1;~$K4D6-Dj5A=q$r:n@.$9$k%D!<%k!%(B

Description
-----------
$B4D6-$H4D6-Dj5A=q$,P*N%$9$k$3$H$O$7$P$7$P$"$k!%(B

puppet$B!$(Bchef$B!$(Bansible$BEy$N%D!<%k$NMxMQ$K$h$C$F4D6-$H@_7W$H$NP*N%$O@8$8$K$/$/$J$C$F$-$F$$$k!%(B
$B$7$+$7!$%3!<%I$@$1$G$O%3%_%e%K%1!<%7%g%s$K;Y>c$r$-$?$9>l9g$b$"$k!%(B
$B$d$O$j!$$*5RMM$G$"$C$?$j!$%^%M!<%8%c!<AX$H$N%3%_%e%K%1!<%7%g%s$K$O8E$-NI$-4D6-Dj5A=q$,9%$^$l$k>l9g$,B?$$!%(B

$B$=$s$JM}M3$+$i%$%s%U%i%3!<%I$K$h$C$F!$(B
* $B4D6-(B
* $B4D6-Dj5A=q(B

$B$rF1;~$KJQ99$9$k%D!<%k$r:n@.$7$?!%(B

Design Priciples
----------------
* **$B%I%-%e%a%s%H$O%3!<%I$NI{;:J*(B**  
    $B%$%s%U%i%3!<%I$r@5$H$7$F!$%3!<%I$+$i%I%-%e%a%s%H$r<+F0@8@.$9$k!%(B
* **$BJQ49$N40A4@-(B**  
    $B%I%-%e%a%s%H@8@.$+$i?M<j$N:n6H$rGS=|$9$k!%(B

Demo
----
$B0J2<$N(Bansible$B$N%3!<%I(B(gist/test_data/demo.yml)$B$+$i4D6-Dj5A=q$r<+F0@8@.$9$k%G%b$G$"$k!%(B

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

Vagrant$B$G2>A[%^%7%s$H5/F0$7!$%G%bMQ%7%'%k(B(gist/demo.sh)$B$r<B9T$9$k$3$H$G!$0J2<$N(Bexcel$B%U%!%$%k(B(gist/test_data/directory_template.xlsx)$B$r%F%s%W%l!<%H$K$7$F4D6-Dj5A=q$,<+F0@8@.$5$l$k!%(B

![simple_demo_template](https://github.com/ynaka81/dockerEE/wiki/images/simple_demo_template.png)

    $ cd gist
    $ vagrant up
    Bringing machine 'master' up with 'virtualbox' provider...
    Bringing machine 'node1' up with 'virtualbox' provider...
    Bringing machine 'node2' up with 'virtualbox' provider...
    ==> master: Importing base box 'opscode-centos-7.1'...
                           ($B>JN,(B)
    $ vagrant ssh master
    [vagrant@master ~]$ cd /vagrant/gist
    [vagrant@master gist]$ ./demo.sh

    PLAY [node1] ****************************************************************** 
    
    GATHERING FACTS *************************************************************** 
    ok: [node1]
                           ($B>JN,(B)
    [vagrant@master gist]$ $B%m%0%"%&%H(B
    Connection to 127.0.0.1 closed.
    $ ls output
    directory.xlsx  directory.yml

![simple_demo_result](https://github.com/ynaka81/dockerEE/wiki/images/simple_demo_result.png)
