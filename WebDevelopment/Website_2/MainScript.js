let SlideClasses = ["Slideshow1", 'Slideshow2'];
SlideIndexes = [0, 0];

window.onload = function showSlides()
{
    for (let SlideSet = 0; SlideSet < SlideClasses.length; SlideSet++) 
    {        
        let slides = document.getElementsByClassName(SlideClasses[SlideSet]);
        // let slides = [document.getElementById("Runestone")];
        console.log(slides.length)
        for (let i = 0; i < slides.length; i++) 
        {
            slides[i].style.display = "none";  
        }
        SlideIndexes[SlideSet]++;
        if (SlideIndexes[SlideSet] > slides.length) 
        {
            SlideIndexes[SlideSet] = 1
        }    
        slides[SlideIndexes[SlideSet]-1].style.display = "block";  
    }

    setTimeout(showSlides, 3000); // Change image every 2 seconds
}

function Ripple (event, e)
{
    let rippleeffect = document.createElement("span");
    rippleeffect.classList.add("ripple");
    e.appendChild(rippleeffect);
    let x = event.clientX - e.offsetLeft;
    let y = event.clientY - e.offsetTop;
    rippleeffect.style.left = `${x}px`;
    rippleeffect.style.top = `${y}px`;
    setTimeout(() => 
    {
        rippleeffect.remove();
    }, 300);
}