# Day 01 – Python OS Module

## Prerequisites

 You should have basic knowledge of Python.

 Automate the boring stuff book
https://automatetheboringstuff.com/
    
As a DevOps/System Admin, we encounter a task to interact with OS every day. OS module provides a portable way of using operating system-dependent functionality. In addition, it allows us to interact with the underlying operating system in different ways to automate tasks(e.g., creating/removing directories, check if the file/directory exists, etc.).
 
 ```bash
# Open the Python prompt
python3
Python 3.8.7 (default, Feb  3 2021, 06:31:03)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>># Import the OS module
>>> import os# To see the methods and attributes that we have access within OS module
>>> dir(os)
[‘CLD_CONTINUED’, ‘CLD_DUMPED’, ‘CLD_EXITED’, ‘CLD_TRAPPED’, ‘DirEntry’, ‘EX_CANTCREAT’, ‘EX_CONFIG’, ‘EX_DATAERR’, ‘EX_IOERR’, ‘EX_NOHOST’, ‘EX_NOINPUT’, ‘EX_NOPERM’, ‘EX_NOUSER’, ‘EX_OK’, ‘EX_OSERR’, ‘EX_OSFILE’, ‘EX_PROTOCOL’, ‘EX_SOFTWARE’, ‘EX_TEMPFAIL’, ‘EX_UNAVAILABLE’, ‘EX_USAGE’, ‘F_LOCK’, ‘F_OK’, ‘F_TEST’, ‘F_TLOCK’, ‘F_ULOCK’, ‘MutableMapping’, ‘NGROUPS_MAX’, ‘O_ACCMODE’, ‘O_APPEND’, ‘O_ASYNC’, ‘O_CREAT’, ‘O_DIRECT’, ‘O_DIRECTORY’, ‘O_DSYNC’, ‘O_EXCL’, ‘O_LARGEFILE’, ‘O_NDELAY’, ‘O_NOATIME’, ‘O_NOCTTY’, ‘O_NOFOLLOW’, ‘O_NONBLOCK’, ‘O_RDONLY’, ‘O_RDWR’, ‘O_RSYNC’, ‘O_SYNC’, ‘O_TRUNC’, ‘O_WRONLY’, ‘POSIX_FADV_DONTNEED’, ‘POSIX_FADV_NOREUSE’, ‘POSIX_FADV_NORMAL’, ‘POSIX_FADV_RANDOM’, ‘POSIX_FADV_SEQUENTIAL’, ‘POSIX_FADV_WILLNEED’, ‘PRIO_PGRP’, ‘PRIO_PROCESS’, ‘PRIO_USER’, ‘P_ALL’, ‘P_NOWAIT’, ‘P_NOWAITO’, ‘P_PGID’, ‘P_PID’, ‘P_WAIT’, ‘PathLike’, ‘RTLD_DEEPBIND’, ‘RTLD_GLOBAL’, ‘RTLD_LAZY’, ‘RTLD_LOCAL’, ‘RTLD_NODELETE’, ‘RTLD_NOLOAD’, ‘RTLD_NOW’, ‘R_OK’, ‘SCHED_BATCH’, ‘SCHED_FIFO’, ‘SCHED_OTHER’, ‘SCHED_RR’, ‘SEEK_CUR’, ‘SEEK_END’, ‘SEEK_SET’, ‘ST_APPEND’, ‘ST_MANDLOCK’, ‘ST_NOATIME’, ‘ST_NODEV’, ‘ST_NODIRATIME’, ‘ST_NOEXEC’, ‘ST_NOSUID’, ‘ST_RDONLY’, ‘ST_SYNCHRONOUS’, ‘ST_WRITE’, ‘TMP_MAX’, ‘WCONTINUED’, ‘WCOREDUMP’, ‘WEXITED’, ‘WEXITSTATUS’, ‘WIFCONTINUED’, ‘WIFEXITED’, ‘WIFSIGNALED’, ‘WIFSTOPPED’, ‘WNOHANG’, ‘WNOWAIT’, ‘WSTOPPED’, ‘WSTOPSIG’, ‘WTERMSIG’, ‘WUNTRACED’, ‘W_OK’, ‘XATTR_CREATE’, ‘XATTR_REPLACE’, ‘XATTR_SIZE_MAX’, ‘X_OK’, ‘_Environ’, ‘__all__’, ‘__builtins__’, ‘__cached__’, ‘__doc__’, ‘__file__’, ‘__loader__’, ‘__name__’, ‘__package__’, ‘__spec__’, ‘_execvpe’, ‘_exists’, ‘_exit’, ‘_fspath’, ‘_fwalk’, ‘_get_exports_list’, ‘_putenv’, ‘_spawnvef’, ‘_unsetenv’, ‘_wrap_close’, ‘abc’, ‘abort’, ‘access’, ‘altsep’, ‘chdir’, ‘chmod’, ‘chown’, ‘chroot’, ‘close’, ‘closerange’, ‘confstr’, ‘confstr_names’, ‘cpu_count’, ‘ctermid’, ‘curdir’, ‘defpath’, ‘device_encoding’, ‘devnull’, ‘dup’, ‘dup2’, ‘environ’, ‘environb’, ‘errno’, ‘error’, ‘execl’, ‘execle’, ‘execlp’, ‘execlpe’, ‘execv’, ‘execve’, ‘execvp’, ‘execvpe’, ‘extsep’, ‘fchdir’, ‘fchmod’, ‘fchown’, ‘fdatasync’, ‘fdopen’, ‘fork’, ‘forkpty’, ‘fpathconf’, ‘fsdecode’, ‘fsencode’, ‘fspath’, ‘fstat’, ‘fstatvfs’, ‘fsync’, ‘ftruncate’, ‘fwalk’, ‘get_blocking’, ‘get_exec_path’, ‘get_inheritable’, ‘get_terminal_size’, ‘getcwd’, ‘getcwdb’, ‘getegid’, ‘getenv’, ‘getenvb’, ‘geteuid’, ‘getgid’, ‘getgrouplist’, ‘getgroups’, ‘getloadavg’, ‘getlogin’, ‘getpgid’, ‘getpgrp’, ‘getpid’, ‘getppid’, ‘getpriority’, ‘getresgid’, ‘getresuid’, ‘getsid’, ‘getuid’, ‘getxattr’, ‘initgroups’, ‘isatty’, ‘kill’, ‘killpg’, ‘lchown’, ‘linesep’, ‘link’, ‘listdir’, ‘listxattr’, ‘lockf’, ‘lseek’, ‘lstat’, ‘major’, ‘makedev’, ‘makedirs’, ‘minor’, ‘mkdir’, ‘mkfifo’, ‘mknod’, ‘name’, ‘nice’, ‘open’, ‘openpty’, ‘pardir’, ‘path’, ‘pathconf’, ‘pathconf_names’, ‘pathsep’, ‘pipe’, ‘popen’, ‘posix_fadvise’, ‘posix_fallocate’, ‘pread’, ‘putenv’, ‘pwrite’, ‘read’, ‘readlink’, ‘readv’, ‘remove’, ‘removedirs’, ‘removexattr’, ‘rename’, ‘renames’, ‘replace’, ‘rmdir’, ‘scandir’, ‘sched_get_priority_max’, ‘sched_get_priority_min’, ‘sched_getparam’, ‘sched_getscheduler’, ‘sched_param’, ‘sched_rr_get_interval’, ‘sched_setparam’, ‘sched_setscheduler’, ‘sched_yield’, ‘sendfile’, ‘sep’, ‘set_blocking’, ‘set_inheritable’, ‘setegid’, ‘seteuid’, ‘setgid’, ‘setgroups’, ‘setpgid’, ‘setpgrp’, ‘setpriority’, ‘setregid’, ‘setresgid’, ‘setresuid’, ‘setreuid’, ‘setsid’, ‘setuid’, ‘setxattr’, ‘spawnl’, ‘spawnle’, ‘spawnlp’, ‘spawnlpe’, ‘spawnv’, ‘spawnve’, ‘spawnvp’, ‘spawnvpe’, ‘st’, ‘stat’, ‘stat_float_times’, ‘stat_result’, ‘statvfs’, ‘statvfs_result’, ‘strerror’, ‘supports_bytes_environ’, ‘supports_dir_fd’, ‘supports_effective_ids’, ‘supports_fd’, ‘supports_follow_symlinks’, ‘symlink’, ‘sync’, ‘sys’, ‘sysconf’, ‘sysconf_names’, ‘system’, ‘tcgetpgrp’, ‘tcsetpgrp’, ‘terminal_size’, ‘times’, ‘times_result’, ‘truncate’, ‘ttyname’, ‘umask’, ‘uname’, ‘uname_result’, ‘unlink’, ‘unsetenv’, ‘urandom’, ‘utime’, ‘wait’, ‘wait3’, ‘wait4’, ‘waitid’, ‘waitid_result’, ‘waitpid’, ‘walk’, ‘write’, ‘writev’]
```

