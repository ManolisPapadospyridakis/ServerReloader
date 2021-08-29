# ServerReloader - An easy way to restart your web server when hot deployment is missing, e.g., Jetty
ServerReloader monitoring a specified src folder and restarts the server when detects changes, e.g, on Jetty web server.


# Youtube
Click [here](https://www.youtube.com/watch?v=iTK5W-AcH6k) to see a set up video 

# Usecases
Have you ever used [Java Spark](https://sparkjava.com/) or [Javalin](https://javalin.io/) web framework to build a web applications?
These two frameworks ships and uses the Jetty (embedded) webserver.
Jetty does not have a feature to hot deploy like Tomcat.
This python script can monitor your src folder and restart the web app, without you interference, make your life a bit easier.



# Before set up:
```
1. Create a Maven project
```
```
2. Add the dependencies of your libraries (here we use Javalin)
```
```
3. Make sure that the IDE 'Build Automatically' is disabled
```
```
4. Try to manually compile and run the app once to be sure that the 'mvn compile' and 'mvn exec:java -Dexec.mainClass=YOU_CLASS_WITH_MAIN_METHOD' works fine.
```

# Run the ServerReloader
```
1. Install python (https://www.python.org/downloads/)
```
```
2. Install psutil python library (pip install psutil) (https://pypi.org/project/psutil/)
```
```
3. Create a web app project
```
```
4. Use Maven or Gradle build tool
```

```
5. Start the server and enjoy the auto restart when you make changes on you src folder
```
* How to start the server when you use Maven as built automation tool. 
    * python path/to/ServerReloaderMain.py "fullpath/to/src" "mvn compile exec:java -Dexec.mainClass=HelloWorld --file /path/to/folder/that/contains/pom.xml" 0.5

    * Real example (on windows OS):
    python path/to/ServerReloaderMain.py "C:\\Users\\manol\\eclipse-workspace\\JavalinTestProject\\src" "mvn compile exec:java -Dexec.mainClass=HelloWorld --file C:\\Users\\manol\\eclipse-workspace\\JavalinTestProject" 0.5

* How to start the server when you use Gradle as built automation tool.
    * python path/to/ServerReloaderMain.py "fullpath/to/src" "gradle run  --project-dir     /path/to/folder/that/contains/gradle.build" 0.5
    * Real example (on windows OS): python path/to/ServerReloaderMain.py "C:\\Users\\manol\\eclipse-workspace\\JavalinWithGradle\\src" "gradle run  --project-dir C:\\Users\\manol\\eclipse-workspace\\JavalinWithGradle" 0.5

# ServerReloader - An easy way to restart your web server when hot deployment is missing, e.g., Jetty   

```
1. Be sure that you have disable the 'Build Automatically' from your IDE 
```

```
2. Create a Maven project
```
```
3. I have jdk 11 so we need to change appropriatly the release of the maven-compiler-plugin
```

```java
// 4. Write your code, copy from https://javalin.io/

import io.javalin.Javalin;

public class HelloWorld {
    public static void main(String[] args) {
        Javalin app = Javalin.create().start(7000);
        app.get("/", ctx -> ctx.result("Hello World"));
    }
}

```

```xml
5. In our example we will use the Javalin web framework. Let's set the dependencies
<dependencies>
    <dependency>
        <groupId>io.javalin</groupId>
        <artifactId>javalin</artifactId>
        <version>3.13.11</version>
    </dependency>

    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
        <version>1.7.30</version>
    </dependency>
</dependencies>
```

```
6. check that 'mvn compile' works fine
```

```
7. check that we can run our up with the mvn exec
   mvn exec:java -Dexec.mainClass=HelloWorld
```

```
8. Time to use our serverReloader
        
1. Download the code from git
2. We need to run the the script, so we can set the script to PATH or just cd into ServerReloader -> src folder
in my case 'cd C:\Users\manol\Desktop\ServerReloader\src'

3. We need to have python installed.
4. pip install psutil

5. Run the script: 
python ServerReloaderMain.py "C:\\Users\manol\\eclipse-workspace-2\\JavalinDemo\\src" "mvn compile exec:java -Dexec.mainClass=HelloWorld --file C:\\Users\\manol\\eclipse-workspace-2\\JavalinDemo" 0.5
```
