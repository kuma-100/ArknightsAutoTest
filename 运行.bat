@echo off
::����AirtestIDE�ĵ�ַ
set a="F:\work\AirtestIDE-win-1.2.14\AirtestIDE\AirtestIDE"
::���нű�
%a% runner ./Runtest.air --log log/
::���ɱ���html
%a% reporter ./Runtest.air --log_root log/ --lang zh
pause