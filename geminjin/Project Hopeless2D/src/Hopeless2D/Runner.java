package Hopeless2D;

import java.io.BufferedReader;
import java.nio.file.Path;
import java.io.InputStreamReader;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.ArrayList;

public class Runner 
{
    public Runner(Path FILEPATH)
    {
        GameWindow gw= new GameWindow();
        gw.SetPath(FILEPATH.getParent().toString());
        gw.entityes = new ArrayList<Entity>();
        gw.ShowWindow();
        Hopeless hp = new Hopeless();
        hp.gw = gw;

        try
        {
            
            // Class<?> mainfile = new tempmainfilefortheshitthatistesting().getClass();
            // tempmainfilefortheshitthatistesting tmfftstit = new tempmainfilefortheshitthatistesting();
            // tmfftstit.hp = hp;
            // tmfftstit.setup();

            Runtime rt = Runtime.getRuntime();
            Process process = rt.exec(new String[]{"javac", /*"-cp", ".\\Hopeless2D\\Hopeless2D", */FILEPATH.getParent().toString()+"\\*.java"});
            process.waitFor();
            
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println("TEST: "+line);
            }

            
            URLClassLoader loader = new URLClassLoader(new URL[] 
            {
                FILEPATH.getParent().toUri().toURL()
            });
            Class<?> mainfile = loader.loadClass("Main");
            loader.close();
            
            Object tmfftstit = mainfile.getDeclaredConstructor().newInstance();
            hp.FileClassObject = tmfftstit;
            Field hpField = tmfftstit.getClass().getDeclaredField("hp");
            hpField.set(tmfftstit, hp);
            Method Setup = tmfftstit.getClass().getDeclaredMethod("setup");
            Setup.invoke(tmfftstit);
            // Method numinstance = tmfftstit.getClass().getDeclaredMethod("getNumOfInstances");
            // System.out.println("GameWindow Instances: "+ String.valueOf(gw.getNumOfInstances())+"\nHopeless Instances: "+String.valueOf(hp.getNumOfInstances())+"\nMain Instances: "+String.valueOf(numinstance.invoke(tmfftstit)));
        }
        catch (Exception e3)
        {
            e3.printStackTrace();
        }
    }
}
