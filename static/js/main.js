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
        // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var day = button.data('day')
        var monthname = button.data('monthname')
        var year = button.data('year')
        var weekday = button.data('weekday')
        var location = button.data('location')
        var high = button.data('high')
        var low = button.data('low')
        var icon = button.data('icon')
        var iconurl = button.data('iconurl')
        var conditions = button.data('conditions')
        var humidity = button.data('humidity')
        var windDirection = button.data('wind-direction')
        var windStrength = button.data('wind-strength')
        var text = button.data('text')

        var modal = $(this)
        // modal.find('.modal-title').text(day)
        // modal.find('.modal-body input').val(day)

        // console.log(JSON.parse(day))
        console.log([day, monthname, year, weekday, location, high, low, icon,iconurl, conditions, humidity, windDirection, windStrength, text])
        // modal.find(".modal-content")
    })
}


function displayAll() {
    conversion();
    modal();
}


$(document).ready(displayAll)
