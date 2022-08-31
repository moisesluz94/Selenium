@echo off
For /F "UseBackQ Delims==" %%A In ("C:\Zabbix\ExecPython\log.txt") Do Set "lastline=%%A"
Echo %lastline%
pause