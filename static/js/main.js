function conversion(){
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

function modal(){
    $('#Modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var day = button.data('day') // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var monthname = button.data('monthname')
        var modal = $(this)
        // modal.find('.modal-title').text(day)
        // modal.find('.modal-body input').val(day)

        // console.log(JSON.parse(day))
        console.log(monthname)
        // modal.find(".modal-content")
    })
}


function displayAll() {
    conversion();
    modal();
}


$(document).ready(displayAll)
