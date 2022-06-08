import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class Hopeless
{
    static List<Entity> Entities = new ArrayList<Entity>();
    int FramesPerSecond = 30;
    int currentfps = 0;
    GameWindow gw;
    Thread run;
    float deltatime = 0;
    boolean rungame=true;
    Object FileClassObject;

    public void Instantiate(Entity e)
    {
        Entities.add(e);
    }

    public void stop()
    {
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