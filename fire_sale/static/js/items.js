$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/sales?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="item">
                                <a href="/sales/${d.id}">
                                    <img class="item-img" src="/media/${d.firstImage}"/>
                                    <h4>${d.name}</h4>
                                </a>
                            </div>`
                })
                $('.items').html(newHtml.join(''))
                $('#search-box').val('')
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });

    $("select[name=sort]").change(function(){
        $("#yourFormId").submit();
    })
});