#!/usr/bin/python
import os


class father():
    """add user"""
    def useradd(self, u_name):
        if os.system("id %s &>/dev/null" % u_name) == 0:
            print "the user is already exist!"
        else:
            os.system("useradd %s &>/dev/null" % u_name)
            print "the user is create ok"


class son_a(father):
    """modifi uid gid shell"""
    def set_uid(self, uid, u_name):
        if os.system("id %s &>/dev/null" % u_name) == 0:
            if os.system("cat /etc/passwd|awk -F: '{print $3}'|egrep '%d' \
               &>/dev/null" % uid) == 0:
                print "the uid is already used!"
            else:
                os.system("usermod -u %d %s &>/dev/null" % (uid, u_name))
                print "the uid is set ok"
        else:
            print "the user is not exist!"

    def set_gid(self, gid, u_name):
        if os.system("id %s &>/dev/null" % u_name) == 0:
            if os.system("cat /etc/passwd|awk -F: '{print $4}'|egrep '%d' \
               &>/dev/null" % gid) == 0:
                os.system("usermod -g %d %s &>/dev/null" % (gid, u_name))
                print "the gid is set ok"
            else:
                print "the gid is not exist!"
        else:
            print "the user is not exist!"

    def set_shell(self, shell, u_name):
        if os.system("id %s &>/dev/null" % u_name) == 0:
            os.system("usermod -s %s %s &>/dev/null" % (shell, u_name))
            print "the shell is set ok"
        else:
            print "the user is not exist!"


class son_b(father):
    """delete user or group"""
    def userdel(self, u_name):
        if os.system("id %s &>/dev/null" % u_name) == 0:
            os.system("userdel -r %s &>/dev/null" % u_name)
            print "the user is delete ok"
        else:
            print "the user is not exist!"

    def groupdel(self, u_group):
        if os.system("cat /etc/group|awk -F: '{print $1}'|egrep '%s' \
           &>/dev/null" % u_group) == 0:
            os.system("groupdel %s &>/dev/null" % u_group)
            print "the group is delete ok"
        else:
            print "the group is not exist!"


class son_c(son_a, son_b):
    """add group,set gid for add group"""
    def groupadd(self, g_name):
        if os.system("cat /etc/group|awk -F: '{print $1}'|egrep '%s' \
           &>/dev/null" % g_name) == 0:
            print "the group is already exist!"
        else:
            os.system("groupadd %s" % g_name)
            print "the group is create ok"

    def set_gid(self, gid, u_name):
        try:
            if os.system("id %s &>/dev/null" % u_name) == 0:
                if os.system("cat /etc/group|awk -F: '{print $3}'|egrep '%d' \
                &>/dev/null" % gid) == 0:
                    os.system("usermod -g %d %s" % (gid, u_name))
                    print "the gid of user is set ok!"
                else:
                    raise TypeError
            else:
                raise NameError
        except TypeError:
            print "the group is not exist!"
        except NameError:
            print "the user is not exist!"
