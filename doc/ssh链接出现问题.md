### 在linux下传输文件，scp无法使用时。

```
解决办法：
1.**重启ssh** 
方案一：service sshd restart
方案二：systemctl restart sshd.service
2.删除**/.ssh/known_hosts** 这个文件
rm -rf known_hosts即可


 