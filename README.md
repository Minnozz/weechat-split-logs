# weechat-split-logs
Script to split existing weechat logs into multiple files based on date.

The weechat setting that does this is `logger.file.mask`. This is script is useful for converting your old, huge log files that are not yet split by date into multiple files.

## Usage
```
./weechat-split-logs <log/dir> <output/dir/with/%Y/%m>
```
Available date placeholder: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

## Example
- Make a backup of your log files. I wouldn't just trust a random script from The Internet.
- Change the weechat setting `logger.file.mask` to the desired value. weechat will start writing log files to the new locations.
- Then, run this script to convert the old log files:
```
$ ls ~/.weechat/logs/**/irc.server.freenode.weechatlog
/home/minnozz/.weechat/logs/irc.server.freenode.weechatlog
$ ./weechat-split-logs ~/.weechat/logs ~/.weechat/logs/%Y/%m
$ ls ~/.weechat/logs/**/irc.server.freenode.weechatlog
/home/minnozz/.weechat/logs/irc.server.freenode.weechatlog
/home/minnozz/.weechat/logs/2017/07/irc.server.freenode.weechatlog
/home/minnozz/.weechat/logs/2017/08/irc.server.freenode.weechatlog
(...)
/home/minnozz/.weechat/logs/2020/05/irc.server.freenode.weechatlog
/home/minnozz/.weechat/logs/2020/05/irc.server.freenode.weechatlog.split
```
- Files ending in `.split` will be created when weechat has already created a file in the location we want to write to. We can't just append to that file because then the lines would be in incorrect order, and weechat probably still has the file opened.
- Check if the script worked correctly and delete the old (non-split) files if you want.

## Caveats
- Only the date part of the timestamp is read, so time placeholders are not available.
- Placeholders are only supported in the directory name, because the file name is identical to the input file.
