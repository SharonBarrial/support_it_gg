"""
.
✅ The Powershell process is the parent process for notepad.exe.
(When you launch notepad.exe from PowerShell, PowerShell becomes its parent process.)

2.
✅ init
(init is the first process started in Linux and always has PID 1. In modern systems, it may be a symlink to systemd.)

3.
✅ From the CLI, use the tasklist command.
✅ Use the Windows Task Manager.
✅ From the PowerShell prompt, use the Get-Process commandlet.
(The ps command is native to Linux/Unix, not Windows.)

4.
✅ Use the ps -x command.
✅ List the contents of the /proc directory.
(The ls command just lists files; /etc does not contain process info.)

5.
✅ To terminate the process that is signaled
(SIGINT = "interrupt" — it terminates the process unless handled.)

6.
✅ Kill Process
✅ Kill Process Tree
(Both options in Process Explorer terminate processes. "Suspend" pauses; "Restart" is not always available.)

7.
✅ SIGTERM
(By default, kill pid sends SIGTERM, which politely asks the process to terminate.)

8.
✅ Close apps, one at a time, starting with the foreground app.
(This helps isolate the misbehaving app. The foreground app is the most immediate suspect.)

9.
✅ Process information along with data about the resources that the process is consuming
✅ Information about particular resources on the system (like CPU, Memory, and Network usage)
(Resource Monitor focuses on real-time resource usage, not system uptime or hardware properties.)

10.
✅ uptime
(The uptime command displays time running, users logged in, and load average.)
"""
