@echo off
::配置AirtestIDE的地址
set a="F:\QA developer\AirtestIDE_2020-01-21_py3_win64\AirtestIDE"
::运行脚本
%a% runner ./Runtest.air --log log/
::生成报告html
%a% reporter ./Runtest.air --log_root log/ --lang zh
pause