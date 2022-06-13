package Hopeless2D;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class Hopeless
{
    static List<Entity> Entities = new ArrayList<Entity>();
    public int FramesPerSecond = 30;
    int currentfps = 0;
    public GameWindow gw;
    Thread run;
    public float deltatime = 0;
    public boolean rungame=true;
    public Object FileClassObject;

    // . . .
    private static int counter;

    public Hopeless() 
    {
        counter++;
    }

    public int getNumOfInstances() 
    {
        return counter;
    }
    // . . .

    public String ProjectPath()
    {
        return gw.GetPath();
    }

    public float DeltaTime()
    {
        return deltatime;
    }

    public int getCurrentFps()
    {
        return currentfps;
    }

    public void SetFrameRate(int fps)
    {
        FramesPerSecond = fps;
    }

    public void Instantiate(Entity e)
    {
        Entities.add(e);
    }

    public void stop()
    {
        gw = null;
        rungame=false;
    }

    public void run()
    {
        gw.hp = this;
        run = new Thread()
        {
            public void run()
            {
                Timer timer = new Timer();
                timer.schedule(new PrintFPS(), 1000, 1000);
                
                Method Frame = null;
                try
                {
                    Frame = FileClassObject.getClass().getDeclaredMethod("Frame");
                }
                catch (NoSuchMethodException | SecurityException e)
                {
                    e.printStackTrace();
                }

                while (rungame==true)
                {
                    long prevtime = System.currentTimeMillis();

                    try 
                    {
                        Frame.invoke(FileClassObject);
                    } 
                    catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException e1) 
                    {
                        e1.printStackTrace();
                    }

                    gw.entityes = Entities;
                    gw.UpdateWindow();
                    currentfps+=1;

                    long aftatime = System.currentTimeMillis();
                    long timedifference = aftatime-prevtime;
                    int mswait = (1000/FramesPerSecond) - (int)timedifference;
                    deltatime = (float) (mswait+(int)timedifference)/1000f;
                    if (deltatime<0)
                    {
                        deltatime = 0f;
                    }
                    if (mswait>0)
                    {
                        try 
                        {
                            Thread.sleep(mswait);
                        } 
                        catch (InterruptedException e) 
                        {
                            e.printStackTrace();
                        }
                    }
                }
                timer.cancel();
                timer.purge();
                run=null;
            }    
        };
        run.start();
    }

    class PrintFPS extends TimerTask
    {
        @Override
        public void run() 
        {
            // System.out.println(currentfps);
            currentfps=0;
        }
    }
}