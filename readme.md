# CodeChef Rank Notifier

Python process which fetches data from CodeChef Rank API after every `15min`[default] and gives notification if anyone have solved any question.

<p  align="center">
	<img src="https://raw.githubusercontent.com/poke19962008/CC-Rank-Notifier/master/git-res/s1.png)" />
</p>

## How to use

- Install `pync` for activating notification center in Mac OSX

```
$ sudo pip install pync
```

- Fire up `main.py` with suitable arguments. Use `\ ` convention to specify institute 

```
$ python mian.py --contest DEC15 --institute SRM\ University
```
