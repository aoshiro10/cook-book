$(document).ready(() => {
    $('.search_bar').keypress((event) => {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {
            filter();
        }
    });
});

function filter() {
    const filter_text = $('.search_bar').val();
    $.ajax({
        type: 'get',
        url: '/app/lazy_filter/',
        data: {
            'filter_text': filter_text
        },
        success: (data) => {
            $('.div_list').html(data.recipes_html);
            //alert(data.recipes_html);
        },
        error: (xhr, status, error) => {
            alert("Failure");
        }
    })
}