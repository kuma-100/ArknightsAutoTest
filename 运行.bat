@echo off
::配置AirtestIDE的地址
set a="F:\work\AirtestIDE-win-1.2.14\AirtestIDE\AirtestIDE"
::运行脚本
%a% runner ./Runtest.air --log log/
::生成报告html
%a% reporter ./Runtest.air --log_root log/ --lang zh
pause