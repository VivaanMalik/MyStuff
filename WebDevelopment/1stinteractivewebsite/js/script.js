const html = document.documentElement;
const frameCount=148;

function RevealMsg()
{
    document.body.classList.add("stop-scrolling");
    document.getElementById("HiddenMsg").style.display='block';
    document.getElementById("HiddenImg").style.display='block';
}

const preloadImages = () => {
    for (let i = 1; i < frameCount; i++) {
      const img = new Image();
      img.src = `https://www.apple.com/105/media/us/airpods-pro/2019/1299e2f5_9206_4470_b28e_08307a42f19b/anim/sequence/large/01-hero-lightpass/${(i).toString().padStart(4, '0')}.jpg`;
    }
};

window.addEventListener('scroll', () => 
{  
    const scrollTop = html.scrollTop;
    const maxScrollTop = html.scrollHeight - window.innerHeight;
    const scrollFraction = scrollTop / maxScrollTop;
    const frameIndex = Math.min(frameCount-2, Math.ceil(scrollFraction * frameCount));
    const url=`url(https://www.apple.com/105/media/us/airpods-pro/2019/1299e2f5_9206_4470_b28e_08307a42f19b/anim/sequence/large/01-hero-lightpass/${(frameIndex+1).toString().padStart(4, '0')}.jpg)`
    document.getElementById("HiddenImg").style["background-image"]=url;
});

preloadImages();