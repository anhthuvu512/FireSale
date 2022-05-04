$(document).ready(function () {
    $('#search-btn').on(types: 'click', selector: function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax(url: {
            url: '/items?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d =>{
                    return 
                })
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});