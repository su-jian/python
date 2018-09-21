#!/user/bin/python
# coding:utf-8
# Filename:user_class.py

import os


###############################################################################
class UserOption:
    def add_user(self, u_name):
        os.system('useradd %s' % u_name)
        print "User %s add success!" % u_name


###############################################################################
class ChangeUser(UserOption):
    # def __init__(self, u_name):
    #    self.u_name = u_name

    def change_uid(self, u_name, uid):
        os.system('usermod -u %s %s' % (uid, u_name))
        print "User %s's uid has changed to %s" % (u_name, uid)

    def change_gid(self, u_name, gid):
        os.system('usermod -g %s %s' % (gid, u_name))
        print "User %s's gid has changed to %s" % (u_name, gid)

    def change_shell(self, u_name, shell):
        os.system('usermod -s %s %s' % (shell, u_name))
        print "User %s's shell has changed to %s" % (u_name, shell)


###############################################################################
class DeleteUserOrGroup(UserOption):
    # def __init__(self, del_name):
    #    self.del_name = del_name

    def del_user(self, u_name):
        os.system('userdel -r %s' % u_name)
        print "User %s delete success!" % u_name

    def del_group(self, g_name):
        os.system('groupdel %s' % g_name)
        print "Group %s delete success!" % g_name


###############################################################################
class GroupOption(ChangeUser, DeleteUserOrGroup):
    def add_group(self, g_name, gid):
        try:
            if os.system('groupadd -g %s %s &> /dev/null' % (gid, g_name)):
                raise TypeError
            else:
                raise NameError
        except TypeError:
            print "Group name or gid has exist"
        except NameError:
            print "Group %s add success!" % g_name

#    def change_gid(self, u_name, gid):
#        os.system('usermod -g %s %s' % (gid, u_name))
#        print "User %s's gid has changed to %s" % (u_name, gid)

###############################################################################
UserOption = UserOption()
ChangeUser = ChangeUser()
DeleteUserOrGroup = DeleteUserOrGroup()
GroupOption = GroupOption()
