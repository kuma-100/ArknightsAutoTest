@echo off
::����AirtestIDE�ĵ�ַ
set a="F:\QA developer\AirtestIDE_2020-01-21_py3_win64\AirtestIDE"
::���нű�
%a% runner ./Runtest.air --log log/
::���ɱ���html
%a% reporter ./Runtest.air --log_root log/ --lang zh
pause