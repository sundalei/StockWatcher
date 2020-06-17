mvn gwt:codeserver -pl *-client -am
mvn jetty:run -pl *-server -am -Denv=dev

netstat -ano| findstr "9876"
tasklist|findstr "24516"
taskkill /f /t /im java.exe