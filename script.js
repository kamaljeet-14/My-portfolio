$(document).ready(function() {
    $(window).scroll(function() {
        if (this.scrollY > 15) //window.scrollY bhi likh sakte the 
        {
            $('.navbar').addClass("sticky");
        } else {
            $('.navbar').removeClass("sticky");
        }
    })
});