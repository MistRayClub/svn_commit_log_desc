from com.mist.svn import svnCommitLog
from com.mist.svn import readExcle3
#ģ��·��
template_path = 'G:/data/zhoubao3.xlsx'
#���·��
output_file_path = 'G:/data/ouput.xlsx'
logs = svnCommitLog.getSvnLog('G: && cd gjyWorkSpace/SMFdev/SMF && svn log --search ' + 'userName')
#����ģ������excel
readExcle3.write_data(logs,template_path,output_file_path)
