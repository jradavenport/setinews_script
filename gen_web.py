# generate website post
# posts are jekyll pages, so the process is simple:
# BEFORE:
# - pull new content for this issue (from ADS API?)
# - generate new Mailchimp email campaign (have URL ready, saved somewhere)
# 1. create new post from text templates
# 2. save as a file with today's date encoded in file name correctly
# 3. run 'jekyll build', assuming jekyll installed correctly on laptop
# 4. run git add, git commit, git push, assuming git authentication saved in laptop
# 5. PROFIT!

# import stuff as needed
import os

# define useful things
webdir = '/Users/james/Dropbox/website/setinews'

# what month is it? (name)

# what day is it? (yyy, mm, dd)

# the top of the article
t1 = '''---
layout: post
title: SETI.news for XYZ
---


# save .md file

# run commands
os.popen('jekyll build').read()
