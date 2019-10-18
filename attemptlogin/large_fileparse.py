#!/usr/bin/env python3
loginsucc = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as kfile:
    for line in kfile:
        if "- - - - -] Loaded 2 encryption keys" in line:
            loginsucc += 1
print("The number of failed log attempts in", loginsucc)
