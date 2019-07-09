import os

domainhome = '/u01/oracle/user_projects/domains/base_domain'
admin_name = 'AdminServer'
apps_source_path = '/u01/oracle/container-scripts/'

print('Set resources and Deploy appications');

readDomain(domainhome)

cd('/')

# this is a library
app = create('CommonLibsWar', 'Library')
app.setSourcePath(apps_source_path + '/CommonLibsWar.war')
app.setStagingMode('nostage')
assign('Library', 'CommonLibsWar', 'Target', admin_name)

# this is a normal app
# app = create('CommonLibsWar', 'AppDeployment')
# app.setSourcePath(apps_source_path + '/CommonLibsWar.war')
# app.setStagingMode('nostage')
# assign('AppDeployment', 'CommonLibsWar', 'Target', admin_name)

updateDomain()
closeDomain()
exit()