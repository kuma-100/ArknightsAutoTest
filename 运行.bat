@echo off
::配置AirtestIDE的地址
set a="E:\AirtestIDE_2020-01-20_py3_win64\AirtestIDE_2020-01-21_py3_win64\AirtestIDE"
::运行脚本
%a% runner ./RunTest.air --log log/ 
::生成报告html
%a% reporter ./RunTest.air --log_root log/ --lang zh
pause