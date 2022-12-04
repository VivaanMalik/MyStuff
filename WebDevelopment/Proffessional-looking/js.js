function PlayAnim(e)
{
    document.getElementById(e).style.top = "0";
    document.getElementById(e).style.animation = "SlideInFormula .2s forwards";
}

function StopAnim(e)
{
    document.getElementById(e).style.top = "-1.2em";
    document.getElementById(e).style.animation = "SlideOutFormula .2s forwards";
}