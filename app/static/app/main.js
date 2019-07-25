function filter() {
    const filter_text = $('.search_bar').val();
    $.ajax({
        type: 'get',
        url: '/app/lazy_filter/',
        data: {
            'filter_text': filter_text
        },
        success: (data) => {
            $('div_list').html(data.recipes_html);
            alert("Success");
        },
        error: (xhr, status, error) => {
            alert("Failure");
        }
    })
}