To print the current working directory, use os.getcwd(). This is similar to pwd command in Linux.
```bash
>>> os.getcwd()
'/home/ec2-user'
```
To change path/current working directory os.chdir(<directory to change>). This is similar to the cd command in Linux.
 
```bash
# os.chdir(<directory to change>)
>>> os.chdir("/tmp")# To verify your path now
>>> os.getcwd()
'/tmp'
```
 
To print/list files in the current directory(it return a list) use os.listdir() . It’s similar to the ls -l command in Linux.

```bash
$ ls -ltr
-rw-rw-r--. 1 cloud_user cloud_user       0 Mar  8  2019 secret.txt
-rw-rw-r--. 1 cloud_user cloud_user       0 Mar  8  2019 reports.csv
-rw-rw-r--. 1 cloud_user cloud_user       0 Mar  8  2019 Junk.txt
-rw-rw-r--. 1 cloud_user cloud_user       0 Mar  8  2019 code_ideas.odt>>> os.listdir()
['aristotle_politics.txt', 'cicero_disputations.txt', 'plato_republic.txt', 'secret.txt', 'Junk.txt', 'code_ideas.odt', 'reports.csv']
``` 
 NOTE: If you are not providing any path, it will take the current directory. But you can always pass the path as an input, e.g.,/etc. In this case.
 
 ```bash
>>> os.listdir(path)>>> os.listdir("/etc")
['fonts', 'crypttab', 'mtab', 'pki', 'rpm', 'yum.repos.d', 'yum', 'libuser.conf', 'audit', 'centos-release', 'rsyslog.d', 'issue', 'binfmt.d', 'issue.net', 'modules-load.d', 'os-release', 'security', 'tuned', 'redhat-release', 'DIR_COLORS', 'vimrc', 'system-release', 'sestatus.conf', 'fstab', 'system-release-cpe', 'tmpfiles.d', 'aliases', 'rc.local', 'bashrc', 'systemd', 'csh.cshrc', 'udev', 'csh.login', 'machine-id', 'environment', 'NetworkManager', 'exports', 'nsswitch.conf.bak', 'filesystems', 'inittab', 'group', 'adjtime', 'gshadow', 'networks', 'host.conf', 'cron.monthly', 'hosts', 'shadow-', 'hosts.allow', 'ppp', 'gconf', 'hosts.deny', 'rwtab', 'pulse', 'inputrc', 'nfsmount.conf', 'motd', 'rwtab.d', 'passwd', 'statetab', 'printcap', 'statetab.d', 'profile', 'profile.d', 'sysctl.conf', 'protocols', 'cron.hourly', 'securetty', 'cron.weekly', 'services', 'anacrontab', 'shadow', 'crontab', 'shells', 'X11', 'bash_completion.d', 'opt', 'pm', 'skel', 'sysconfig', 'xdg', 'xinetd.d', 'terminfo', 'default', 'polkit-1', 'ld.so.conf', 'ld.so.conf.d', 'my.cnf', 'nsswitch.conf', 'passwd-', 'dconf', 'rpc', 'cloud', 'ld.so.cache', 'ssh', 'man_db.conf', 'libaudit.conf', 'popt.d', 'alternatives', 'chkconfig.d', 'gnupg', 'avahi', 'init.d', 'rc.d', 'cron.d', 'rc0.d', 'cron.deny', 'rc1.d', 'grub.d', 'rc2.d', 'dnsmasq.conf', 'rc3.d', 'dnsmasq.d', 'rc4.d', 'updatedb.conf', 'rc5.d', 'dracut.conf', 'rc6.d', 'aliases.db', 'GREP_COLORS', 'libnl', 'gcrypt', 'pkcs11', 'wpa_supplicant', 'magic', 'sasl2', 'groff', 'ssl', 'dbus-1', 'samba', 'request-key.conf', 'request-key.d', 'kernel', 'virc', 'iproute2', 'selinux', 'gss', 'dracut.conf.d', 'krb5.conf', 'openldap', 'DIR_COLORS.256color', 'idmapd.conf', 'grub2.cfg', 'DIR_COLORS.lightbgcolor', 'rsyslog.conf', 'login.defs', 'pam.d', '.pwd.lock', 'logrotate.d', 'my.cnf.d', 'prelink.conf.d', 'sgml', 'group-', 'gshadow-', 'sysctl.d', 'yum.conf', 'netconfig', 'dhcp', 'xml', 'e2fsck.conf', 'exports.d', 'mke2fs.conf', 'depmod.d', 'modprobe.d', 'cron.daily', 'logrotate.conf', 'favicon.png', 'kdump.conf', 'makedumpfile.conf.sample', 'firewalld', 'audisp', 'postfix', 'chrony.conf', 'chrony.keys', 'rsyncd.conf', 'sudo-ldap.conf', 'sudo.conf', 'sudoers', 'sudoers.d', 'vconsole.conf', 'localtime', 'locale.conf', 'hostname', 'resolv.conf', 'grub.conf', 'plymouth', 'asound.conf', 'oddjob', 'oddjobd.conf', 'oddjobd.conf.d', 'gtk-2.0', 'libreport', 'UPower', 'udisks2', 'gdm', 'nanorc', 'wgetrc', 'mime.types', 'mailcap', 'ghostscript', 'centos-release-upstream', 'tcsd.conf', 'gssproxy', 'python', 'geoclue', 'la_version', '.updated', 'xrdp', 'amazon', 'init', 'subgid', 'subuid', 'nsswitch.conf.rpmnew', 'krb5.conf.d', 'GeoIP.conf', 'bluetooth', 'sysctl.conf.rpmnew', 'iscsi', 'chrony.keys.rpmnew', 'nfs.conf', 'kernel-reinstall-count', 'zprofile', 'bash.bashrc', 'rvmrc', 'libblockdev', 'multipath', 'lvm', 'trusted-key.key', 'glvnd', 'fuse.conf', 'egl', 'flatpak', 'libpaper.d', 'papersize', 'ImageMagick-6']
```
 
