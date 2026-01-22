param (
    [Parameter(Mandatory)]
    [string]$workspaceFolder
)

mvn clean package

Copy-Item -Force "${workspaceFolder}\target\*.war" "C:\Program Files\Apache Software Foundation\Tomcat 10.1\webapps"