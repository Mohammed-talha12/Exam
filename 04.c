/* 
public class Test
{
public static void main(String[] args)
{
int a=20,b=30,c;
c=a*b;
System.out.println("Hello world");
System.out.println("value of c is "+c);
}
}

create a Dockerfile
FROM openjdk # uses the base image –openjdk with java installed
WORKDIR /sam  # Set the working directory
COPY. /sam   # Copies all the files to working directory
RUN javac Test.java  # Compile the Java program
CMD ["java", "Test"]   # Set the default command to run the Java program






*/