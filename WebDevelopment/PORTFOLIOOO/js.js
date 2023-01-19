window.onload = function()
{
    let r = document.getElementById("ripple");
    r.style.top=window.scrollY + "50vh";
    var x, y
    
    var firstTime = localStorage.getItem("first_time");
    t = 0 // 32
    if(!firstTime) 
    {
        
        document.getElementById("ripple").classList.remove("initripple");
        t=32
    }
    localStorage.setItem("first_time","1");
    localStorage.removeItem("first_time")

    document.onmousemove = move;
    function move(event)
    {
        if (window.event)
        {
            x = event.x; // there are other values depending on your needs
            y = event.y; // one is clientX. Can't remember the others offhand
        }
        else
        {
            x = evt.x;
            y = evt.y;
        }
    }
    function ripple(element)
    {
        let r = document.getElementById("ripple");
        r.classList.add('ripple');
        r.style.left = `${(element.getBoundingClientRect().left + element.getBoundingClientRect().right)/2}px`;
        r.style.top = `${(element.getBoundingClientRect().top + element.getBoundingClientRect().bottom)/2 + window.scrollY}px`;
        setTimeout(function(){r.classList.remove("ripple");}, 2000);
        console.log(r);
    }
    document.body.scrollTop = document.documentElement.scrollTop = 0;
    elementss = document.getElementsByClassName('Work');

    [...elementss].forEach(element => 
    {
        element.addEventListener('click', function()
        {
            console.log('click');
            [...elementss].forEach(element => 
            {
                element.classList.remove('click');
            });
            element.classList.add('click');
            ripple(element);
            setTimeout(function(){window.location.href=document.querySelector('.click').dataset.link;element.classList.remove('click');}, 1000);
        });
    });

    elements = document.getElementsByClassName('Skill');
    [...elements].forEach(element => 
    {
        [...element.children].forEach(element_2 => 
        {
            element_2.style.width = "0px";
        });
    });

    function stopscroll()
    {
        document.body.classList.add("StopScroll");
    }

    function startscroll()
    {
        document.body.classList.remove("StopScroll");
    }

    function sett(val)
    {
        t = val;
    }
    
    var i = 0;
    var i2 = 0;
    varitxt = "C:\\Users\\Vivaan Malik\\Young Developer\\Portfolio>";
    var txt = "startC:\\Users\\Vivaan Malik\\Portfolio.exe";
    document.getElementsByClassName("cmd")[0].innerHTML = varitxt;

    setTimeout(tw, t);
    function tw()
    {
        if (i<txt.length)
        {
            document.getElementsByClassName("cmd")[0].innerHTML=document.getElementsByClassName("cmd")[0].innerHTML.replace(/(\s+)?.$/, '').replace("start", "start ");
            document.getElementsByClassName("cmd")[0].innerHTML += txt.charAt(i);
            document.getElementsByClassName("cmd")[0].innerHTML += "_";
            i++;
            setTimeout(tw, t );
        }
        else
        {
            setTimeout(twe, t *20);
        }
    }

    function twe()
    {
        if (i2<5)
        {
            if (i2%2==0)
            {
                document.getElementsByClassName("cmd")[0].innerHTML=document.getElementsByClassName("cmd")[0].innerHTML.replace(/(\s+)?.$/, '');
            }
            else
            {
                document.getElementsByClassName("cmd")[0].innerHTML+="_";
            }
            i2++;
            setTimeout(twe, t *20)
        }
        else
        {
            document.getElementsByClassName("cmd_container")[0].classList.add("fade")
            document.getElementsByClassName("MainContent")[0].classList.add("active")
            setTimeout(twt1, 500)
        }
    }

    var i3 = 0;
    var i4 = 0;
    var txt1 = "> My name is Vivaan Malik";
    var txt2 = "> I am a young developer...";

    setTimeout(tw, t);
    function twt1()
    {
        if (i3<txt1.length)
        {
            document.getElementsByClassName("t1")[0].innerHTML=document.getElementsByClassName("t1")[0].innerHTML.replace("_", '');
            document.getElementsByClassName("t1")[0].innerHTML += txt1.charAt(i3);
            document.getElementsByClassName("t1")[0].innerHTML += "_";
            i3++;
            setTimeout(twt1, t);
        }
        else
        {
            setTimeout(twt2, t*20);
            document.getElementsByClassName("t1")[0].innerHTML=document.getElementsByClassName("t1")[0].innerHTML.replace("_", '');
        }
    }

    function twt2()
    {
        if (i4<txt2.length)
        {
            document.getElementsByClassName("t2")[0].innerHTML=document.getElementsByClassName("t2")[0].innerHTML.replace("_", '');
            document.getElementsByClassName("t2")[0].innerHTML += txt2.charAt(i4);
            document.getElementsByClassName("t2")[0].innerHTML += "_";
            i4++;
            setTimeout(twt2, t);
        }
        else
        {
            document.getElementsByClassName("t2")[0].innerHTML=document.getElementsByClassName("t2")[0].innerHTML.replace("_", '');
            setInterval(function(){document.getElementsByClassName("slidetitle")[0].classList.add("active")}, t*66);
            setInterval(function(){document.getElementsByClassName("slidetitletext")[0].classList.add("active")}, t*66);
            setInterval(function(){startscroll()}, t*66);
            setInterval(function(){document.getElementsByClassName("mainmaincontent")[0].classList.add("active")}, t*66);
        }
    }


    // navbar and skills

    const list = document.querySelectorAll(".list");


    function isInViewport(element) 
    {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    function AboveViewport(element) 
    {
        const rect = element.getBoundingClientRect();
        return (rect.top <= 0);
    }

    var percents=["70%", "100%", "30%", "80%"];
    window.addEventListener('scroll', () =>
    {
        elements = document.getElementsByClassName('Skill');
        var j = 0;
        [...elements].forEach(element => 
        {
            if(isInViewport(element))
            {
                var i=0;
                [...element.children].forEach(element_2 => 
                {
                    var v = percents[j];
                    setInterval(function(){element_2.style.width = v;}, i*333);
                    i++;
                });
            }
            j++;
        });
        
        const list2 = document.querySelectorAll(".seperator");
        var k =1;
        list2.forEach((item)=>
        {
            if(AboveViewport(item))
            {
                k++;
            }
        });
        var l = 0;
        list.forEach((item)=>
        {
            l++;
            item.classList.remove("active");
            if (k==l)
            {
                item.classList.add("active");
            }
        });
    });

};
