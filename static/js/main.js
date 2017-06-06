function displayAll(){
    metric = false;
    $("#convert-button").on('click', function(){
        if (metric == false){
            $(".imperial").css('display', 'none')
            $('.metric').css('display', 'block')
            $("#convert-button").html('IMPERIAL')
            $("#convert-button").css("background-color", "#000639")
            metric = true
        } else {
            $(".metric").css('display', 'none')
            $('.imperial').css('display', 'block')
            $("#convert-button").html('METRIC')
            $("#convert-button").css("background-color", "#660000")
            metric = false
        }
    });
}



$(document).ready(displayAll)