To create a file, use os.mknod().

 ```bash
# To create a fileos.mknod(<file name>)>>> os.mknod("testfile")# Verify it
>>> os.listdir()
['aristotle_politics.txt', 'cicero_disputations.txt', 'plato_republic.txt', 'secret.txt', 'Junk.txt', 'code_ideas.odt', 'reports.csv', 'testfile']
```
 To create a directory os.mkdir().
 
 ```bash
# To create a directoryos.mkdir(<directory name>)>>> os.mkdir("mytest")# To verify it
>>> os.listdir()
['aristotle_politics.txt', 'cicero_disputations.txt', 'plato_republic.txt', 'secret.txt', 'Junk.txt', 'code_ideas.odt', 'reports.csv', 'mytest']
```

But now, let say we want to go one level deep, i.e., both test3 and test4 don’t exist; if we are trying to create a directory recursively, it will not work; to do that, we need to use os.makedirs().

  ```bash
>>> os.mkdir("test3/test4")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'test3/test4'>>> os.makedirs("test3/test4")
```
 
To print, all the environment variables use os.environ. This is similar to the env command in Linux.
 
  ```bash
$ env
XDG_SESSION_ID=9
rvm_bin_path=/usr/local/rvm/bin
HOSTNAME=cddebed89c1c.mylabserver.com
GEM_HOME=/usr/local/rvm/gems/ruby-2.4.1
TERM=xterm-256color
SHELL=/bin/bash
HISTSIZE=100000
IRBRC=/usr/local/rvm/rubies/ruby-2.4.1/.irbrc
OLDPWD=/home/cloud_user
MY_RUBY_HOME=/usr/local/rvm/rubies/ruby-2.4.1
USER=cloud_user

_system_type=Linux
rvm_path=/usr/local/rvm
rvm_prefix=/usr/local
MAIL=/var/spool/mail/cloud_user
PATH=/usr/local/rvm/gems/ruby-2.4.1/bin:/usr/local/rvm/gems/ruby-2.4.1@global/bin:/usr/local/rvm/rubies/ruby-2.4.1/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local/rvm/bin:/home/cloud_user/.local/bin:/home/cloud_user/bin
PWD=/home/cloud_user/Documents
LANG=en_US.UTF-8
_system_arch=x86_64
_system_version=7
HISTCONTROL=ignoredups
rvm_version=1.29.3 (latest)
SHLVL=1
HOME=/home/cloud_user
LOGNAME=cloud_user
GEM_PATH=/usr/local/rvm/gems/ruby-2.4.1:/usr/local/rvm/gems/ruby-2.4.1@global
XDG_DATA_DIRS=/home/cloud_user/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share
LESSOPEN=||/usr/bin/lesspipe.sh %s
XDG_RUNTIME_DIR=/run/user/1002
RUBY_VERSION=ruby-2.4.1
_system_name=CentOS
_=/bin/env>>> os.environ
environ({'XDG_SESSION_ID': '9', 'rvm_bin_path': '/usr/local/rvm/bin', 'HOSTNAME': 'cddebed89c1c.mylabserver.com', 'GEM_HOME': '/usr/local/rvm/gems/ruby-2.4.1', 'TERM': 'xterm-256color', 'SHELL': '/bin/bash', 'HISTSIZE': '100000', 'IRBRC': '/usr/local/rvm/rubies/ruby-2.4.1/.irbrc', 'OLDPWD': '/home/cloud_user', 'MY_RUBY_HOME': '/usr/local/rvm/rubies/ruby-2.4.1', 'USER': 'cloud_user', 'LS_COLORS': ,'_system_type': 'Linux', 'rvm_path': '/usr/local/rvm', 'rvm_prefix': '/usr/local', 'MAIL': '/var/spool/mail/cloud_user', 'PATH': '/usr/local/rvm/gems/ruby-2.4.1/bin:/usr/local/rvm/gems/ruby-2.4.1@global/bin:/usr/local/rvm/rubies/ruby-2.4.1/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local/rvm/bin:/home/cloud_user/.local/bin:/home/cloud_user/bin', 'PWD': '/home/cloud_user/Documents', 'LANG': 'en_US.UTF-8', '_system_arch': 'x86_64', '_system_version': '7', 'HISTCONTROL': 'ignoredups', 'rvm_version': '1.29.3 (latest)', 'SHLVL': '1', 'HOME': '/home/cloud_user', 'LOGNAME': 'cloud_user', 'GEM_PATH': '/usr/local/rvm/gems/ruby-2.4.1:/usr/local/rvm/gems/ruby-2.4.1@global', 'XDG_DATA_DIRS': '/home/cloud_user/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share', 'LESSOPEN': '||/usr/bin/lesspipe.sh %s', 'XDG_RUNTIME_DIR': '/run/user/1002', 'RUBY_VERSION': 'ruby-2.4.1', '_system_name': 'CentOS', '_': '/bin/python3'})
```
 
 If we are looking for any specific environment variable, os.environ.get(<variable name>)
 
  ```bash
>>> os.environ.get('LOGNAME')
'cloud_user'
```
 
 To get the userid use os.getuid() or group id use os.getgid(). It’s similar to the id command in Linux.

 
  ```bash
$ id
uid=1002(cloud_user) gid=1003(cloud_user) groups=1003(cloud_user),10(wheel)>>> os.getuid()
1002
    
>>> os.getgid()
1003
```
Remove directory or remove directory recursively use os.rmdir() or remove directory recursively use os.removedirs().
  ```bash
>>> os.rmdir("mytest")>>> os.removedirs("test3/test4")
```
 To rename a file use os.rename()
   ```bash
# To rename a fileos.rename(<file to rename>, <destination file name>)
>>> os.rename("testfile","testfile1")>>> os.listdir()
['aristotle_politics.txt', 'cicero_disputations.txt', 'plato_republic.txt', 'secret.txt', 'Junk.txt', 'code_ideas.odt', 'reports.csv', 'testfile1']
```
