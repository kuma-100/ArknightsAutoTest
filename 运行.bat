@echo off
::����AirtestIDE�ĵ�ַ
set a="E:\AirtestIDE_2020-01-20_py3_win64\AirtestIDE_2020-01-21_py3_win64\AirtestIDE"
::���нű�
%a% runner ./RunTest.air --log log/ 
::���ɱ���html
%a% reporter ./RunTest.air --log_root log/ --lang zh
pause