$(document).ready(function () {
    $('.requests-article__number-button').on('click', function () {
        $(this).attr('hidden', '');
        let id = $(this).data('id');
        $(`#request-${ id }-tel`).removeAttr('hidden');
        let viewsCntSpan = $(`#request-${ id }-views-cnt`);
        let viewsCnt = viewsCntSpan.data('count');
        viewsCntSpan.data('count', viewsCnt + 1);
        viewsCntSpan.text(`${ viewsCnt + 1 } просмотров`)
    })
});