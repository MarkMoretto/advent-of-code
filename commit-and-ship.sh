#!/bin/sh

day_num = git status --short | egrep '^\?\? day[0-9]+\/$' | head -1 | egrep -oh '[0-9]+'
git add day_$day_num/
git commit -m "AOC 2021 day $day_num update and/or completed."
git push -u origin master
