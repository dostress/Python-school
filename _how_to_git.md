# How to git really quick

## 1. Going into the directory and initializing the repo. <a name="1"></a>

1. Go to your `/Python-Class` directory

Doing a simple `cd /mnt/c/Python-Class`

2. Check if the the repo is initialized

Do `git init`

And it should pop up this message:

```
Reinitialized existing Git repository in /mnt/c/Python-Class/.git/
```

Otherwise, it should still work the same as always.

## 2. Adding the code to the repo

Let's say you've added a new python program (`python.py`)

You need to `push` the file into the repo.

1. **Add the file to the repo**

Do `git add python.py`

If nothing prompted, it's normal so you don't have to worry about that.

---

2. **(Optional) check the status on the repo**

If you're still unsure whether it's added, just do `git status`.

It will pop something like this:

```
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   python.py
```
If `new file: python.py` is red, then it means you haven't added. Look at step 1 to do that.

Otherwise, the `new file: python.py` will be green which means it's ready to commit!

---

3. **Commit the file so it can be ready to be `push`ed**

Now that the file is ready to be commit, you must add a `message` (`message` can be changed to anything).

`git commit -m "message"`

When it is ready, it will similar to this:

```
[main 5242f5d] message
 1 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 python.py
```

The output means that you've just created `python.py`.

---

4. **Push the file into a new directory**

Now that everything is added and commited, it is ready to be added to the main repo.

To do this, you need to `push` the changes from the `commit` to the repo. To do this:

`git push`

It will prompt you to put your 'passphrase', is your PIN to your computer (if you want to change it, ask Hansel).

That simple. It should output something like this: 

```
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 394 bytes | 394.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:dostress/Python-school.git
   bbb3063..5242f5d  main -> main
```

Of course, not to the tea, but similar.

---

6. **(Optional) Check if the commit is updated**

Just do `git log`, and it will output this:

```
commit 5242f5d06a86ec6f1878947df99706a35455231a (HEAD -> main, origin/main)
Author: MJ <mtamarra101@gmail.com>
Date:   Mon Nov 21 17:43:02 2022 -0700
```

It just mean that the code is commit to the `main` branch.

---

5. **Check on [GitHub](https://github.com) if the files are added.**

Go to the GitHub repo is the files are added to the repo. Notify Hansel so that he can pull the code to his computer and can do the same process aswell.

But how do I get the code from Hansel?

## 3. Getting the changed code(s) from the repo

Hansel just changed, maybe added some code to help you out. Now how do I get the code?

1. **Go to the file (go to [1.1](#1))**

---

2. **Check [GitHub](https://guthub.com) for the changed files**

Double cheking if the changes are commited.

---

3. **Getting the code**

To get the code, do:

`git pull`

Then it will prompt you to put you passphrase (again is the Pin from your laptop).

It should be added to your computer.
